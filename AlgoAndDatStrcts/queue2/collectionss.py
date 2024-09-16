from collections import deque

customQueue= deque(maxlen=3)
print(customQueue)

for i in range(6):
    customQueue.append(i)

print(customQueue)
print(customQueue.popleft())
print(customQueue)
print(customQueue.clear())
print(customQueue)