
# --- imports

### General imports
# import threading
import platform

### Import Neural Network Engines
from Engines.wake_word_detector.engine  import WakeEngine
from Engines.speech_recognizer.engine   import SpeechRecognizer

### Use different Synthesizer for Windows or Unix
if platform.system() == "Windows":
    from Engines.speech_synthesizer.engine  import WindowsSpeechSynthesizer as SpeechSynthesizer
elif platform.system() == "Darwin" or platform.system() == "Linux":
    from Engines.speech_synthesizer.engine  import UnixSpeechSynthesizer    as SpeechSynthesizer

### Import Skills
from Skills.music_skill      import play_music, stop_music
from Skills.news_skill       import read_news, stop_news
from Skills.wiki_skill       import run_search
from Skills.stocks_skill     import get_stock_price, get_stock_market
from Skills.email_skill      import send_email
from Skills.timer_skill      import run_timer, run_alarm
from Skills.translate_skill  import translate



# --- globals

from Engines.engines_settings  import *
from Skills.skills_settings    import *



# --- classes

class VoiceAssistant:
    '''
    '''

    def __init__(self) -> None:
        self.wake_engine = WakeEngine()
        self.recognizer  = SpeechRecognizer()
        self.synthesizer = SpeechSynthesizer()


    def run(self):
        '''
        NOTES: 
            - Use threading
            - Delegate skill routing to NLU module
            - News: parse text and delegate reading to synthesizer
            - News: handle request fail
        '''

        while True:

            # Detect wake word
            wake_state = self.wake_engine.run()

            # Handle active requests
            while wake_state == WAKE_STATES['active']:

                ### TEST
                test_msg = SYNTHESIZER_MSG['test_active']
                self.synthesizer.print_say(test_msg)

                # Capture user input
                input_msg = SYNTHESIZER_IO['input']
                self.synthesizer.print_say(input_msg)
                ans = self.recognizer.voice_to_text().lower()
                self.synthesizer.print_say(ans) # change to print in final

                # Requests switches
                standby_req = ("back"     in ans and "stand" in ans)
                music_req   = ("music by" in ans or  "play"  in ans)
                email_req   = ("send"     in ans and "email" in ans)
                news_req    = ("news"     in ans)
                stock_req   = ("stock"    in ans)
                timer_req   = (
                    "timer for" in ans and                 \
                        ("hour" in ans or "minute" in ans) \
                    or "alarm for" in ans and              \
                        ("a.m." in ans or "p.m." in ans)
                )
                transl_req  = (
                    (
                        "how to say"     in ans or \
                        "how do you say" in ans or \
                        "translate"      in ans
                    ) and " in " in ans
                )
                
                # Handle standby request
                if standby_req:
                    standby_msg = SYNTHESIZER_IO['standby']
                    self.synthesizer.print_say(standby_msg)
                    break

                # Handle specific skill requests routing
                elif music_req:
                    found = play_music(ans)
                    if not found:
                        not_found_msg = SYNTHESIZER_MSG['not_found']
                        self.synthesizer.print_say(not_found_msg)
                    # Say 'stop' to stop the music at any time
                    while True:
                        background = self.recognizer.voice_to_text().lower()
                        if "stop" in background:
                            stop_music()
                            break
                        else:
                            continue

                elif news_req:
                    # res = read_news()
                    # self.synthesizer.print_say(res)
                    read_news()
                    # Say 'stop' to stop the news at any time
                    while True:
                        background = self.recognizer.voice_to_text().lower()
                        if "stop" in background:
                            stop_news()
                            break
                        else:
                            continue
                
                elif stock_req:
                    # Route request
                    if "stock price" in ans:
                        res = get_stock_price(ans)
                    elif "stock market" in ans:
                        res = get_stock_market(ans)
                    # Report result
                    if res:
                        self.synthesizer.print_say(res)
                    else:
                        not_found_msg = SYNTHESIZER_MSG['not_found']
                        self.synthesizer.print_say(not_found_msg)
                    continue

                elif timer_req:
                    start_msg = SYNTHESIZER_MSG['timer_start']
                    self.synthesizer.print_say(start_msg)
                    # Run based on request
                    if "timer" in ans:
                        res = run_timer(ans)
                    elif "alarm" in ans:
                        res = run_alarm(ans)
                    # Notify at end
                    if res:
                        end_msg = SYNTHESIZER_MSG['timer_end']
                        self.synthesizer.print_say(end_msg)
                    else:
                        debug_msg = SYNTHESIZER_MSG['debug']
                        self.synthesizer.print_say(debug_msg)
                    continue

                elif transl_req:
                    # Determine language
                    pos = ans.rfind(' in ')
                    lng = ans[pos + 4:]
                    msg = ans[:pos]
                    res = translate(request = msg, language = lng)
                    if res:
                        self.synthesizer.print_say(input = res, language = lng)
                    else:
                        not_found_msg = SYNTHESIZER_MSG['not_found']
                        self.synthesizer.print_say(not_found_msg)
                    continue
                
                elif email_req:
                    addr_msg = SYNTHESIZER_MSG['email_address']
                    body_msg = SYNTHESIZER_MSG['email_body']
                    subj_msg = SYNTHESIZER_MSG['email_subject']

                    self.synthesizer.print_say(addr_msg)
                    address = self.recognizer.voice_to_text().lower()

                    self.synthesizer.print_say(body_msg)
                    body = self.recognizer.voice_to_text().lower()

                    self.synthesizer.print_say(subj_msg)
                    subject = self.recognizer.voice_to_text().lower()

                    res = send_email(
                        address = address,
                        body    = body,
                        subject = subject
                    )
                    if res:
                        self.synthesizer.print_say(res)
                    else:
                        fail_msg = SYNTHESIZER_MSG['fail']
                        self.synthesizer.print_say(fail_msg)
                    continue

                else: # try wiki request
                    res = run_search(ans)
                    if res is None:
                        # Request fail, go back in standby
                        fail_msg = SYNTHESIZER_MSG['fail']
                        self.synthesizer.print_say(fail_msg)
                        break
                    else:
                        self.synthesizer.print_say(res)
                    continue

            # Handle exit request
            if wake_state == WAKE_STATES['quit']:
                exit_msg = SYNTHESIZER_IO['quit']
                self.synthesizer.print_say(exit_msg)
                break



# --- main

if __name__ == '__main__':

    va = VoiceAssistant()
    va.run()