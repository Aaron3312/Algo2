import queue as q


customQueue = q.Queue(maxsize=3)

print(customQueue.qsize())

for i in range(5):
    customQueue.put(i)

print(customQueue.qsize())