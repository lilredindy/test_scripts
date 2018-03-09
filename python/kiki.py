import threading
import time 
from time import sleep

import threading
import time

class Kiki(threading.Thread):
    def __init__(self,name, time):
        super(Kiki, self).__init__()
        self.name = name
        self.time = time
        self.start()
        print ("starting..."+self.name+"\n")

    def run(self):
        for i in range(0,self.time):
            time.sleep(1)
            print ("running..."+self.name +"\n")


t1 = Kiki("thread1",1)
t2 = Kiki("thread2",2)
t3 = Kiki("thread3",3)
t1.join()
print "t1.join() finished"
t2.join()
print "t2.join() finished"
t3.join()
print "t3.join() finished"