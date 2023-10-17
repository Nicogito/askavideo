from pytube import YouTube
from domain.video import Video
from usecases.ports.audio_downloader import AudioDownloader


class YoutubeAudioDownloader(AudioDownloader):
    def execute(self, video: Video, output_path: str):
        yt = YouTube(video.url)
        stream = yt.streams.get_audio_only()
        stream.download(output_path=".", filename=output_path)
        print(f"La vidéo a été téléchargée avec succès sous {output_path}")