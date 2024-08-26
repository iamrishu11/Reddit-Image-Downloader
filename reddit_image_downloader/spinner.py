import sys
import time
import threading

class Spinner:
    def __init__(self, message='Processing', delay=0.1):
        self.spinner_thread = threading.Thread(target=self._spinner)
        self.spinner_thread.daemon = True
        self.spinner_active = True
        self.delay = delay
        self.message = message

    def _spinner(self):
        spinner_chars = '|/-\\'
        while self.spinner_active:
            for char in spinner_chars:
                sys.stdout.write(f'\r{self.message} {char}')
                sys.stdout.flush()
                time.sleep(self.delay)
        sys.stdout.write('\rDone!                      \n')
        sys.stdout.flush()

    def start(self):
        self.spinner_thread.start()

    def stop(self):
        self.spinner_active = False
        self.spinner_thread.join()
