"""import threading
import time

def loop1_10():
    for i in range(1, 11):
        time.sleep(1)
        print(i)
#loop1_10()
threading.Thread(target=loop1_10).start()"""

"""import threading
import time


class MyThread(threading.Thread):
    def run(self):                                         # Default called function with mythread.start()
        print("{} started!".format(self.getName()))        # "Thread-x started!"
        time.sleep(1)                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))       # "Thread-x finished!"

def main():
    for x in range(4):                                     # Four times...
        mythread = MyThread(name = "Thread-{}".format(x))  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread, run method will be invoked
        time.sleep(.9)                                     # ...Wait 0.9 seconds before starting another

if __name__ == '__main__':
    main()"""
#Multi thread

"""class Hello:
    def run(s):
        for i in range(5):
            print("live")
class hi:
    def run(s):
        for i in range(5):
            print("wire")
t1=Hello()
t1.run()
t2=hi()
t2.run()"""
"""from time import*
from threading import*
class hello(Thread):
    def run(s):
        for i in range(5):
            print("Livewire")
            sleep(1)
class hi(Thread):
    def run(s):
        for i in range(5):
            print("gh")
            sleep(1)
t1=hello()
t2=hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()

"""
"""import threading

class thread(threading.Thread):
	def __init__(self, thread_name, thread_ID):
		threading.Thread.__init__(self)
		self.thread_name = thread_name
		self.thread_ID = thread_ID

		# helper function to execute the threads
	def run(self):
		print(str(self.thread_name) +" "+ str(self.thread_ID));

thread1 = thread("GFG", 1000)
thread2 = thread("Livewire", 2000);

thread1.start()
thread2.start()
print()
print("Exit")"""

"""from threading import*
class bus:
    def buy(s):
        print("Hello")
ob=bus()
t1=Thread(target=ob.buy())
t2=Thread(target=ob.buy())
t1.start()
t2.start()"""

"""from threading import*
class bus:
    def __init__(s,avs):
        s.avs=avs
    def buy(s,sr):
        print("Total",s.avs)
        if(s.avs>=sr):
            print("confirm seat")
            s.avs-=sr
        else:
            print("no seats")
            s.release()
obj=bus(5)
t1=Thread(target=obj.buy,args=(10,))
#t2=Thread(target=obj.buy,args=(4,))
#t3=Thread(target=obj.buy,args=(5,))
t1.start()
#t2.start()
#t3.start()"""
"""from threading import*
class bus:
    def __init__(s,avs):
        s .l=lock()
        s.l.acquire()"""
"""import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()"""


"""import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()"""

"""import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker= 'p')
plt.show()
"""
"""import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()"""

"""import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()"""



import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()










