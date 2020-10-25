#Queue
from queue import Queue

q = Queue(maxsize = 5)

print(q.qsize())

q.put('a')
q.put('b')
q.put('c')
q.put('d')
q.put('e')

print("\nFull: ", q.full())

print("\nЕлементи, виведені з черги: ")
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())

print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())