# CMPT 145: Assignment 8
# Name: Shea Slade
# NSID: sds266
# Student#:11235049
# Course#: CMPT 145
# Lab-04

import treenode as tn
import treebuilding as tb
fib_tree = tb.build_fibtree(4)
tree1 = tb.build_lecture_example()



def complete(tnode):
    """
    Purpose :
    Determine if the given tree is complete .
    Pre - conditions :
    : param tnode : a primitive binary tree
    Return
    : return : A tuple (True , height ) if the tree is complete ,
    A tuple (False , None ) otherwise .
    """
    print("TNODE", tnode)

    if tnode is None:
        return False, None

    if tn.get_left(tnode) is None and tn.get_right(tnode) is None:  # complete subtree
        print("subtree complete")
        return True, +1

    if tn.get_left(tnode) is None and tn.get_right(tnode) is not None:  # incomplete subtree
        print("this")
        return False, None

    if tn.get_right(tnode) is None and tn.get_left(tnode) is not None:  # incomplete subtree
        print("that")
        return False, None

    else:
        ldepth = complete(tn.get_left(tnode))
        rdepth = complete(tn.get_right(tnode))
        return True, +1

print(complete(tree1))

###  Not sure how to transfer level in return statement ###