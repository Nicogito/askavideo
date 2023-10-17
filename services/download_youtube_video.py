from pytube import YouTube


class ExtractAudioFromYoutubeVideo:
    @staticmethod
    def execute(url: str, output_path: str)->None:
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        stream.download(output_path=".", filename=output_path)
        print(f"La vidéo a été téléchargée avec succès sous {output_path}")
