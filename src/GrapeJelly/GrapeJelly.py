import os
import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from ffmpeg_normalize import FFmpegNormalize
from prettytable import PrettyTable

class GrapeJelly:
    def __init__(self, directories):
        self.directories = directories
        self.observer = Observer()
        self.audio_codec = os.getenv('AUDIO_CODEC', 'aac')
        self.audio_bitrate = os.getenv('AUDIO_BITRATE', '192k')
        self.sample_rate = os.getenv('SAMPLE_RATE', '48000')
        self.loudness_target = os.getenv('LOUDNESS_TARGET', '-24.0')
        self.true_peak = os.getenv('TRUE_PEAK', '-2.0')
        self.loudness_range_target = os.getenv('LOUDNESS_RANGE_TARGET', '7.0')
        self.video_codec = os.getenv('VIDEO_CODEC', 'libx264')
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
            post_filter="speechnorm=e=6.25:r=0.00001:l=1"
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

class Handler(FileSystemEventHandler):
    def __init__(self, grape_jelly):
        self.grape_jelly = grape_jelly

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(('.mp4', '.mkv', '.avi')):
            self.grape_jelly.normalize_audio(event.src_path)

if __name__ == "__main__":
    directories_to_watch = os.getenv('DIRECTORIES_TO_WATCH', 'path/to/your/directory').split(',')
    grape_jelly = GrapeJelly(directories_to_watch)
    grape_jelly.run()