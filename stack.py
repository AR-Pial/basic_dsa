class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Can not pop from a empty list!")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Can not pop from a empty list!")
        return self.items[-1]
    def size(self):
        return len(self.items)

    def search(self, item):
        try:
            index = self.items.index(item)
            return len(self.items) - index
        except ValueError:
            return -1

    def __str__(self):
        return str(self.items)


stack = Stack()

stack.push("Age of Empire")
stack.push("project IGI")
stack.push("Farm Frenzy")
stack.push("Vice")

print("Is empty : ", stack.is_empty())
print("Stack List : ", stack)
print("Size : ", stack.size())
print("Pop : ", stack.pop())
print("Stack List : ", stack)
print("Peek : ", stack.peek())
searchItem = "Farm Frenzy"
result = stack.search(searchItem)

if result != -1:
    print(f"{searchItem} is in Index No.  : {result}")
else:
    print(f"{searchItem} not foundin the stack!")

