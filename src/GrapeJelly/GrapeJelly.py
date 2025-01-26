import os
import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from ffmpeg_normalize import FFmpegNormalize
from prettytable import PrettyTable
import ffmpeg

class GrapeJelly:
    def __init__(self, directories):
        self.directories = directories
        self.observer = Observer()
        self.audio_codec = os.getenv('AUDIO_CODEC', 'eac3')
        self.audio_bitrate = os.getenv('AUDIO_BITRATE', '256k')
        self.sample_rate = os.getenv('SAMPLE_RATE', '48000')
        self.loudness_target = os.getenv('LOUDNESS_TARGET', '-23.0')
        self.true_peak = os.getenv('TRUE_PEAK', '-2.0')
        self.loudness_range_target = os.getenv('LOUDNESS_RANGE_TARGET', '7.0')
        self.video_codec = os.getenv('VIDEO_CODEC', 'copy')
        self.file_extensions = os.getenv('FILE_EXTENSIONS', '.mp4,.mkv,.avi').split(',')
        self.file_extensions.append('.grapejelly')
        self.force = os.getenv('FORCE', 'false').lower() == 'true'
        self.debug = os.getenv('DEBUG', 'false').lower() == 'true'
        self.verbose = os.getenv('VERBOSE', 'false').lower() == 'true'
        self.quiet = os.getenv('QUIET', 'false').lower() == 'true'
        self.dry_run = os.getenv('DRY_RUN', 'false').lower() == 'true'
        self.progress = os.getenv('PROGRESS', 'true').lower() == 'true'
        self.normalization_type = os.getenv('NORMALIZATION_TYPE', 'ebu')
        self.print_stats = os.getenv('PRINT_STATS', 'true').lower() == 'true'
        self.keep_loudness_range_target = os.getenv('KEEP_LOUDNESS_RANGE_TARGET', 'false').lower() == 'true'
        self.keep_lra_above_loudness_range_target = os.getenv('KEEP_LRA_ABOVE_LOUDNESS_RANGE_TARGET', 'false').lower() == 'true'
        self.offset = float(os.getenv('OFFSET', '0.0'))
        self.lower_only = os.getenv('LOWER_ONLY', 'false').lower() == 'true'
        self.auto_lower_loudness_target = os.getenv('AUTO_LOWER_LOUDNESS_TARGET', 'false').lower() == 'true'
        self.dual_mono = os.getenv('DUAL_MONO', 'false').lower() == 'true'
        self.dynamic = os.getenv('DYNAMIC', 'false').lower() == 'true'
        self.keep_original_audio = os.getenv('KEEP_ORIGINAL_AUDIO', 'false').lower() == 'true'
        self.pre_filter = os.getenv('PRE_FILTER', '')
        self.post_filter = os.getenv('POST_FILTER', '')
        self.video_disable = os.getenv('VIDEO_DISABLE', 'false').lower() == 'true'
        self.subtitle_disable = os.getenv('SUBTITLE_DISABLE', 'false').lower() == 'true'
        self.metadata_disable = os.getenv('METADATA_DISABLE', 'false').lower() == 'true'
        self.chapters_disable = os.getenv('CHAPTERS_DISABLE', 'false').lower() == 'true'
        self.processed_files = self.load_state()

    def load_state(self):
        processed_files = {}
        for directory in self.directories:
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.endswith('.grapejelly'):
                        with open(os.path.join(root, file), 'r') as f:
                            processed_files[file[:-10]] = json.load(f)
        return processed_files

    def save_state(self, file_path, state):
        state_file = f"{file_path}.grapejelly"
        with open(state_file, 'w') as f:
            json.dump(state, f)

    def run(self):
        event_handler = Handler(self)
        for directory in self.directories:
            self.observer.schedule(event_handler, directory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

    def normalize_audio(self, file_path):
        state_file = f"{file_path}.grapejelly"
        if os.path.exists(state_file):
            with open(state_file, 'r') as f:
                state = json.load(f)
                if state.get('normalized') == 'Processing':
                    print(f"File {file_path} is currently being processed.")
                    return
                elif state.get('normalized') == 'True':
                    print(f"File {file_path} has already been processed.")
                    return

        initial_state = {
            'normalized': 'Processing',
            'audio_codec': self.audio_codec,
            'audio_bitrate': self.audio_bitrate,
            'sample_rate': self.sample_rate,
            'loudness_target': self.loudness_target,
            'true_peak': self.true_peak,
            'loudness_range_target': self.loudness_range_target,
            'video_codec': self.video_codec
        }
        self.save_state(file_path, initial_state)

        normalizer = FFmpegNormalize(
            audio_codec=self.audio_codec,
            audio_bitrate=self.audio_bitrate,
            sample_rate=self.sample_rate,
            loudness_target=self.loudness_target,
            true_peak=self.true_peak,
            loudness_range_target=self.loudness_range_target,
            video_codec=self.video_codec,
            force=self.force,
            debug=self.debug,
            verbose=self.verbose,
            quiet=self.quiet,
            dry_run=self.dry_run,
            progress=self.progress,
            normalization_type=self.normalization_type,
            print_stats=self.print_stats,
            keep_loudness_range_target=self.keep_loudness_range_target,
            keep_lra_above_loudness_range_target=self.keep_lra_above_loudness_range_target,
            offset=self.offset,
            lower_only=self.lower_only,
            auto_lower_loudness_target=self.auto_lower_loudness_target,
            dual_mono=self.dual_mono,
            dynamic=self.dynamic,
            keep_original_audio=self.keep_original_audio,
            pre_filter=self.pre_filter,
            post_filter=self.post_filter,
            video_disable=self.video_disable,
            subtitle_disable=self.subtitle_disable,
            metadata_disable=self.metadata_disable,
            chapters_disable=self.chapters_disable
        )
        normalizer.add_media_file(file_path)
        output_path = file_path
        normalization_results = normalizer.run_normalization(output_path)

        table = PrettyTable()
        table.field_names = ["File", "Input Loudness", "Output Loudness", "Input True Peak", "Output True Peak"]
        for result in normalization_results:
            table.add_row([
                result['file'],
                result['input_loudness'],
                result['output_loudness'],
                result['input_true_peak'],
                result['output_true_peak']
            ])

        final_state = {
            'normalized': 'True',
            'output_path': output_path,
            'normalization_results': table.get_string()
        }
        self.processed_files[file_path] = final_state
        self.save_state(file_path, final_state)

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

class Handler(FileSystemEventHandler):
    def __init__(self, grape_jelly):
        self.grape_jelly = grape_jelly

    def on_created(self, event):
        if not event.is_directory and any(event.src_path.endswith(ext) for ext in self.grape_jelly.file_extensions):
            self.grape_jelly.normalize_audio(event.src_path)

if __name__ == "__main__":
    directories_to_watch = os.getenv('DIRECTORIES_TO_WATCH', 'path/to/your/directory').split(',')
    grape_jelly = GrapeJelly(directories_to_watch)
    grape_jelly.run()