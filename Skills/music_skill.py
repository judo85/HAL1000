
# --- imports

import os
import random
from pygame import mixer



# --- globals

from Skills.skills_settings import *



# --- functions

def play_music(request):

    # Clean request
    pos = request.find("play ")
    request = request[pos + len("play "):]

    # separate song and artist name
    names  = request.split("by ")
    song   = names[0]
    artist = names[1]

    # Find song(s)    
    with os.scandir(MUSIC_FOLDER) as files:
        mysongs = [
        file.name for file in files if  \
        song   in file.name.lower() or  \
        artist in file.name.lower() and \
        "mp3"  in file.name
    ]

    # Return False if none found
    if len(mysongs) == 0:
        return False
    else:
        # Randomly select one from the list and play
        mysong = random.choice(mysongs)
        mixer.init()
        mixer.music.load(MUSIC_FOLDER + f'/{mysong}')
        mixer.music.play()
        return mysong


def stop_music():
    try:
        mixer.music.stop()
    except:
        print('no music to stop')



# --- tests

if __name__ == '__main__':
    pass



### --- NOTES
#
#   Use classes
#
#
#
