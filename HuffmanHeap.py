# CMPT 145: Huffman Codes

# This file is copyright (c) Michael C Horsch, provided solely for the
# use of CMPT 145 students.  Students are welcome to use this file
# for their own work, and make copies for their own personal use.
# This file should not be shared for any reason without explicit
# consent of the author.

# Defines a data structure that allows Huffman codes to
# be computed efficiently.
#
# A Huffman Heap is a queue to store HuffmanTree objects.
# The word "heap" implies that the dequeue operation will always 
# remove and return the HuffmanTree object with the lowest frequency.

# CMPT 145: Assignment 10
# Name: Shea Slade
# NSID: sds266
# Student#:11235049
# Course#: CMPT 145
# Lab-04

import HuffmanTree as HT
class HuffmanHeap(object):
    def __init__(self, leafs, new_tree):
        """
        Purpose:
            Creates a new HuffmanHeap object.
        Pre-conditions:
            leafs: a list of HuffmanTree leaf nodes.
        Post-conditions:
            The heap is created and initialized.
        Return:
            None
        """
        self.__size = 0
        self.leafs = [leafs]
        self.new_tree = [new_tree]



    def enqueue(self, tree):
        """
        Purpose:
            Adds the tree to the Heap.  
            This is an O(1) operation.
        Pre-conditions:
            tree is a HuffmanTree object
        Post-conditions:
            the heap increases in size by 1
        Return:
            None
        """

        self.new_tree.append(tree)
        self.__size += 1
        return None

    def dequeue(self):
        """
        Purpose:
            Return the smallest value in the queue.
            This is an O(1) operation.
        Pre-conditions:
            None
        Post-conditions:
            The heap decreases in size by 1
        Return:
            A HuffmanTree object, with the lowest frequency
        """
        self.__size -= 1
        if self.leafs[0] < self.new_tree[0]:
            return self.leafs.pop(0)
        else:
            return self.new_tree.pop(0)

    def __len__(self):
        """
        Purpose:
            Return the number of data values stored in the heap.
            This method allows Python scripts to call len(hh)
            if hh is a HuffmanHeap object.
        Pre-conditions:
            None
        Post-conditions:
            None
        Return:
            The number of values stored in the heap
        """
        return self.__size

    def display(self):
        """
        Purpose:
            Display the data for debugging.
        Pre-conditions:
            None
        Post-conditions:
            None
        Return:
            None
        """
        print('Add code to HuffmanHeap.display() to help you debug.')

