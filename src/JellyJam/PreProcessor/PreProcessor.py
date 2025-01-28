import os
import ffmpeg
import sqlite3
from ffmpeg_normalize import FFmpegNormalize, SubtitleStream, VideoStream, AudioStream

class PreProcessor:
    def __init__(self, db_path):
        self.db_path = db_path
        self._create_tables()
        self.subtitle_languages = os.getenv('SUBTITLE_LANGUAGES', '').split(',')

    def _create_tables(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Removed duplicate creation of streams table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS shows (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS seasons (
                id INTEGER PRIMARY KEY,
                show_id INTEGER NOT NULL,
                season_number INTEGER NOT NULL,
                FOREIGN KEY (show_id) REFERENCES shows(id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS episodes (
                id INTEGER PRIMARY KEY,
                season_id INTEGER NOT NULL,
                episode_number INTEGER NOT NULL,
                title TEXT NOT NULL,
                FOREIGN KEY (season_id) REFERENCES seasons(id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS volumedetect_results (
                id INTEGER PRIMARY KEY,
                episode_id INTEGER NOT NULL,
                mean_volume REAL,
                max_volume REAL,
                histogram_0db REAL,
                FOREIGN KEY (episode_id) REFERENCES episodes(id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS streams (
                id INTEGER PRIMARY KEY,
                episode_id INTEGER NOT NULL,
                codec_type TEXT,
                codec_name TEXT,
                width INTEGER,
                height INTEGER,
                language TEXT,
                FOREIGN KEY (episode_id) REFERENCES episodes(id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subtitles (
                id INTEGER PRIMARY KEY,
                episode_id INTEGER NOT NULL,
                language TEXT,
                FOREIGN KEY (episode_id) REFERENCES episodes(id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ebu_r128_results (
                id INTEGER PRIMARY KEY,
                episode_id INTEGER NOT NULL,
                integrated REAL,
                range REAL,
                lra_low REAL,
                lra_high REAL,
                sample_peak REAL,
                true_peak REAL,
                FOREIGN KEY (episode_id) REFERENCES episodes(id)
            )
        ''')
        conn.commit()
        conn.close()

    def store_volumedetect_results(self, episode_id, volumedetect_results):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO volumedetect_results (episode_id, mean_volume, max_volume, histogram_0db)
            VALUES (?, ?, ?, ?)
        ''', (episode_id, volumedetect_results.get('mean_volume'), volumedetect_results.get('max_volume'), volumedetect_results.get('histogram_0db')))
        conn.commit()
        conn.close()

    def store_streams(self, episode_id, streams):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for stream in streams:
            cursor.execute('''
                INSERT INTO streams (episode_id, codec_type, codec_name, width, height, language)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (episode_id, stream.get('codec_type'), stream.get('codec_name'), stream.get('width'), stream.get('height'), stream.get('language')))
        conn.commit()
        conn.close()

    def store_subtitles(self, episode_id, subtitles):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for subtitle in subtitles:
            cursor.execute('''
                INSERT INTO subtitles (episode_id, language)
                VALUES (?, ?)
            ''', (episode_id, subtitle.get('language')))
        conn.commit()
        conn.close()

    def store_streams(self, streams):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for stream in streams:
            cursor.execute('''
                INSERT INTO streams (codec_type, codec_name, width, height, language)
                VALUES (?, ?, ?, ?, ?)
            ''', (stream.codec_type, stream.codec_name, getattr(stream, 'width', None), getattr(stream, 'height', None), getattr(stream, 'language', None)))
        conn.commit()
        conn.close()

    def store_streams_without_episode_id(self, streams):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for stream in streams:
            cursor.execute('''
                INSERT INTO streams (codec_type, codec_name, width, height, language)
                VALUES (?, ?, ?, ?, ?)
            ''', (stream.codec_type, stream.codec_name, getattr(stream, 'width', None), getattr(stream, 'height', None), getattr(stream, 'language', None)))
        conn.commit()
        conn.close()

    def run_volumedetect(self, input_file):
        """
        Run ffmpeg volumedetect on the given input file.
        
        Args:
            input_file (str): The path to the input file.
        
        Returns:
            dict: A dictionary containing the volumedetect results.
        
        Raises:
            RuntimeError: If ffmpeg volumedetect fails.
        """
        try:
            out, err = (
                ffmpeg
                .input(input_file)
                .output('null', af='volumedetect', f='null')
                .run(capture_stdout=True, capture_stderr=True)
            )
        except ffmpeg.Error as e:
            raise RuntimeError(f"ffmpeg volumedetect failed: {e.stderr.decode()}")

        volumedetect_results = self.parse_volumedetect_output(err.decode())
        return volumedetect_results

    def parse_volumedetect_output(self, output):
        """
        Parse the output from ffmpeg volumedetect.
        
        Args:
            output (str): The stderr output from ffmpeg volumedetect.
        
        Returns:
            dict: A dictionary containing the parsed volumedetect results.
            The dictionary has the following keys:
                - mean_volume (float): The mean volume in dB.
                - max_volume (float): The maximum volume in dB.
                - histogram_0db (float): The percentage of samples at 0 dB.
        """
        results = {}
        for line in output.split('\n'):
            if 'mean_volume:' in line:
                results['mean_volume'] = float(line.split('mean_volume:')[1].strip().split()[0])
            elif 'max_volume:' in line:
                results['max_volume'] = float(line.split('max_volume:')[1].strip().split()[0])
            elif 'histogram_0db:' in line:
                results['histogram_0db'] = float(line.split('histogram_0db:')[1].strip().split()[0])
        return results

    def get_streams(self, input_file):
        """
        Get the streams in the given input file using ffprobe.
        
        Args:
            input_file (str): The path to the input file.
        
        Returns:
            list: A list of stream objects containing stream information.
        
        Raises:
            RuntimeError: If ffprobe fails.
        """
        try:
            probe = ffmpeg.probe(input_file)
        except ffmpeg.Error as e:
            raise RuntimeError(f"ffprobe failed: {e.stderr.decode()}")

        streams = []
        for stream in probe.get('streams', []):
            codec_type = stream.get('codec_type')
            if codec_type == 'video':
                streams.append(VideoStream(**stream))
            elif codec_type == 'audio':
                streams.append(AudioStream(**stream))
            elif codec_type == 'subtitle':
                streams.append(SubtitleStream(**stream))
        
        return streams

    def filter_subtitles_by_language(self, streams, desired_languages):
        """
        Filter subtitle streams based on the provided languages.
        
        Args:
            streams (list): A list of stream objects. Each stream object is a dictionary containing stream information.
            desired_languages (list): A list of desired subtitle languages. Each language is represented as a string.
        
        Returns:
            list: A list of subtitle streams that match the desired languages.
        """
        filtered_subtitles = [
            stream for stream in streams
            if isinstance(stream, SubtitleStream) and stream.tags.get('language') in desired_languages
        ]
        return filtered_subtitles

    def analyze_file(self, input_file, episode_id):
        """
        Analyze the given input file for various properties.
        
        Args:
            input_file (str): The path to the input file.
            episode_id (int): The ID of the episode in the database.
        
        Returns:
            dict: A dictionary containing the analysis results.
        """
        volumedetect_results = self.run_volumedetect(input_file)
        streams = self.get_streams(input_file)
        subtitle_streams = self.filter_subtitles_by_language(streams, self.subtitle_languages)
        ebu_r128_results = self.run_ebu_r128(input_file)
        
        # Add more analysis functions here if needed
        analysis_results = {
            'volumedetect': volumedetect_results,
            'streams': streams,
            'filtered_subtitles': subtitle_streams,
            'ebu_r128': ebu_r128_results,
            # Add more results here if needed
        }
        self.store_volumedetect_results(episode_id, volumedetect_results)
        self.store_streams(episode_id, streams)
        self.store_subtitles(episode_id, subtitle_streams)
        self.store_ebu_r128_results(episode_id, ebu_r128_results)
        return analysis_results

    def store_ebu_r128_results(self, episode_id, ebu_r128_results):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO ebu_r128_results (episode_id, integrated, range, lra_low, lra_high, sample_peak, true_peak)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            episode_id,
            ebu_r128_results.get('integrated'),
            ebu_r128_results.get('range'),
            ebu_r128_results.get('lra_low'),
            ebu_r128_results.get('lra_high'),
            ebu_r128_results.get('sample_peak'),
            ebu_r128_results.get('true_peak')
        ))
        conn.commit()
        conn.close()

    def create_ffmpeg_normalize_config(self, input_file):
        """
        Create a configuration object for ffmpeg-normalize based on the analysis results.
        
        Args:
            input_file (str): The path to the input file.
        
        Returns:
            dict: A configuration object for ffmpeg-normalize.
        """
        analysis_results = self.analyze_file(input_file)
        streams = analysis_results['streams']
        volumedetect_results = analysis_results['volumedetect']
        
        config = {
            'input_file': input_file,
            'streams': streams,
            'volumedetect': volumedetect_results,
            # Add more configuration options here if needed
        }
        
        return config

    def run_ebu_r128(self, input_file, video=0, size='640x480', meter=9, metadata=0, framelog='info', peak='none', dualmono=False, panlaw=-3.01, target=-23, gauge='momentary', scale='absolute'):
        """
        Run EBU R128 scanner filter on the given input file.
        
        Args:
            input_file (str): The path to the input file.
            video (int): Activate the video output. Default is 0.
            size (str): Set the video size. Default is '640x480'.
            meter (int): Set the EBU scale meter. Default is 9.
            metadata (int): Set metadata injection. Default is 0.
            framelog (str): Force the frame logging level. Default is 'info'.
            peak (str): Set peak mode(s). Default is 'none'.
            dualmono (bool): Treat mono input files as "dual mono". Default is False.
            panlaw (float): Set a specific pan law. Default is -3.01.
            target (int): Set a specific target level in LUFS. Default is -23.
            gauge (str): Set the value displayed by the gauge. Default is 'momentary'.
            scale (str): Sets the display scale for the loudness. Default is 'absolute'.
        
        Returns:
            dict: A dictionary containing the EBU R128 results.
        """
        try:
            out, err = (
                ffmpeg
                .input(input_file)
                .filter('ebur128', video=video, size=size, meter=meter, metadata=metadata, framelog=framelog, peak=peak, dualmono=dualmono, panlaw=panlaw, target=target, gauge=gauge, scale=scale)
                .output('null', f='null')
                .run(capture_stdout=True, capture_stderr=True)
            )
        except ffmpeg.Error as e:
            raise RuntimeError(f"ffmpeg ebur128 failed: {e.stderr.decode()}")

        ebur128_results = self.parse_ebu_r128_output(err.decode())
        
        return ebur128_results

    def parse_ebu_r128_output(self, output):
        """
        Parse the output from ffmpeg ebur128.
        
        Args:
            output (str): The stderr output from ffmpeg ebur128.
        
        Returns:
            dict: A dictionary containing the parsed ebur128 results.
        """
        results = {}
        for line in output.split('\n'):
            if 'I:' in line:
                results['integrated'] = float(line.split('I:')[1].strip().split()[0])
            elif 'LRA:' in line:
                results['range'] = float(line.split('LRA:')[1].strip().split()[0])
            elif 'LRA low:' in line:
                results['lra_low'] = float(line.split('LRA low:')[1].strip().split()[0])
            elif 'LRA high:' in line:
                results['lra_high'] = float(line.split('LRA high:')[1].strip().split()[0])
            elif 'Sample peak:' in line:
                results['sample_peak'] = float(line.split('Sample peak:')[1].strip().split()[0])
            elif 'True peak:' in line:
                results['true_peak'] = float(line.split('True peak:')[1].strip().split()[0])
        
        return results

    def process_file(self, input_file):
        try:
            probe = ffmpeg.probe(input_file)
        except ffmpeg.Error as e:
            raise RuntimeError(f"ffprobe failed: {e.stderr.decode()}")

        streams = []
        for stream in probe.get('streams', []):
            codec_type = stream.get('codec_type')
            if codec_type == 'video':
                streams.append(VideoStream(**stream))
            elif codec_type == 'audio':
                streams.append(AudioStream(**stream))
            elif codec_type == 'subtitle':
                streams.append(SubtitleStream(**stream))
        
        self.store_streams(streams)
        return streams

# Example usage:
# preprocessor = PreProcessor('path/to/your/database.db')
# config = preprocessor.create_ffmpeg_normalize_config('path/to/your/file.mp4')
# print(config)
# ebu_r128_results = preprocessor.run_ebu_r128('path/to/your/file.mp4')
# print(ebu_r128_results)