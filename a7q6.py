# CMPT 145: Assignment 7
# Name: Shea Slade
# NSID: sds266
# Student#:11235049
# Course#: CMPT 145
# Lab-04

import node as node


def to_string(node_chain):
    """
     Purpose: Display a node chain as a string with references(arrows)
    Preconditions:
        :param node_chain: A Node chain
    Post-conditions: None
        :return: The Node chain as a string
    """
    if node_chain is None:  # Special case if Node chain is None
        return "EMPTY"
    elif node.get_next(node_chain) is None:  # Base case, where there is only one node
        val = node.get_data(node_chain)
        result = "[ " + str(val) + ' |' + ' / ]'
        return result

    else:  # When there is larger than 1 node in the chain
        val = node.get_data(node_chain)
        result = "[ " + str(val) + ' |' + ' *-]-->'
        return result + to_string(node.get_next(node_chain))


def copy(node_chain):
    """
    Purpose: Copy a node chain and return the reference to the first node
    Preconditions:
        :param node_chain: A Node chain to be copied
    Post-conditions: None
        :return: The reference to the first node in copied chain
    """

    if node_chain is None:  # Special case if Node chain is None
        return None  # make last value in chain None
    else:
        return node.create(node.get_data(node_chain), copy(node.get_next(node_chain)))  # new node with next:recursive


def replace(node_chain, target, replacement):
    """
      Purpose: Find the target value in a node chain and replace it

     Preconditions:
        :param node_chain: A Node chain
        :param target: The data to be replaced
        :param replacement: Data to replace target
    Post-conditions:
        modifies original node data
    :return:
        The Node chain after replacement of data
     """

    if node_chain is None:  # Special case where node chain is empty
        return "EMPTY"

    elif node.get_next(node_chain) is None:  # Case where last node is reached
        if node.get_data(node_chain) == target:
            node.set_data(node_chain, replacement)
            return node_chain
        else:
            return node_chain

    elif node.get_data(node_chain) == target:  # Case where there is more than one node left in the chain
        node.set_data(node_chain, replacement)
        nex = node.get_next(node_chain)
        replace(nex, target, replacement)
        return node_chain

    else:
        nex = node.get_next(node_chain)  # Case where data is not found, move to next node
        replace(nex, target, replacement)
        return node_chain

