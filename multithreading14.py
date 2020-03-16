"""
Name: Esuabom Dijemeni
Date: 16/03/2020
Purpose: create a program to create 3 daemons threads, and using the enumerate
         and join function function. wait for the daemon threads to complete
         execution.
"""

# Import libraries
import logging
import threading
import time

# Basic Logging Configuration
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName) - 10s) %(message)s',
                    )

# User defined function
def uf():
    logging.debug('Starting')
    time.sleep(10)
    logging.debug('Exiting')

# Create 3 threads
for i in range(3):
    t = threading.Thread(target=uf)
    t.setDaemon(True)
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()
