
# --- wake word detector globals

WAKE_STATES = {
    "inactive": "inactive",
    "active":   "active",
    "quit":     "quit"
}

WAKE_PHRASES = {
    "activate":   ["Hey, Hal!", "Hey, Hal", "Hey Hal", "Hal"],
    "deactivate": ["quit", "stop", "exit"]
}



# --- speech recognizer engine globals

###



# --- speech synthesizer engine globals

SYNTHESIZER_IO = {
    "input":   "Hello, how may I help you?",
    "standby": "Ok, going back in standby. Let me know if you need anything.",
    "quit":    "Quitting, goodbye!"
}

SYNTHESIZER_MSG = {
    # general
    'not_found': 'I could not find that, sorry!',
    'fail':      "I'm sorry, I couldn't understand your request. Going back in standby.",
    'repeat':    "Could you repeat that, please?",
    'debug':     "Something has gone wrong, please check.",

    # email
    'email_address': 'To what address should I send it?',
    'email_body':    'Please dictate the email text.',
    'email_subject': 'Should I put something as object field?',

    # timer
    'timer_start': "I'll start the timer now.",
    'timer_end':   "Your timer has gone off!",

    # TEST
    'test_active': "Hey there!"
}

LANG_ABBREVIATION = {
    "english":     "en",
    "chinese":     "zh",
    "spanish":     "es",
    "french":      "fr",
    "japanese":    "ja",
    "portuguese":  "pt",
    "russian":     "ru",
    "korean":      "ko",
    "german":      "de",
    "italian":     "it"
}



# --- nlu engine globals

###



# --- other globals

###