
# --- imports

import time
import arrow

from text2digits import text2digits


# --- globals



# --- functions

def run_timer(request):

    # Text to digits converter
    t2d     = text2digits.Text2Digits()
    request = t2d.convert(request)

    # Find the positions of "hour" and "minute"
    pos1 = request.find("timer for")
    pos2 = request.find("hour")
    pos3 = request.find("minute")

    # Handle the case of only hours selected
    if pos3 == -1:
        addhour   = request[pos1 + len("timer for"): pos3]
        addminute = 0
    # Handle the case of only minutes selected
    elif pos2 == -1:
        addhour   = 0
        addminute = request[pos1 + len("timer for"): pos3]
    # General case
    else:
        addhour   = request[pos1 + len("timer for"): pos2]
        addminute = request[pos2 + len("hour"): pos3]

    # Current hour, minute, and second
    startHH = arrow.now().format('H')
    startmm = arrow.now().format('m')
    startss = arrow.now().format('s')

    # Obtain the time for the timer to go off
    newHH = int(startHH) + int(addhour)
    newmm = int(startmm) + int(addminute)
    if newmm > 59:
        newmm -= 60
        newHH += 1
    newHH = newHH % 24
    ###
    print(newHH)
    print(newmm)
    print(startss)
    ###
    end_time = str(newHH) + ":" + str(newmm) + ":" + startss

    ### Test message
    print("Timer will go off at " + end_time)

    # Start timer
    while True:
       timenow = arrow.now().format('H:m:s')
       if timenow == end_time:
           return True
       time.sleep(0.5)


def run_alarm(request):
    
    # Find the positions of the four indicators
    p1 = request.find("alarm for")
    p2 = request.find("a.m.")
    p3 = request.find("p.m.")
    p4 = request.find(":")

    # Handle the four different cases
    if p2 != -1 and p4 != -1:
        request = request[p1 + len("alarm for") + 1: p2] + "AM"
    elif p3 != -1 and p4 != -1:
        request = request[p1 + len("alarm for") + 1: p3] + "PM"
    elif p2 != -1 and p4 == -1:
        request = request[p1 + len("alarm for") + 1: p2 - 1] + ":00 AM"
    elif p3 != -1 and p4 == -1:
        request = request[p1 + len("alarm for") + 1: p3 - 1] + ":00 PM"

    ### Test message
    print("Alarm set for " + request)
    
    # Start alarm
    while True:
        # Obtain time and change it to "h:mm AM" format
        tm = arrow.now().format('h:mm A')
        time.sleep(5)
        # If the clock reaches the preset time, the alarm clock goes off
        if request == tm:
            return True





# --- tests

if __name__ == '__main__':

    from skills_settings import *
    
    request = "set timer for 1 minute"
    res = run_timer(request)
    print(res)



### --- NOTES
#
#   Use classes
#
#
#
