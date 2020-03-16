"""
Name: Esuabom Dijemeni
Date: 16/03/2020
Purpose: create a program to override the run() function of thread
"""

# Import key libraries
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class SubThread(threading.Thread):

    def run(self):
        logging.debug('Starting')
        logging.debug('Existing')
        return


t = SubThread()
t.start()
