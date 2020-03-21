"""
Name: Esuabom Dijemeni
Date: 18/03/2020
Purpose: Create a program using a with statement to acquire a lock in a thread
"""

# Import key libraries
import threading
import logging
import time

# Logging  message for status tracking
logging.basicConfig( level=logging.DEBUG,
                    format='(%(threadName) -10s) %(message)s'
)

# Function - Create a lock using with statement
def thread_using_with(lock):
    with lock:
        logging.debug('Locked acquired via with')

# Function - Create a lock without using with statement
def thread_not_using_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()

# Initialise a lock
lock = threading.Lock()
w = threading.Thread(target=thread_using_with, args=(lock,))
nw = threading.Thread(target=thread_not_using_with, args=(lock, ))

w.start()
nw.start()
