"""
Name: Esuabom Dijemeni
Date: 14/03/2020
Purpose: create a program which a logging function to print the thread name and message
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
w = threading.Thread(name='uf', target=uf)

# Start running thread
w.start()
