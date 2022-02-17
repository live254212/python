"""import threading
import time
 
class BankAccount():
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
 
  def __str__(self):
    return self.name
 
# These accounts are our shared resources
account1 = BankAccount("account1", 100)
account2 = BankAccount("account2", 0)

class BankTransferThread(threading.Thread):
  def __init__(self, sender, receiver, amount):
    threading.Thread.__init__(self)
    self.sender = sender
    self.receiver = receiver
    self.amount = amount
   
  def run(self):
    sender_initial_balance = self.sender.balance
    sender_initial_balance -= self.amount
    # Inserting delay to allow switch between threads
    time.sleep(1)
    self.sender.balance = sender_initial_balance
     
    receiver_initial_balance = self.receiver.balance
    receiver_initial_balance += self.amount
    # Inserting delay to allow switch between threads
    time.sleep(0.001)
    self.receiver.balance = receiver_initial_balance
 
if __name__ == "__main__":
   
  threads = []
 
  for i in range(100):
    threads.append(BankTransferThread(account1, account2, 1))
 
  for thread in threads:
    thread.start()
 
  for thread in threads:
    thread.join()
 
  print(account1.balance)


"""





"""import threading
import time
 
class BankAccount():
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
 
  def __str__(self):
    return self.name
 
# These accounts are our shared resources
account1 = BankAccount("account1", 100)
account2 = BankAccount("account2", 0)
 
# Creating lock for threads
lock = threading.Lock()
 
class BankTransferThread(threading.Thread):
  def __init__(self, sender, receiver, amount):
    threading.Thread.__init__(self)
    self.sender = sender
    self.receiver = receiver
    self.amount = amount
   
  def run(self):
    lock.acquire()
     
    sender_initial_balance = self.sender.balance
    sender_initial_balance -= self.amount
    # Inserting delay to allow switch between threads
    time.sleep(0.1)
    self.sender.balance = sender_initial_balance
     
    receiver_initial_balance = self.receiver.balance
    receiver_initial_balance += self.amount
    # Inserting delay to allow switch between threads
    time.sleep(0.001)
    self.receiver.balance = receiver_initial_balance
     
    lock.release()
     
 
if __name__ == "__main__":
   
  threads = []
 
  for i in range(100):
    threads.append(BankTransferThread(account1, account2, 1))
 
  for thread in threads:
    thread.start()
 
  for thread in threads:
    thread.join()
 
  print(account1.name, account1.balance)
  print(account2.name, account2.balance)

"""

"""

import threading
 
lock = threading.Lock()
 
def funcA():
  print("In A, acquiring lock")
  lock.acquire()
   
  print("In A, lock acquired")
   
  print("In A, lock acquiring again and entering into deadlock")
  lock.acquire()
   
  print("In A, releasing lock")
  lock.release()
   
  print("In A, lock released")
 
def funcB():
  print("In B, releasing lock acquired by A")
  lock.release()
   
  print("In B, lock released")
 
if __name__ == "__main__":
  thread1 = threading.Thread(target=funcA)
  thread2 = threading.Thread(target=funcB)
 
  thread1.start()
  thread2.start()
 
  thread1.join()
  thread2.join()

  print(account2.balance)

"""


"""
import threading
 
lock = threading.RLock()
 
def funcA():
  print("In A, acquiring lock")
  lock.acquire()
   
  print("In A, lock acquired, recursion level = 1")
   
  print("In A, acquiring lock again")
  lock.acquire()
   
  print("In A, lock acquired again, recursion level = 2")
   
  print("In A, releasing lock")
  lock.release()
   
  print("In A, lock released, recursion level = 1")
   
 
def funcB():
  print("In B, trying to acquire lock, but A released only once, so entering in deadlock state")
  lock.acquire()
  print("This statement won't be executed")
   
if __name__ == "__main__":
  thread1 = threading.Thread(target=funcA)
  thread2 = threading.Thread(target=funcB)
 
  thread1.start()
  thread2.start()
 
  thread1.join()
  thread2.join()
"""


import threading
import time
 
read_mutex = threading.Semaphore(4)
 
# Our shared resource
data = "A Data Stream"
 
class ReaderThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
 
  def run(self):
     
    read_mutex.acquire()
     
    output = self.getName() + " starts reading"
    print(output)
     
    # threads take time to read a data
    time.sleep(0.5)
    some_data = data
     
    output = self.getName() + " ends reading"
    print(output)
     
    read_mutex.release()
   
   
if __name__ == "__main__":
   
  threads = []
  for i in range(10):
    threads.append(ReaderThread())
 
  for thread in threads:
    thread.start()
 
  for thread in threads:
    thread.join()

 
