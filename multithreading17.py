"""
Name: Esuabom Dijemeni
Date: 16/03/2020
Purpose: create a program where  in a thread waits for a particular event indefinitely
"""

# Import key libraries
import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

# Function - to wait for an event
def function_waiting_for_event(e):
    """wait for the event to be set before doing anything"""
    logging.debug('function waiting for event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)

# Create an event thread
e = threading.Event()
# Create a thread
t1 = threading.Thread(name='userfunctionawaitingforevent',
                      target=function_waiting_for_event, args=(e, ))
t1.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(3)
e.set()
logging.debug('Event is set')
