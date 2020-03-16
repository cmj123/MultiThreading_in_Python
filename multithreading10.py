"""
Name: Esuabom Dijemeni
Date: 15/03/2020
Purpose: create a daemon threading and check it is done
"""

# Import libraries
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

# User defined function
def uf():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

# Create thread
w = threading.Thread(name='daemonthread', target=uf)
w.setDaemon(True)
# Start running thread
w.start()
w.join()
