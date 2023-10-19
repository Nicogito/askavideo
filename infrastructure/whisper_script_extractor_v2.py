import whisper
from domain.video import Video
from usecases.ports.script_extractor import ScriptExtractor


class WhisperScriptExtractorV2(ScriptExtractor):
    def __init__(self, model: str, working_directory: str, audio_filename: str):
        self.model = model
        self.working_directory = working_directory
        self.audio_filename = audio_filename

    def execute(self, video: Video)-> str:
        model = whisper.load_model("base")
        result = model.transcribe(
            audio="tmp_files/audio.mp3",
            fp16=False,
            model=self.model,
            threads=4,
            language=video.language
        )
        return result["text"]
