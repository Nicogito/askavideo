from pytube import YouTube
from domain.video import Video
from usecases.ports.audio_downloader import AudioDownloader


class DownloadAudioFromVideo:
    def __init__(self):
        self.audio_downloader = AudioDownloader()

    def execute(self, video: Video, output_path: str) -> None:
        self.audio_downloader.execute(video, output_path)
