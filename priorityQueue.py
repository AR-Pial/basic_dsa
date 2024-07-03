from collections import deque

class PriorityQueue:
    def __init__(self):
        self._queue = deque()

    def push(self, item, priority):
        # Find the correct position to insert the new item to maintain the queue sorted by priority
        if not self._queue:
            # If the queue is empty, just append the new item
            self._queue.append((priority, item))
        else:
            # Iterate through the queue to find the correct insertion point
            for index, (p, i) in enumerate(self._queue):
                if priority < p:
                    # Insert the new item at the current index if its priority is higher
                    self._queue.insert(index, (priority, item))
                    break
            else:
                # If no higher priority is found, append the new item to the end
                self._queue.append((priority, item))

    def pop(self):
        # Pop the item with the highest priority (first element in the deque)
        return self._queue.popleft()[1]

    def is_empty(self):
        return not self._queue

    def __str__(self):
        # Return a string representation of the priority queue
        if not self._queue:
            return "PriorityQueue: Empty"
        else:
            items = ", ".join([f"{item} (Priority: {priority})" for priority, item in self._queue])
            return f"PriorityQueue: [{items}]"

# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push("task1", 1)
    pq.push("task2", 3)
    pq.push("task3", 2)
    print("pq : ", pq)
    while not pq.is_empty():
        print(pq.pop())


