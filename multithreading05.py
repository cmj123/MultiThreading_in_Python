"""
Name: Esuabom Dijemeni
Date: 14/03/2020
Purpose: a program to create 5 threads to print two numbers and sum of 2 numbers
"""

# Import libraries, functions and classes
import threading
import numpy as np

# User defined function
def uf(num1, num2,i):
    """thread uf function"""
    print 'Thread %s' % (i)
    print 'numbers: %s, %s' % (num1, num2)
    print 'result = %d' %(num1 + num2)
    return

# Create 5 threads to print two numbers and sum of 2 numbers
for i in range(5):
    num1 = np.random.randint(0,100)
    num2 = np.random.randint(0,100)
    t = threading.Thread(target=uf, args=(num1, num2, i))
    t.start()
