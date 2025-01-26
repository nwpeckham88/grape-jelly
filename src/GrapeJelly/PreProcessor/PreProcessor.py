import os
import ffmpeg
from ffmpeg_normalize import SubtitleStream, VideoStream, AudioStream

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

# Example usage:
# preprocessor = PreProcessor()
# results = preprocessor.analyze_file('path/to/your/file.mp4')
# print(results)