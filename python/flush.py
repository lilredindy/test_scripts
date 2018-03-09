import time
import sys


import sys

for i in range(10):
    print i
    if i == 5:
        print "Flushing buffer"
        sys.stdout.flush()
   # time.sleep(1)

for i in range(10):
    print i,
    if i == 5:
    	pass
        #print "Flushing buffer"
       # sys.stdout.flush()


import sys
for x in range(10000):
    print "HAPPY >> %s <<\r" % str(x),
#    sys.stdout.flush()

