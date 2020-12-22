import pyminizip
import pathlib
import os
import string
import secrets
import time
import tempfile

class ZipUtility():
    targetFiles = []
    zipLayout = []

    def __init__(self):
        pass

    def AddFile(self, f: str, base: str = os.sep)->None:
        if not pathlib.Path(f).exists():
            print('"{}" does NOT exist. Skip process.....'.format(f))
        else:
            self.targetFiles.append(f)
            self.zipLayout.append(base)

    def AddFiles(self, files: list, bases: list = None)->None:
        if bases is None or len(files) != len(bases):
            bases = [os.sep for i in range(len(files))]

        for f, b in zip(files, bases):
            self.AddFile(f, b)
        
    def AddFolder(self, folder: str)->None:
        path = pathlib.Path(folder)
        if not path.exists():
            print('"{}" does NOT exist. Skip process.....'.format(folder))
            return

        elif path.is_file():
            print('"{}" is not folder but file. Process as file'.format(folder))
            self.AddFile(str(path))
            return

        elif path.is_dir():
            files = [str(item) for item in pathlib.Path(folder).glob("**/*") if item.is_file()]

            if len(files) == 0:
                print('"{}" has no files. Skip process.....'.format(folder))
                return
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
            print('"{}" is exist as folder. "Archive.zip" is generated in there'.format(archive, archive))
            path = path / "Archive.zip"

        if override or not path.exists():
            pathlib.Path(temp).replace(path)
        else:
            print('"{}" is already exists. Use --override option to override it.'.format(archive))
        