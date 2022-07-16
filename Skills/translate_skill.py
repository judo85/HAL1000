
# --- imports

from translate import Translator



# --- globals

from Skills.skills_settings import *



# --- functions

def translate(request, language):
    # Extract the phrase
    patterns = ['how to say', 'how do you say', 'translate']
    pid  = None
    for id, patt in enumerate(patterns):
        pos = request.find(patt)
        if pos != -1:
            pid = id
    if not pid:
        return None

    try:
        eng_phrase = request[pos + len(patterns[pid]):]
        translator = Translator(from_lang = "english", to_lang = language)
        translation = translator.translate(eng_phrase)
        ret = f"The {language} for {eng_phrase} is " + translation
        return ret
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
