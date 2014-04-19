import os
import ConfigParser

CONFIG_PATH = os.path.expanduser('~/.pylapse/config.cfg')
config = ConfigParser.ConfigParser()

if os.path.exists(CONFIG_PATH):
    config.read(CONFIG_PATH)

DELAY = float(config.get('pylapse', 'DELAY'))
CAPTURES_PATH = config.get('pylapse', 'CAPTURES_PATH')

if CAPTURES_PATH.startswith('~'):
    CAPTURES_PATH = os.path.expanduser(CAPTURES_PATH)

VIDEOS_PATH = config.get('pylapse', 'VIDEOS_PATH')

if VIDEOS_PATH.startswith('~'):
    VIDEOS_PATH = os.path.expanduser(VIDEOS_PATH)

IMAGE_EXT = config.get('pylapse', 'IMAGE_EXT')
VIDEO_DEVICE = config.get('pylapse', 'VIDEO_DEVICE')
RESOLUTION = config.get('pylapse', 'RESOLUTION')
