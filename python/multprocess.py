from multiprocessing import Process
import multiprocessing
from time import sleep

def f(name):
	sleep(4)
	print 'hello', name
	cpus=multiprocessing.cpu_count() #detect number of cores
	print (cpus)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    print ("process started")
    p.join()
    print ("process completed")