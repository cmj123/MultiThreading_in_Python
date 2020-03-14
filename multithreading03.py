# Import threading
import threading

# User Defined Function
def uf(number):
    """ thread uf function """
    print 'Hello World'
    print 'Thread - ' + str(number)
    return

# Initialise a list for holding threads
threads = []
# Create Five threads that run a simple function
for i in range(5):
    t = threading.Thread(target=uf(i))
    threads.append(t)
    t.start()
