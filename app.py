import os
import argparse
import subprocess

from capture_image import capture
from time import sleep
from config import *


def create_timelapse(args):
    while True:
        capture(CAPTURES_PATH, **args)
        sleep(DELAY)


def generate_video(videos_path, captures_path, delay=20):
    captures_dir = os.path.join(captures_path, '*.%s' % IMAGE_EXT)
    videos_dir = os.path.join(videos_path, 'outvideo.mpeg')
    command = 'convert -delay %d -loop 0 -scale %s %s %s' % (delay, '50%',
                                                             captures_dir,
                                                             videos_dir)
    subprocess.call(command, shell=True)


def main():
    parser = argparse.ArgumentParser(description='PyLapse - Timelapse image generator')
    parser.add_argument('--src-captures',
                        help='Source directory for the images',
                        default=CAPTURES_PATH)
    subparsers = parser.add_subparsers(help='sub-command help')
    parser_capture = subparsers.add_parser('capture', help='capture help')
    parser_video = subparsers.add_parser('video', help='video help')

    parser_capture.add_argument('--video-device',
                                help='Root of the device',
                                default=VIDEO_DEVICE)
    parser_capture.add_argument('--image-ext',
                                help='Extension for the images captured',
                                default=IMAGE_EXT)
    parser_capture.add_argument('--resolution',
                                help='Resolution of the image capture',
                                default=RESOLUTION)
    parser_video.add_argument('--src-video',
                              help='Source directory for the videos',
                              default=VIDEOS_PATH)
    parser_video.add_argument('--video-delay',
                              help='Delay for the video',
                              default=20)

    arguments = parser.parse_args()

    #FIXME We should be able to know which subparser used the user
    if 'video_device' in arguments:
        args = {'image_ext': arguments.image_ext,
                'resolution': arguments.resolution.split('*'),
                'video_device': arguments.video_device}
        create_timelapse(args)
    else:
        args = {'videos_path': arguments.src_video,
                'captures_path': arguments.src_captures,
                'delay': arguments.video_delay}
        generate_video(**args)


if __name__ == '__main__':
    main()
