class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        #   1. create the Node from the value
        new_node = Node(value)
        # What do we do if tail is None?
        # What's the rule we want to set to indicate that the linked list is empty?
        # Would it be better to check the head?
        # Let's check them both: an empty linked list has an empty head & empty tail
        if self.head and self.tail is None:
            # in a one-element linked list, what should head and tail be referring to?
            # have both head and tail referring to a single node
            self.head = new_node
            # set the new node to be the tail
            self.tail - new_node
        else:
            # These steps assume that the tail is already referring to a Node
            # 2. set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node
            self.tail = new_node

    def remove_head(self):