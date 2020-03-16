# Import key libraries
import threading
import time
import logging

# Basic Logging Configuration
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName) - 10s) %(message)s',
                    )
# User defined function
def uf():
    logging.debug('Starting')
    time.sleep(10)
    logging.debug('Exiting')

# Create thread
t = threading.Thread(name='daemonthread', target=uf)
# Make the thread as a daemon thread
t.setDaemon(True)

t.start()
t.join(2)
print 't.isAlive()', t.isAlive()
print 't.isDaemon', t.isDaemon()
time.sleep(15)
print 't.isAlive()', t.isAlive()
print 't.isDaemon', t.isDaemon()
