"""
Name: Esuabom Dijemeni
Date: 14/03/2020
Purpose: create a program which creates multiple threads, names them and prints the name
"""

# Import libraries
import threading
import time

# User defined function 1
def ug():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'

# User defined function 2
def servicefunction():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'

t = threading.Thread(name='servicefunction', target=servicefunction)
w = threading.Thread(name='ug', target=ug)
w2 = threading.Thread(target=ug)

w.start()
w2.start()
t.start()
