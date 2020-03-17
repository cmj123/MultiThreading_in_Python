"""
Name: Esuabom Dijemeni
Date: 17/03/2020
Purpose: create a program 2 threads which acquire the lock, increment the counter value and release the lock.
"""

# Import key libraries
import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

# Create a counter class
class Counter(object):
    # Initialise the class
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    # Create a method to increment value
    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()

# Define a user function
def userfunction(c):
    logging.debug('Starting')
    time.sleep(3)
    c.increment()
    logging.debug('Exiting')

counter = Counter()
for i in range(2):
    t = threading.Thread(target=userfunction, args=(counter, ))
    t.start()

logging.debug('Waiting for userfunction threads')
main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)
