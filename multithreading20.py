"""
Name: Esuabom Dijemeni
Date: 17/03/2020
Purpose: Create a program where in the main thread tries to acquire the lock twice in a sequential fashion
"""

# Import key libraries
import threading


### Case 01
lock = threading.Lock()

print 'First try: ', lock.acquire()
print 'Second try: ', lock.acquire(0)

### Case 02
lock2 = threading.RLock()

print 'First try: ', lock2.acquire()
print 'Second try: ', lock2.acquire(0)
