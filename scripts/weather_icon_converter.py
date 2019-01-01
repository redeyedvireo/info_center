# weather_icon_converter.py
#
# Converts the svg weather images to png.


import os
import argparse
import subprocess


def processFile(dirName, fileName):
    baseName, fileExtension = fileName.split(".")

    svgFile = fileName
    pngFile = "{}.png".format(baseName)

    svgPath = os.path.join(dirName, fileName)
    pngPath = os.path.join(dirName, pngFile)

    print("Converting {} to {}".format(svgPath, pngPath))

    try:
        subprocess.check_output(["C:/Program Files/Inkscape/inkscape", "-z", "-e", pngPath, "-w" "200", "-h", "200", svgPath])

    except subprocess.CalledProcessError as err:
        print("Error converting {}: {}".format(svgFile, err.output))


def processFiles(inDirectory):
    files = os.listdir(inDirectory)
    print("Files:")
    for file in files:
        processFile(inDirectory, file)


# ---------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert weather icons from SVG to PNG.')

    parser.add_argument("directory", type=str, help="Directory of SVG files")


    args = parser.parse_args()

    print("Processing icons in: {}".format(args.directory))
    processFiles(args.directory)
