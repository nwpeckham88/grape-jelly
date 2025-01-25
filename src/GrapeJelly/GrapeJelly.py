import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from ffmpeg_normalize import FFmpegNormalize

class GrapeJelly:
    def __init__(self, directories):
        self.directories = directories
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
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
        normalizer = FFmpegNormalize(
            audio_codec=os.getenv('AUDIO_CODEC', 'aac'),
            audio_bitrate=os.getenv('AUDIO_BITRATE', '192k'),
            sample_rate=os.getenv('SAMPLE_RATE', '48000'),
            loudness_target=os.getenv('LOUDNESS_TARGET', '-24.0')
        )
        normalizer.add_media_file(file_path)
        output_path = f"{file_path}.normalized.json"
        normalizer.run_normalization(output_path)

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(('.mp4', '.mkv', '.avi')):
            grape_jelly = GrapeJelly([])
            grape_jelly.normalize_audio(event.src_path)

if __name__ == "__main__":
    directories_to_watch = ["path/to/your/directory"]
    grape_jelly = GrapeJelly(directories_to_watch)
    grape_jelly.run()