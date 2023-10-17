from pytube import YouTube
from domain.video import Video


class DownloadAudioFromVideo:
    @staticmethod
    def execute(video: Video, output_path: str)->None:
        yt = YouTube(video.url)
        stream = yt.streams.get_audio_only()
        stream.download(output_path=".", filename=output_path)
        print(f"La vidéo a été téléchargée avec succès sous {output_path}")