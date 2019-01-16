# weather_icon_converter.py
#
# Converts the svg weather images to png.


import os
import argparse
import subprocess

scriptDir = os.path.dirname(os.path.realpath(__file__))


def processFile(dirName, fileName, destDir):
    baseName, fileExtension = fileName.split(".")

    svgFile = fileName
    pngFile = "{}.png".format(baseName)

    svgPath = os.path.join(dirName, fileName)
    pngPath = os.path.join(destDir, pngFile)

    print("Converting {} to {}".format(svgPath, pngPath))

    command = ["C:/Program Files/Inkscape/inkscape", "-z", "-t", "-w", "90", "-h", "90", "-e", pngPath, svgPath]
    #print("Command: {}".format(" ".join(command)))

    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT)

    except subprocess.CalledProcessError as err:
        print("Error converting {}: {}".format(svgFile, err.output.decode('utf-8')))


def processFiles(inDirectory, scriptDir):
    files = os.listdir(inDirectory)
    parentDir, scriptDir = os.path.split(scriptDir)
    weatherIconDir = os.path.join(parentDir, "weather")

    for file in files:
        processFile(inDirectory, file, weatherIconDir)


# ---------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert weather icons from SVG to PNG.')

    parser.add_argument("directory", type=str, help="Directory of SVG files")


    args = parser.parse_args()

    print("Processing icons in: {}".format(args.directory))
    processFiles(args.directory, scriptDir)
