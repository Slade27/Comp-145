# CMPT 145: Primitive Binary Search Trees

# This file is copyright (c) Michael C Horsch, provided solely for the
# use of CMPT 145 students.  Students are welcome to use this file
# for their own work, and make copies for their own personal use.
# This file should not be shared for any reason without explicit
# consent of the author.


# Defines functions for primitive Binary Search Tree data structure
#
# A Primitive Binary Tree is defined as follows:
# 1. The value None is a primitive binary tree;
#    None is an empty tree.
# 2. If lt and rt are primitive binary trees, and d is any value
#    TreeNode(d, lt, rt) is a primitive binary tree.

# A Primitive Binary Tree t satisfies the Binary Search Tree (BST)
# property if all of the following hold:
# 1. The key stored at TreeNode t is greater than any key
#    in t's left subtree (if any)
# 2. The key stored at TreeNode t is less than any key
#    in t's right subtree (if any)
# 3. t's left subtree satisfies the BST property
# 4. t's right subtree satisfies the BST property

# this implementation uses object-oriented KVTreeNode

# CMPT 145: Assignment 10
# Name: Shea Slade
# NSID: sds266
# Student#:11235049
# Course#: CMPT 145
# Lab-04

import KVTreeNode as TN

def member_prim(tnode, key):
    """
    Purpose:
        Check if key,value is stored in the binary search tree.
    Preconditions:
        :param tnode: a KVTreeNode with the BST property
        :param key: a key
    Postconditions:
        none
    :return: a pair True, value if key is in the tree
             a pair False, None if the key is not in the tree
    """
    if tnode is None:  # end of branch
        return False, None

    elif tnode.key == key:  # found key
        return True, tnode.value

    elif key < tnode.key:  # if less than kv key go left
        return member_prim(tnode.left, key)

    else:  # else go right
        return member_prim(tnode.right, key)



def insert_prim(tnode, key, value):
    """
    Insert a new key,value into the binary search tree.
    Preconditions:
        :param tnode: a KVTreeNode with the BST property
        :param key: a key
        :param value: a value to replace KVTreeNode value
    Postconditions:
        If the key is not already in the tree, it is added.
        If the key is already in the tree, the old value is replaced
        with the given value.
    Return
        :return: tuple (flag, tree)
        flag is True if insertion succeeded;
                tree contains the new key-value
        flag is False if the value is already in the tree,
                the value stored with the key is changed
    """
    if tnode is None:
        return True, TN.KVTreeNode(key, value)
    else:
        k = tnode.key
        if key == k:
            tnode.value = value
            return False, tnode

        elif key < k:
            flag, new = insert_prim(tnode.left, key, value)
            if flag:
                tnode.left = new
            return flag, tnode

        else:
            flag, new = insert_prim(tnode.right, key, value)
            if flag:
                tnode.right = new
            return flag, tnode



def delete_prim(tnode, key):
    """
    Delete a value from the binary search tree.
    Preconditions:
        :param tnode: a KVTreeNode with the BST property
        :param key: a key
    Postconditions:
        If the key is in the tree, it is deleted.  The tree
        retains the binary search tree property.
        If the key is not there, there is no change to the tree.
    Return
        :return: tuple (flag, tree)
        flag is True if deletion succeeded;
                tree is the resulting without the value
        flag is False if the value was not in the tree,
                tree returned unchanged
    """
    def delete(tnode):
        """
        does the work of deleting the key
        """

        if tnode is None:
            return False, tnode
        else:
            k = tnode.key
            if k == key:
                return reconnect(tnode)
            elif key < k:
                flag, sub = delete(tnode.left)
                if flag:
                    tnode.left = sub
                return flag, tnode
            else:
                flag, sub = delete(tnode.right)
                if flag:
                    tnode.right = sub
                return flag, tnode

    def reconnect(delnode):
        "removes and reconnects trees together"
        if delnode.left is None and delnode.right is None:
            # No Children
            return True, delnode.right
        elif delnode.left is None:
            # left only
            return True, delnode.right

        else:
        #delthisnode has two children
        # value in oldright is bigger than any value in oldleft
            oldleft = delnode.left
            oldright = delnode.right

            # find the place in oldleft to attach oldright
            # at the bottom right of oldleft!
            walker = oldleft
            while walker.right is not None:
                walker = walker.right

        # attach
            walker.right = oldright

        # oldleft has all the values, and is the new tree
            return True, oldleft

    # the body of delete_prim() is very short:
    return delete(tnode)

