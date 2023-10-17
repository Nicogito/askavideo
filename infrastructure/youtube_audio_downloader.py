from pytube import YouTube
from domain.video import Video
from usecases.ports.audio_downloader import AudioDownloader


class YoutubeAudioDownloader(AudioDownloader):
    def __init__(self, working_directory: str, audio_filename: str):
        self.working_directory = working_directory
        self.audio_filename = audio_filename

    def execute(self, video: Video):
        yt = YouTube(video.url)
        stream = yt.streams.get_audio_only()
        stream.download(output_path=self.working_directory, filename=self.audio_filename)
        print(f"La vidéo a été téléchargée avec succès")