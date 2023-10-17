import subprocess


class Whisper:
    @staticmethod
    def execute(model: str, language:str):
        commande = "whisper tmp_files/tmp.mp3 --fp16 False --model " + model + " --output_format txt --output_dir tmp_files --threads 4 --language "+language
        subprocess.run(commande, shell=True, stdout=None)
