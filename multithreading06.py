"""
Name: Esuabom Dijemeni
Date: 14/03/2020
Purpose: create a program to print the default thread while the thread is under execution
"""

# Import libraries
import threading
import time

# user defined functions
def ug():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'

# Initialise the thread
w = threading.Thread(target=ug) # use default time

# Start the thread
w.start()
