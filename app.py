import os
import argparse
import subprocess

from capture_image import capture
from time import sleep
from config import *


def create_timelapse():
    while True:
        capture(CAPTURES_PATH)
        sleep(DELAY)


def generate_video(videos_path, captures_path):
    command = 'convert -delay 20 -loop 0 -scale %s %s %s' % ('50%',
                                                                   os.path.join(captures_path, '*.jpg'),
                                                                   os.path.join(videos_path, 'outvideo.mpeg'))
    subprocess.call(command, shell=True)


def main():
    parser = argparse.ArgumentParser(description='PyLapse - Timelapse image generator')

    parser.add_argument('--capture', action='store_true',
                        help='Starts the timelapse')
    parser.add_argument('--video', action='store_true',
                        help='Generates the video')

    arguments = parser.parse_args()

    if arguments.capture:
        create_timelapse()
    elif arguments.video:
        generate_video(VIDEOS_PATH, CAPTURES_PATH)


if __name__ == '__main__':
    main()
