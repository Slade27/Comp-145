# CMPT 145: Assignment 9
# Name: Shea Slade
# NSID: sds266
# Student#:11235049
# Course#: CMPT 145
# Lab-04
import Node as node

class Stack(object):
    def __init__(self):
        self.stack = {}
        self.stack["size"] = 0
        self.stack["top"] = None
    def size(self):
        """
         Purpose
             returns the number of data values in the given queue
         Pre-conditions:
         Return:
             The number of data values in the queue
         """
        return self.stack["size"]

    def is_empty(self):
        """
           Purpose
               checks if the given queue has no data in it
           Pre-conditions:
               queue is a queue created by create()
           Return:
               True if the queue has no data, or false otherwise
           """
        return self.stack["size"] == 0

    def push(self, value):
        """
        Purpose
            adds the given data value to the given stack
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the stack
        Return:
            (none)
        """
        self.new_node = node.Node(value, self.stack["top"])
        self.stack["top"] = self.new_node
        self.stack["size"] += 1

    def pop(self):
        """
        Purpose
            removes and returns a data value from the given stack
        Pre-conditions:
        Post-condition:
            the first value is removed from the stack
        Return:
            the first value in the stack, or None
        """
        self.prev_first_node = self.stack["top"]
        self.stack["top"] = node.Node.get_next(self.prev_first_node)
        self.stack["size"] -= 1
        return node.Node.get_data(self.prev_first_node)

    def peek(self):
        """
         Purpose
             returns the value from the front of given stack
             without removing it
         Pre-conditions:
         Post-condition:
             None
         Return:
             the value at the front of the stack
         """
        return node.Node.get_data(self.stack["top"])

    def __str__(self):
        if self.is_empty():
            result = 'EMPTY'
        else:
            # walk along the chain
            walker = self.stack['top']
            value = node.Node.get_data(walker)
            # print the data
            result = '[ ' + str(value) + ' |'
            while node.Node.get_next(walker) is not None:
                walker = node.Node.get_next(walker)
                value = node.Node.get_data(walker)
                # represent the next with an arrow-like figure
                result += ' *-]-->[ ' + str(value) + ' |'

            # at the end of the stack, use '/'
            result += ' / ]'

        return result

new_stacks = Stack()
ex_stack = list(range(5))
for st in ex_stack:
    new_stacks.push(st)

print(new_stacks.__str__())

new_stacks.push(99)
print(new_stacks.__str__())

