from fileinput import filename
import sys
import os
import ffmpeg   # pip install ffmpeg-python

def main(args):
    filename = args[1]
    extension = args[2]
    if not os.path.exists(filename + extension):
        print("file not exist")
        return
    stream = ffmpeg.input(filename+extension)
    stream = ffmpeg.output(stream, f"{filename}.wav")
    ffmpeg.run(stream)

if __name__ == "__main__":
    args = sys.argv
    main(args)