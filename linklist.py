class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                if current_node == self.head:
                    self.head = current_node.next
                return
            current_node = current_node.next

    def print_list_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def print_list_backward(self):
        current_node = self.head
        while current_node and current_node.next:
            current_node = current_node.next
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.prev
        print("None")

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Append elements
    dll.append("A")
    dll.append("B")
    dll.append("C")

    # Prepend elements
    dll.prepend("D")

    # Print the doubly linked list forward
    print("Forward:")
    dll.print_list_forward()  # Output: D -> A -> B -> C -> None

    # Print the doubly linked list backward
    print("Backward:")
    dll.print_list_backward()  # Output: C -> B -> A -> D -> None

    # Delete an element
    dll.delete_with_value("B")
    print("After deleting B:")
    dll.print_list_forward()  # Output: D -> A -> C -> None
