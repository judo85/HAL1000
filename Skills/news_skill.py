
# --- imports

from random import choice
from pygame import mixer

import requests
import bs4



# --- globals

from Skills.skills_settings import *



# --- functions

def read_news(request, site = 'npr'):

    # Convert the source code to a soup string
    url = NEWS_URL[site]
    response = requests.get(url)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Get the link to the news brief mp3
    casts = soup.findAll('a', {'class': 'audio-module-listen'})
    cast  = casts[0]['href']
    pos   = cast.find("?")

    # Download the mp3 file
    mymp3      = cast[0:pos]
    fname      = choice(range(1000000))
    mymp3_file = requests.get(mymp3)
    with open(f'f{fname}.mp3','wb') as f:
        f.write(mymp3_file.content)

    # Play the mp3 file
    mixer.init()
    mixer.music.load(f'f{fname}.mp3')
    mixer.music.play()


def stop_news():
    try:
        mixer.music.stop()
    except:
        print('no news to stop')


# --- tests

if __name__ == '__main__':
    pass



### --- NOTES
#
#   Use classes
#
#
#
