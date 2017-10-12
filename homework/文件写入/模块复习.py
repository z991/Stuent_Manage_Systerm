'''import collections
queue=collections.deque([1,2,3,4,5])
print(queue)
queue.append(6)
print(queue)
queue.append(7)
print(queue)
print(queue.popleft())
print(queue)'''

from collections import deque
queue=deque([1,2,3,4,5])
print(queue)
queue.append(6)
print(queue)
queue.append(7)
print(queue)
print(queue.popleft())
print(queue)