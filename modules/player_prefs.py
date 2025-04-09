import re

from constants.general import *

width_regex = re.compile(r'r=(\d+)x\d+')
height_regex = re.compile(r'r=\d+x(\d+)')
fullscreen_regex = re.compile(r'f=([y|n])')

lang_regex = re.compile(r'l=(\w+)')

class PlayerPrefs:
    def __init__(self):
        self.height = DEFAULT_HEIGHT
        self.width = DEFAULT_WIDTH
        self.fullscreen = DEFAULT_FULLSCREEN

        self.lang = DEFAULT_LANG

        player_prefs_file = open(PLAYER_PREFS_FILE)
        player_prefs = player_prefs_file.read()

        width_match = width_regex.search(player_prefs)
        height_match = height_regex.search(player_prefs)
        fullscreen_match = fullscreen_regex.search(player_prefs)

        lang_match = lang_regex.search(player_prefs)

        try :
            self.width = int(width_match.group(1))
            self.height = int(height_match.group(1))
        except AttributeError :
            print(f"Width or height don't exists in player prefs file, using defaults instead.")

        try :
            self.fullscreen = fullscreen_match.group(1) == 'y'
        except AttributeError :
            print(f"Fullscreen don't exists in player prefs file, using defaults instead.")

        try :
            self.lang = lang_match.group(1)
        except AttributeError :
            print(f"Lang don't exists in player prefs file, using defaults instead.")