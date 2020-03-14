"""
Name: Esuabom Dijemeni
Date: 14/03/2020
Purpose: create a program that adds 2 numbers and prints the result on a thread
"""

# Import libraries, functions and classes
import threading
import numpy as np

# User defined function
def uf(num1, num2):
    """thread uf function"""
    print 'numbers: %s, %s' % (num1, num2)
    print 'result = %d' %(num1 + num2)
    return

# Create a thread to print two numbers and sum of 2 numbers
num1 = np.random.randint(0,10)
num2 = np.random.randint(0,10)
t = threading.Thread(target=uf, args=(num1, num2))
t.start()
