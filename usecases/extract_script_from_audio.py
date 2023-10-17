import subprocess

from domain.video import Video


class ExtractScriptFromAudio:
    @staticmethod
    def execute(model: str, video: Video):
        subprocess.run("whisper tmp_files/tmp.mp3 "
                       "--fp16 False "
                       "--model " + model +
                       " --output_format txt "
                       "--output_dir tmp_files "
                       "--threads 4 "
                       "--language " + video.language,
                       shell=True, stdout=None)
