import select
import subprocess


class Llama:
    def __init__(self):
        self.llama = subprocess.Popen(["ollama", "run", "llama2"],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True,
                         bufsize=0
                         )

    def finetune_with_video_script(self):
        query = "Le texte suivant est un script de vidéo. Je vais te poser différentes " \
                "question concernant cette vidéo et je veux que tu me répondes selon le script donné. " \
                "Le voici:"

        with open("tmp_files/tmp.txt", "r") as file:
            video_script = ''.join(file.readlines()).replace("\n","")
        self.llama.stdin.write(query+ video_script + "\n")
        self.mute_response()

    def interact(self):
        while True:
            query = input(">> ")

            if query == "exit":
                self.close()
                return
            else:
                self.llama.stdin.write(query.replace("\n","")+"\n")
                self.get_response()

    def close(self):
        self.llama.stdin.close()

    def get_response(self):
        self.llama.stdout.readline()
        self.llama.stdout.readline()
        ready, _, _ = select.select([self.llama.stdout], [], [], 3)
        line = ""
        while ready and line is not None:
            line = self.llama.stdout.readline()
            print(line, end='')  # or do something with the line
            ready, _, _ = select.select([self.llama.stdout], [], [], 3)

    def mute_response(self):
        self.llama.stdout.readline()
        self.llama.stdout.readline()
        ready, _, _ = select.select([self.llama.stdout], [], [], 3)
        line = ""
        while ready and line is not None:
            line = self.llama.stdout.readline()
            ready, _, _ = select.select([self.llama.stdout], [], [], 3)



