
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



# --- API

class SpeechRecognizer:
    '''
    '''

    def __init__(self) -> None:
        self.sr = sr.Recognizer()


    def voice_to_text(self) -> str:
        voice_input = "" 
        with sr.Microphone() as source:
            self.sr.adjust_for_ambient_noise(source)
            try:
                audio = self.sr.listen(source)
                voice_input = self.sr.recognize_google(audio)
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass        
            except sr.WaitTimeoutError:
                pass
        return voice_input

  



# --- tests

if __name__ == '__main__':
    pass