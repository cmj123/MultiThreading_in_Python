"""
Name: Esuabom Dijemeni
Date: 16/03/2020
Purpose: create a daemon threading and using the enumerate and join function ,
         wait for the daemon thread a daemon.
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

# Create thread
t = threading.Thread(name='daemonthread', target=uf)
# Make the thread as a daemon thread
t.setDaemon(True)
# Start the thread
t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()
