import argparse

from domain.video import Video
import os

from usecases.ask_questions_about_video import AskQuestionsAboutVideo
from usecases.download_audio_from_video import DownloadAudioFromVideo
from usecases.extract_script_from_audio import ExtractScriptFromAudio


def main():
    youtube_url, whisper_model, language = check_args()

    video = Video(youtube_url, language)

    print("STEP 1 - DOWNLOAD AUDIO")
    DownloadAudioFromVideo.execute(video, 'tmp_files/tmp.mp3')
    print("STEP 2 - SCRIPT EXTRACTION")
    ExtractScriptFromAudio.execute(whisper_model, video)
    os.system('clear')
    llm = AskQuestionsAboutVideo()
    llm.finetune_with_video_script()
    print("Hey welcome ! Ask me some questions about your video")
    llm.interact()


def check_args()->(str, str):
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
