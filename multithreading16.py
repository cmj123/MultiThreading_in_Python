"""
Name: Esuabom Dijemeni
Date: 16/03/2020
Purpose: create a program to override the constructor and  run() function of thread
"""

# Import key libraries
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class SubThreadWithArgs(threading.Thread):
    # override the constructor
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)
        self.args = args
        self.kwargs = kwargs
        return

    # Override the run function 
    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs)
        return

t = SubThreadWithArgs(args=(1,), kwargs={'a':'A','b':'B'})
t.start()
