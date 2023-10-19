import argparse

from domain.video import Video

from infrastructure.llama_qa_engine import LlamaQaEngine
from infrastructure.whisper_script_extractor import WhisperScriptExtractor
from infrastructure.youtube_audio_downloader import YoutubeAudioDownloader
from usecases.ask_questions_about_video import AskQuestionsAboutVideo

WORKING_DIR = "tmp_files"
AUDIO_FILENAME = "audio.mp3"


def main():
    youtube_url, whisper_model, language = check_args()

    video = Video(youtube_url, language)
    audio_downloader = YoutubeAudioDownloader(WORKING_DIR, AUDIO_FILENAME)
    script_extractor = WhisperScriptExtractor(whisper_model, WORKING_DIR, AUDIO_FILENAME)
    qa_engine = LlamaQaEngine()
    ask_questions_about_video = AskQuestionsAboutVideo(qa_engine, audio_downloader, script_extractor)

    ask_questions_about_video.execute(video)


def check_args() -> (str, str):
    parser = argparse.ArgumentParser(description="AskAVideo - Sytème de Q/A sur des vidéos")
    parser.add_argument("--youtube-url", required=True, help="URL de la vidéo YouTube à télécharger")
    parser.add_argument("--language", required=True, choices=["English", "French"],
                        help="Langue de la vidéo")
    parser.add_argument("--whisper-model", choices=["tiny", "small", "medium", "large"], default="tiny",
                        help="Modèle Whisper à utiliser (par défaut: tiny)")

    args = parser.parse_args()
    return args.youtube_url, args.whisper_model, args.language


if __name__ == '__main__':
    main()
