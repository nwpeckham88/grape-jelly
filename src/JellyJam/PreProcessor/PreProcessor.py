import os
import ffmpeg
from ffmpeg_normalize import FFmpegNormalize, SubtitleStream, VideoStream, AudioStream

class PreProcessor:
    def __init__(self):
        pass

    def run_volumedetect(self, input_file):
        """
        Run volumedetect via ffmpeg on the given input file.
        
        Args:
            input_file (str): The path to the input file.
        
        Returns:
            dict: A dictionary containing the volumedetect results.
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

    def filter_subtitles_by_language(self, streams):
        """
        Filter subtitle streams based on the language set in the environment variable.
        
        Args:
            streams (list): A list of stream objects.
        
        Returns:
            list: A list of subtitle streams that match the desired languages.
        """
        desired_languages = os.getenv('SUBTITLE_LANGUAGES', '').split(',')
        filtered_subtitles = [
            stream for stream in streams
            if isinstance(stream, SubtitleStream) and stream.tags.get('language') in desired_languages
        ]
        return filtered_subtitles

    def analyze_file(self, input_file):
        """
        Analyze the given input file for various properties.
        
        Args:
            input_file (str): The path to the input file.
        
        Returns:
            dict: A dictionary containing the analysis results.
        """
        volumedetect_results = self.run_volumedetect(input_file)
        streams = self.get_streams(input_file)
        subtitle_streams = self.filter_subtitles_by_language(streams)
        # Add more analysis functions here if needed
        analysis_results = {
            'volumedetect': volumedetect_results,
            'streams': streams,
            'filtered_subtitles': subtitle_streams,
            # Add more results here if needed
        }
        return analysis_results

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

# Example usage:
# preprocessor = PreProcessor()
# config = preprocessor.create_ffmpeg_normalize_config('path/to/your/file.mp4')
# print(config)
# ebu_r128_results = preprocessor.run_ebu_r128('path/to/your/file.mp4')
# print(ebu_r128_results)