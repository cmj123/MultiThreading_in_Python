# Import key libraries, classes and functions
import threading

# Function - Simple function to print
def uf():
    """ thread uf function"""
    print "Hello world"
    return


# Create a thread
t = threading.Thread(target=uf) # Target is looking at the function address
# Start the thread 
t.start()
