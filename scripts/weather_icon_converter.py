
import os
from os import listdir
import subprocess 


def processFile(filePath):
    # print("Number of lines in {}".format(filePath))
    subprocess.call(["wc", "-l", filePath])

def processFiles():
    files = os.listdir()
    print("Files:")
    for file in files:
        # print("  {}".format(file))
        processFile(file)


# ---------------------------------------------------------------
if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-w", "--windowed", action="store_true", default=False, dest="windowed", help="Use windowed mode instead of full-screen")
    # parser.add_argument("--no_backlight", action="store_true", default=False, dest="no_backlight", help="Disable backlight control")


    # args = parser.parse_args()

    processFiles()
