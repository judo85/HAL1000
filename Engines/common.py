
# --- imports

### [!] only import for testing; imports delegated to specific classes
#
#   imports needed:
#
#       pyaudio
#       time
#
#
###



# --- shared classes

class Listener:
    '''
    
    '''

    def __init__(self, sample_rate=8000, record_seconds=2):
        self.chunk = 1024
        self.sample_rate = sample_rate
        self.record_seconds = record_seconds
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=self.sample_rate,
                        input=True,
                        output=True,
                        frames_per_buffer=self.chunk)


    def listen(self, queue):
        while True:
            data = self.stream.read(self.chunk , exception_on_overflow=False)
            queue.append(data)
            time.sleep(0.01)


    # def run(self, queue):
    #     thread = threading.Thread(target=self.listen, args=(queue,), daemon=True)
    #     thread.start()
    #     print("\nWake Word Engine is now listening... \n")





# --- tests

if __name__ == '__main__':
    
    import time, pyaudio

    ls = Listener()
    ls.listen()