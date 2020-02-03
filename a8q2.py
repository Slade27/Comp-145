# CMPT 145: Assignment 8
# Name: Shea Slade
# NSID: sds266
# Student#:11235049
# Course#: CMPT 145
# Lab-04

import treenode as tn


def mirrored(t1, t2):
    """
     Purpose: Determine if two inputted trees are reflections of each other
     Preconditions:
         :param t1: A tree node
         :param t2: A tree node
     Post-conditions: None
         :return: A boolean value if the two trees are reflections or not
     """
    if t1 is None and t2 is None:  # If both are empty it is a reflection
        return True

    elif t1 is None or t2 is None:
        return False

    elif tn.get_right(t1) is None and tn.get_left(t1) is None: # If reached end of iteration
        return tn.get_data(t1) == tn.get_data(t2)

    elif tn.get_right(t2) is None and tn.get_left(t2) is None:
        return tn.get_data(t1) == tn.get_data(t2)

    else:  # If not false already iterate though the trees
        if tn.get_data(t1) == tn.get_data(t2):
            left1 = tn.get_left(t1)
            right1 = tn.get_right(t1)
            left2 = tn.get_left(t2)
            right2 = tn.get_right(t2)
            return mirrored(left1, right2) and mirrored(left2, right1)
    return False


def reflect(tnode):
    """
    Purpose: Copy the inputted tree and reflect it
    Preconditions:
        :param tnode: A tree node to be reflected and copied
    Post-conditions: reflects the inputted tree fulfilling the reflection property
        :return: None
    """

    if tnode is None:  # Special case if tree is None
        return None

    else:
        right = tn.get_right(tnode)  # simplify right and left
        left = tn.get_left(tnode)

        reflect(left)  # Iterate through the tree
        reflect(right)

        tn.set_left(tnode, right)  # Set each tree on the on right to tree on the left ect.
        tn.set_right(tnode, left)


def refection(tnode):
    """
    Purpose: Copy the inputted tree and return a reflected copy
    Preconditions:
        :param tnode: A tree node to be reflected and copied
    Post-conditions: None
        :return: The reflected and copied tree
    """

    if tnode is None:  # Special case if tree is None
        return None
    else:  # a new tree with subtrees swapped
        return tn.create(tn.get_data(tnode), refection(tn.get_right(tnode)), refection(tn.get_left(tnode)))


