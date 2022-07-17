
# --- imports

import wolframalpha
import wikipedia



# --- globals

from Skills.skills_settings import *



# --- functions

def wiki_search(request):
    # Look for answer in Wikipedia
    res = wikipedia.summary(request)
    return res[0:200]


def wolfram_search(request):
    # Define API entry point
    wolf = wolframalpha.Client(WOLFRAM_API_KEY)
    # Look for answer in Wolfram Alpha
    res = wolf.query(request)
    return next(res.results).text


def run_search(request):
    ### Test message
    print("Running search...")
    
    try:
        wiki_search(request)
    except:
        return None


# --- tests

if __name__ == '__main__':
    pass



### --- NOTES
#
#   Use classes
#
#
#
