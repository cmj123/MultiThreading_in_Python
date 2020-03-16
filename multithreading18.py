"""
Name: Esuabom Dijemeni
Date: 16/03/2020
Purpose: create a program where in a thread waits for a particular event for a particular time
"""

# Import key libraries
import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

# Function - to wait for an event
def function_waiting_for_event(e, t):
    """wait for the event to be set before doing anything"""
    logging.debug('function waiting for event starting')
    event_is_set = e.wait(t)
    if event_is_set:
        logging.debug('event set: %s', event_is_set)
    else:
        logging.debug('doing other work')

# Create an event thread
e = threading.Event()
# Create a thread
t1 = threading.Thread(name='userfunctionawaitingforevent',
                      target=function_waiting_for_event, args=(e, 2))
t1.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(5)
e.set()
logging.debug('Event is set')
