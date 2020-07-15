"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if newnode < node.value
        if value < self.value:
        #    if left doesn't exist
            if self.left is None:
        #        create left
                self.left = BSTNode(value)
        #       else
            else:
        #           leftnode.insert(value)
                self.left.insert(value)
        #   if >=
        else:
        #       if right doesn't exist
            if self.right is None:
        #           create right
                self.right = BSTNode(value)
        #       else
            else:
        #           rightnode.insert(value)
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        # if node is None
        # return false
        # elif node.value == findvalue
        #   return true
        # else
        #   if find < node.value:
        #      contains on node.left
        #   else
        #      contains on node.right:

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass 

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
