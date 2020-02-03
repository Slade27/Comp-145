# CMPT 145: Assignment 9
# Name: Shea Slade
# NSID: sds266
# Student#:11235049
# Course#: CMPT 145
# Lab-04
import Node as node

class Queue(object):
    def __init__(self):
        self.queue = {}
        self.queue["size"] = 0
        self.queue["front"] = None
        self.queue["back"] = None

    def size(self):
        """
        Purpose
            returns the number of data values in the given queue
        Pre-conditions:
        Return:
            The number of data values in the queue
        """
        return self.queue["size"]

    def is_empty(self):
        """
         Purpose
             checks if the given queue has no data in it
         Pre-conditions:
         Return:
             True if the queue has no data, or false otherwise
         """
        return self.queue["size"] == 0

    def enqueue(self, value):
        """
        Purpose
            adds the given data value to the given queue
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the queue
        Return:
            (none)
        """
        self.new_node = node.Node(value, None)
        if self.is_empty():
            self.queue["front"] = self.new_node
            self.queue["back"] = self.new_node
        else:
            self.prev_last_node = self.queue["back"]
            node.Node.set_next(self.prev_last_node, self.new_node)
            self.queue["back"] = self.new_node

        self.queue["size"] += 1

    def dequeue(self):
        """
          Purpose
              removes and returns a data value from the given queue
          Pre-conditions:
          Post-condition:
              the first value is removed from the queue
          Return:
              the first value in the queue, or None
          """
        self.prev_first_node = self.queue["front"]
        self.queue["front"] = node.Node.get_next(self.prev_first_node)
        self.queue["size"] -= 1
        if self.queue["size"] == 0:
            self.queue["back"] = None
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
             the value at the front of the queue
         """
        if self.is_empty():
            return None
        else:
            self.result = node.Node.get_data(self.queue['front'])
            return self.result
