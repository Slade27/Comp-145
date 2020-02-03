# CMPT 145: Assignment 7
# Name: Shea Slade
# NSID: sds266
# Student#:11235049
# Course#: CMPT 145
# Lab-04


def fib_seq(n):
    """
    Purpose: Fi33nd the nth Fibonacci number
    Preconditions:
    :param n: the nth iteration of Fibonacci numbers N>0
    Post conditions:
    The value of n is changed
    :return: The nth Fib Number
    """
    # Creates error if n is less than 0
    assert n >= 0, "Less than 0"

    if n == 0:  # Base Cases
        return 0
    elif n == 1:
        return 1
    elif n > 1:  # Recursive function while n>1
        return fib_seq(n-1) + fib_seq(n-2)


def moo_seq(m):
    """
      Purpose: Find the nth Mooseonacci number
      Preconditions:
      :param m: the nth iteration of Mooseonacci numbers (m>0)
      Post conditions:
      The value of n is changed
      :return: The nth Mooseonacci Number
      """
    # Creates error if n is less than 0
    assert m >= 0, "Less than 0"

    if m == 0:  # Base Cases
        return 0
    elif m == 1:
        return 1
    elif m == 2:
        return 2
    elif m > 1:  # Recursive function while n>1
        return moo_seq(m-1) + moo_seq(m-2) + moo_seq(m-3)


def substr(s, c, r):
    """
         Purpose: Replace a target character in a string with another selected character
         Preconditions:
         :param s: An inputted string example
         :param c: A target character in string
         :param r: A character to replace the target with
         Post conditions:
         A new list is returned each time
         :return: The new string with replaced characters
         """
    assert len(s) > 0, "Empty String"

    if c not in s:  # If there is no target in s
        return s
    elif s[0] == c:  # If the first character is the target replace it
        print("This")
        return r + substr(s[1:], c, r)
    else:  # If not first return the regular character
        print("That")
        return s[0] + substr(s[1:], c, r)
