import argparse

from services.ask_about_video_through_llama import Llama
from services.download_youtube_video import ExtractAudioFromYoutubeVideo
from services.extract_script_from_audio import Whisper
import os


def main():
    youtube_url, whisper_model, language = check_args()
    print("STEP 1 - DOWNLOAD AUDIO")
    ExtractAudioFromYoutubeVideo.execute(youtube_url, 'tmp_files/tmp.mp3')
    print("STEP 2 - SCRIPT EXTRACTION")
    Whisper.execute(whisper_model, language)
    os.system('clear')
    llm = Llama()
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
