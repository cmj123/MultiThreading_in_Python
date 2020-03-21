"""
Name: Esuabom Dijemeni
Date: 22/03/2020
Purpose: Create a program where two consumer threads wait on the producer thread to notify them
"""

# Import key libraries
import threading
import logging

# Logging  message for status tracking
logging.basicConfig( level=logging.DEBUG,
                    format='(%(threadName) -10s) %(message)s'
)

def consumer_thread(cond):
    """wait for the condition and use the resources"""
    logging.debug('Starting consumer_thread thread')
    t = threading.currentThread()
    with cond:
        cond.wait()
        logging.debug('Resources is avaliable to consumer_thread')

def producer_thread(cond):
    """set up the resources """
    logging.debug('Starting producer_thread thread')
    with cond:
        logging.debug('Making resources avaliable')
        cond.notifyAll()


# Initialise threading condition
condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer_thread, args=(condition, ))
c2 =  threading.Thread(name='c2', target=consumer_thread, args=(condition, ))
p = threading.Thread(name='p', target=producer_thread, args=(condition, ))

c1.start()
c2.start()
p.start()
