
### --- Patch to get rid of ALSA lib error messages in Linux

import platform

if  platform.system() == "Linux":
    from ctypes import CFUNCTYPE, c_char_p, c_int, cdll
    
    # Define error handler
    error_handler = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
    # Don't do anything if there is an error message
    def py_error_handler(filename, line, function, err, fmt):
      pass
    # Pass to C
    c_error_handler = error_handler(py_error_handler)
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)

### ---------------------------------------------------------



# --- imports

# import pyaudio
# import threading
# import time
# import argparse
# import wave

# from common import Listener

import speech_recognition as sr

from Engines.engines_settings import *



# --- API

class WakeEngine:
    '''
    '''

    def __init__(self) -> None:
        self.sr = sr.Recognizer()


    # def predict(self):
    #     pass


    def run(self) -> str:
        wake_state = WAKE_STATES['inactive']
        voice_input = "" 
        with sr.Microphone() as source:
            self.sr.adjust_for_ambient_noise(source)
            try:        
                audio = self.sr.listen(source,timeout=3)
                voice_input = self.sr.recognize_google(audio).lower()
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
            except sr.WaitTimeoutError:
                pass
        if any(s.lower() in voice_input for s in WAKE_PHRASES['activate']):
            wake_state = WAKE_STATES['active'] 
        elif any(s.lower() in voice_input for s in WAKE_PHRASES['deactivate']):
            wake_state = WAKE_STATES['quit']
        return wake_state



# --- tests

if __name__ == '__main__':
    pass