
# --- imports

# import pyaudio
# import threading
# import time
# import argparse
# import wave
import pyttsx3
import os

from Engines.engines_settings import LANG_ABBREVIATION



# --- API

class SpeechSynthesizer:
    '''
    Abstract Base Class (for now, just a placeholder)
    '''

    def __init__(self) -> None:
        pass
    

    def say(self, input):
        pass


    def print_say(self, input):
        pass


class WindowsSpeechSynthesizer(SpeechSynthesizer):
    '''
    Specific instance working on a Windows-based OS
    '''

    def __init__(self) -> None:
        self.synthesizer = pyttsx3.init()

    
    ### Add getters and setters
    #
    #    voices = self.synthesizer.getProperty('voices')
    #    self.synthesizer.setProperty('voice', voices[1].id)
    #    self.synthesizer.setProperty('rate', 150)
    #    self.synthesizer.setProperty('volume', 1.2)
    #
    

    def say(self, input):
        self.synthesizer.say(input)
        self.synthesizer.runAndWait()


    def print_say(self, input, language = 'english'):
        ### Language not supported yet!
        print(input)
        self.synthesizer.say(input)
        self.synthesizer.runAndWait()


class UnixSpeechSynthesizer(SpeechSynthesizer):
    '''
    Specific instance working on a Unix-based OS
    '''

    def __init__(self) -> None:
        super().__init__()
    

    def say(self, input):
        pass


    def print_say(self, input, language = 'english'):
        print(input)
        input = input.replace('"','')
        lang = LANG_ABBREVIATION[language]
        os.system(f'gtts-cli --nocheck "{input}" --lang {lang} | mpg123 -q -')





# --- tests

if __name__ == '__main__':
    pass