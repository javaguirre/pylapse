import os
import ConfigParser

HOME_PATH = os.path.expanduser('~')
CONFIG_PATH = '%s/.pylapse/config.cfg' % HOME_PATH
config = ConfigParser.ConfigParser()

if os.path.exists(CONFIG_PATH):
    config.read(CONFIG_PATH)

DELAY = float(config.get('pylapse', 'DELAY'))
CAPTURES_PATH = config.get('pylapse', 'CAPTURES_PATH')
VIDEOS_PATH = config.get('pylapse', 'VIDEOS_PATH')
IMAGE_EXT = config.get('pylapse', 'IMAGE_EXT')
VIDEO_DEVICE = config.get('pylapse', 'VIDEO_DEVICE')
RESOLUTION = config.get('pylapse', 'RESOLUTION')
