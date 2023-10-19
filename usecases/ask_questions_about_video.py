import select
import subprocess

from domain.video import Video
from usecases.ports.audio_downloader import AudioDownloader
from usecases.ports.qa_engine import QaEngine
from usecases.ports.script_extractor import ScriptExtractor


class AskQuestionsAboutVideo:

    def __init__(self, qa_engine: QaEngine, audio_downloader: AudioDownloader, script_extractor: ScriptExtractor):
        self.audio_downloader = audio_downloader
        self.script_extractor = script_extractor
        self.qa_engine = qa_engine

    def give_video_script_to_qa_engine(self):
        query = "Le texte suivant est un script de vidéo. Je vais te poser différentes " \
                "question concernant cette vidéo et je veux que tu me répondes selon le script donné. " \
                "Le voici:"

        with open("tmp_files/audio.txt", "r") as file:
            video_script = ''.join(file.readlines()).replace("\n", "")

        self.qa_engine.send_message(query + video_script + "\n")
        self.qa_engine.get_response()

    def execute(self, video: Video):
        self.audio_downloader.execute(video)
        script = self.script_extractor.execute(video)
        self.give_video_script_to_qa_engine()

        while True:
            query = input(">> ")

            if query == "exit":
                self.qa_engine.close()
                return
            else:
                self.qa_engine.send_message(query.replace("\n", "") + "\n")
                print(self.qa_engine.get_response())


