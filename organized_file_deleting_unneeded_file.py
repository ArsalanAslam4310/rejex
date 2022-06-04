import os
from pathlib import PosixPath, Path


def unneeded_files(directory: PosixPath):
    for folder, _, files in os.walk(directory):
        for file in files:
            filePath = os.path.join(folder, file)
            if os.path.getsize(filePath) > 131072:
                print('File Name: '+file+"      File Path: "+filePath)


if __name__ == "__main__":
    unneeded_files(Path('/home/arslan/Documents/programs'))
