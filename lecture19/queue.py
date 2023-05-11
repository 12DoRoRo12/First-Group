#deque
from collections import deque
  
# Initializing a queue
q = deque()
  
# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')
  
print("Initial queue")
print(q)
  
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
  
print("\nQueue after removing elements")
print(q)
  
# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty



#Implementation using queue.Queue
# Queue is built-in module of Python which is used to implement a queue. 
 

# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
# qsize() – Return the number of items in the queue.

  
from queue import Queue
  
# Initializing a queue
q = Queue(maxsize = 3)
  
# qsize() give the maxsize 
# of the Queue 
print(q.qsize()) 
  
# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')
  
# Return Boolean for Full 
# Queue 
print("\nFull: ", q.full()) 
  
# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
  
# Return Boolean for Empty 
# Queue 
print("\nEmpty: ", q.empty())
  
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())
  
# This would result into Infinite 
# Loop as the Queue is empty. 
# print(q.get())