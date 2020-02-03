# CMPT 145: Assignment 8
# Name: Shea Slade
# NSID: sds266
# Student#:11235049
# Course#: CMPT 145
# Lab-04
import treenode as tn


def subst(tnode, t, r):
    """
      Purpose: Find the target value in a Tree and replace it

     Preconditions:
        :param tnode: A Node chain
        :param t: The data to be replaced
        :param r: Data to replace target
    Post-conditions:
        modifies original node data
    :return:
        The Tree after replacement of data
     """

    if tnode is None:  # Special case where  tree node is empty
        return
    elif tn.get_data(tnode) == t:  # Case where data is found at current tree node
        tn.set_data(tnode, r)
        left = tn.get_left(tnode)
        right = tn.get_right(tnode)
        subst(left, t, r)
        subst(right, t, r)
        return tnode

    else:
        left = tn.get_left(tnode)
        right = tn.get_right(tnode)  # Case where data is not found, move to next ree node
        subst(left, t, r)
        subst(right, t, r)
        return tnode


def copy(tnode):
    """
    Purpose: Copy a tree and return the copy
    Preconditions:
        :param tnode: A tree node to be copied
    Post-conditions: None
        :return: The reference to the copied tree
    """
    if tnode is None:  # Special case if tree is None
        return None
    else:
        return tn.create(tn.get_data(tnode), copy(tn.get_left(tnode)), copy(tn.get_right(tnode)))   # return a copy of items in tree


def nodes_at_level(tnode, level):
    """
       Purpose: Find number of nodes in a selected level of a  primitive tree
      Preconditions:
         :param tnode: A Tree node
         :param level: The level on the tree to be counted
     :return:
         The number of nodes in the selected tree level
      """
    if tnode is None:  # Case where there is no node at the selected level
        return 0
    elif level is 0:  # Case where there is a node at selected level
        return 1
    else:  # take the left and right nodes and add them together to find number of nodes in level
        left = tn.get_left(tnode)
        right = tn.get_right(tnode)
        return nodes_at_level(left, level-1) + nodes_at_level(right, level-1)


def smallest_leaf_value(tnode):
    """
        Purpose: Find the smallest value in the leaf nodes of a tree
       Preconditions:
          :param tnode: A Tree node
      :return:
          The smallest value in the leaf nodes data
       """
    if tnode is None: # If node is none return none
        return None
    if tn.get_right(tnode) is None and tn.get_left(tnode) is None:  # If it is a leaf node, return data
        return tn.get_data(tnode)
    else:
        left = smallest_leaf_value(tn.get_left(tnode))  # loop through the left and right branches of tree
        right = smallest_leaf_value(tn.get_right(tnode))
        return min(left, right)  # Return smallest value


def closest(tnode, target):
    """
            Purpose: Find the closes value to the target in the  nodes of a tree
           Preconditions:
              :param tnode: A Tree node
              :param target: A target integer
          :return:
              The closest value in the nodes to the target
           """
    if tn.get_data(tnode) == target:  # if it is the target cant get any closer so return data
        return tn.get_data(tnode)
    if tnode is None:  # if tnode is none return
        return 0
    else:
        closest(tn.get_left(tnode), target)  # iterate through the data values
        closest(tn.get_right(tnode), target)
