import subprocess

from domain.video import Video
from usecases.ports.script_extractor import ScriptExtractor


class WhisperScriptExtractor(ScriptExtractor):
    def __init__(self, model: str, working_directory: str,audio_filename: str):
        self.model = model
        self.working_directory = working_directory
        self.audio_filename = audio_filename

    def execute(self, video: Video):
        subprocess.run("whisper " + self.working_directory+'/'+self.audio_filename + " " +
                       "--fp16 False "
                       "--model " + self.model + " " +
                       "--output_format txt "
                       "--output_dir "+ self.working_directory + " " +
                       " --threads 4 "
                       "--language " + video.language,
                       shell=True, stdout=None)
