# CMPT 145: Assignment 9
# Name: Shea Slade
# NSID: sds266
# Student#:11235049
# Course#: CMPT 145
# Lab-04
import a9q1_Stack as Stack
import a9q1_Queue as Queue


class Container(Stack.Stack,Queue.Queue):
    def __init__(self):
        pass

    def size(self):
        """
            Purpose
                returns the number of data values in the given queue
            Pre-conditions:
            Return:
                The number of data values in the queue
            """
        Stack.Stack.size(self)
        Queue.Queue.size(self)

    def is_empty(self):
        """
                Purpose
                    checks if the given queue has no data in it
                Pre-conditions:
                Return:
                    True if the queue has no data, or false otherwise
                """
        Stack.Stack.is_empty(self)
        Queue.Queue.is_empty(self)

    def peek(self):
        """
         Purpose
             returns the value from the front of container
             without removing it
         Pre-conditions:
         Post-condition:
             None
         Return:
             the value at the front of the container
         """
        Stack.Stack.peek(self)
        Queue.Queue.peek(self)

    def push(self, value):
        """
        Purpose
            adds the given data value to the given container
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the container
        Return:
            (none)
        """
        Stack.Stack.push(self,value)
        Queue.Queue.enqueue(self,value)

    def pop(self):
        """
         Purpose
             returns the value from the front of container
             by removing it
         Pre-conditions:
         Post-condition:
             first value is removed
         Return:
             the value at the front of the container
         """
        Stack.Stack.pop(self)
        Queue.Queue.dequeue(self)
