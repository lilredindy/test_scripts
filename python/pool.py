import threading
from random import randint
from time import sleep
import time
import sys


def print_number(number):
    # Sleeps a random 1 to 10 seconds
    #rand_int_var = randint(1, 10)
    s =time.time()
    t = 3
    sleep(t)
    e =time.time()
    print( "Thread " + str(number) + " slept for " + str(e-s) + " seconds")


thread_list = []

for i in range(1, 11):
    # Instantiates the thread    
    # (i) does not make a sequence, so (i,)
    t = threading.Thread(target=print_number, args=(i,))
    # Sticks the thread in a list so that it remains accessible
    thread_list.append(t)

# Starts threads
for thread in thread_list:
    thread.start()


s = time.time()
time.sleep(5)
e = time.time()
print (e-s) 

# This blocks the calling thread (main thread) until the thread whose join() method is called is terminated.
# From http://docs.python.org/2/library/threading.html#thread-objects
#You could say join is (only) relevant for the execution-flow of the main-thread.
for thread in thread_list:
    thread.join() #seems like this should be called let_finish() or block()


# Demonstrates that the main process waited for threads to complete
print "Done"