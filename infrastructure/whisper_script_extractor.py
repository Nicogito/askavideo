import whisper
from domain.video import Video
from usecases.ports.script_extractor import ScriptExtractor


class WhisperScriptExtractor(ScriptExtractor):
    def __init__(self, model: str, working_directory: str, audio_filename: str):
        self.model = model
        self.working_directory = working_directory
        self.audio_filename = audio_filename

    def execute(self, video: Video)-> str:
        model = whisper.load_model(self.model)
        result = model.transcribe(
            audio="tmp_files/audio.mp3",
            fp16=False,
            language=video.language
        )
        return result["text"]
