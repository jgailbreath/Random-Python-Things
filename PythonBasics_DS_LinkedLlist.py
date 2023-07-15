# Linked list is a linear data structure.  Each element (a node) contains a value
# and a reference (a link) to the next node in the sequence.  They do not require
# contiguous memory allocation and can dynamically grow or shrink as needed.
# Each node holds the value of an element and a pointer/reference to the next node.
# The last node will have a reference to None to identify the end of the list.

# Ideal for when the size of the data is unknown or can change. They dynamically allocate
# memory as nodes are added or removed.

# Have fairly efficient insertion and deletion operations (especially when working with
# large datasets), typically requiring updates to a few pointers/references instead of
# having to use shift operations as in arrays.

# Serves as the foundation for more complex data structures like stacks, queues,
# and hash tables.

# Situations and Conditions when to use:
#-the size of the data can change dynamically
#-frequent insertion or deletion operations are expected
#-random access or indexing is not a requirement
#-memory allocation needs to be flexible

# When not to use:
#-frequent random access or searching is needed (linke list has a linear time complexity)
#-memory efficiency is a concern (linked list require additional mempory for storing the reference to the next node)

# Use Cases:
#-managing a playlist for songs (each song is a node and can be added/removed/deleted)
#-

# Bad use cases:
#-data analytics where sorting/searching/finding the median value would be a normal requirement
#-database storage (would have to traverse the linked list sequentially any time a search is initiated)


# Example of link list implementation.
# Node class representing a node in a linked list
class Node:
    def __init__(self, data):
        self.data = data  # Value of the node
        self.next = None  # Reference to the next node in the linked list

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list as None

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:
            self.head = new_node  # If the linked list is empty, make the new node as the head
        else:
            current = self.head
            while current.next:
                current = current.next  # Traverse to the last node
            current.next = new_node  # Set the next reference of the last node to the new node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Print the value of the current node
            current = current.next  # Move to the next node
        print("None")  # Print None to indicate the end of the linked list

# Create a linked list and perform operations
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()  # Output: 1 -> 2 -> 3 -> None
