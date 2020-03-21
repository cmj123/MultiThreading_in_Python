"""
Name: Esuabom Dijemeni
Date: 22/03/2020
Purpose: Create a program using semaphores in threads
"""

# Import key libraries
import threading
import logging
from numpy import random

# Logging  message for status tracking
logging.basicConfig( level=logging.DEBUG,
                    format='(%(asctime)s) (%(threadName) - 2s) %(message)s',
)


# Function - To display a thread's value
def display_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)

# Function - a function to run on thread
def thread_function(data):
    display_value(data)
    data.value = random.randint(1, 100)
    display_value(data)

# Get a thread's local data
local_data = threading.local()

# Create mulitple threads with different version
for i in range(2):
    t = threading.Thread(target=thread_function, args=(local_data, ))
    t.start()
