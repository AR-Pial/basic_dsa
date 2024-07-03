from collections import deque

queue = deque()

queue.append("CSE")
queue.append("EEE")
queue.append("CIVIL")

print("Queue : ", queue)
print(queue.popleft())
print("Queue : ", queue)