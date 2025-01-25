import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from ffmpeg_normalize import FFmpegNormalize

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