"""
Name: Esuabom Dijemeni
Date: 22/03/2020
Purpose: Create a program using semaphores in threads
"""

# Import key libraries
import threading
import logging
import time

# Logging  message for status tracking
logging.basicConfig( level=logging.DEBUG,
                    format='(%(asctime)s) (%(threadName) - 2s) %(message)s',
)

class availPool(object):
    def __init__(self):
        super(availPool, self).__init__
        self.active = []
        self.lock = threading.Lock()
    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running: %s', self.active)
    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)

def thread_function(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        time.sleep(1)
        pool.makeInactive(name)

pool = availPool()
s = threading.Semaphore(2)
for i in range(5):
    t = threading.Thread(target=thread_function, name=str(i), args=(s,pool))
    t.start()
