from pathlib import Path

class Site():
    def __init__(self, source, dest):
        self.source = self.source.Path()
        self.dest = self.dest.Path()

    def create_dir(self, path):
        directory = f"{self.dest}/{path.relative_to(self.source)}"
        os.mkdir(directory, parents=True, exist_ok=True)

    def build(self):
        os.mkdir(self.dest, parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if os.path.isdir(path):
                create_dir(path)
