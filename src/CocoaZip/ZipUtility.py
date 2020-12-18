import pyminizip
import pathlib
from .ErrorMessageManager import ErrorMessageManager
import os
import string
import secrets
import time
import tempfile

class ZipUtility():
    targetFiles = []
    zipLayout = []
    errorMessage = ErrorMessageManager()

    def __init__(self):
        self.errorMessage.RefreshMessage("ja")

    def AddFile(self, f: str, base: str = os.sep)->None:
        if not pathlib.Path(f).exists():
            self.errorMessage.AppendMessage(1001, filename = f).Assert()
        else:
            self.targetFiles.append(f)
            self.zipLayout.append(base)

    def AddFiles(self, files: list, bases: list = None)->None:
        if bases is None:
            bases = [os.sep for i in range(len(files))]

        for f, b in zip(files, bases):
            self.AddFile(f, b)
        
    def AddFolder(self, folder: str)->None:
        path = pathlib.Path(folder)
        if not path.exists():
            self.errorMessage.AppendMessage(1002, folder = folder).Assert()
            return

        elif path.is_file():
            self.errorMessage.AppendMessage(1003, folder = folder).Assert()
            self.AddFile(str(path))
            return

        elif path.is_dir():
            files = [str(item) for item in pathlib.Path(folder).glob("**/*") if item.is_file()]
            bases = [os.path.dirname(item)[folder.rfind(os.sep) + 1:] + os.sep for item in files]
            self.AddFiles(files, bases)

    def PasswordGeneration(self, size: int = 12, salt: str = '')->str:
        return salt + ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(size))

    def Compress(self, archive: str = "Archive.zip", password:str = None, override = False)->None:
        temp = os.path.join(tempfile.gettempdir(), "Archive.zip")
        pyminizip.compress_multiple(self.targetFiles, self.zipLayout, temp, password, 0)

        path = pathlib.Path(archive).resolve()
        print(path)
        if path.is_dir():
            self.errorMessage.AppendMessage(1004, archive = archive).Assert()
            path = path / "Archive.zip"

        if override or not path.exists():
            pathlib.Path(temp).replace(path)
        else:
            self.errorMessage.AppendMessage(1005, archive = archive).Assert()
        