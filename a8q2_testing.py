# CMPT 145: Assignment 8
# Name: Shea Slade
# NSID: sds266
# Student#:11235049
# Course#: CMPT 145
# Lab-04

import a8q2 as a8q2
import treebuilding as tb
import treetesting as tt
lecture_tree = tb.build_lecture_example()
reflect_lecture_tree = tb.build_reflect_lecture_example()
turtle_tree = tb.build_turtle()
xtree = tb.build_xtree_me()


####################################################################################################
#### UNIT TEST CASE: mirrored() ####
arg1 = lecture_tree
arg2 = reflect_lecture_tree
expected = True
reason = "Test if None is inputted"
result = a8q2.mirrored(arg1,arg2)
if result != expected:
    print('Test failed: reflection(): got', str(result), 'expected', str(expected), '--' + reason)
#### UNIT TEST CASE: mirrored() ####
arg1 = lecture_tree
arg2 = a8q2.refection(lecture_tree)
expected = True
reason = "Test if None is inputted"
result = a8q2.mirrored(arg1,arg2)
if result != expected:
    print('Test failed: reflection(): got', str(result), 'expected', str(expected), '--' + reason)
####################################################################################################
arg1 = turtle_tree
arg2 = a8q2.reflect(turtle_tree)
expected = False
reason = "Test if None is inputted"
result = a8q2.mirrored(arg1,arg2)
if result != expected:
    print('Test failed: reflection(): got', str(result), 'expected', str(expected), '--' + reason)
#####################################################################################################
#### UNIT TEST CASE: reflection() ####
args_in = lecture_tree
expected = reflect_lecture_tree
reason = 'Test if the copy is equal to a relect of original tree'

result = a8q2.refection(args_in)
if result != expected:
    print('Test failed: reflection(): got', tt.to_string_for_testing(result), 'expected', tt.to_string_for_testing(expected), '--' + reason)

#### UNIT TEST CASE: reflection() ####
args_in = None
expected = None
reason = "Test if None is inputted"
result = a8q2.refection(args_in)
if result != expected:
    print('Test failed: reflection(): got', str(tt.to_string_for_testing(result)), 'expected', str(tt.to_string_for_testing(expected)), '--' + reason)

#### UNIT TEST CASE: reflection() ####
args_in = None
expected = None
reason = "Test if None is inputted"
result = a8q2.refection(args_in)
if result != expected:
    print('Test failed: reflection(): got', str(tt.to_string_for_testing(result)), 'expected', str(tt.to_string_for_testing(expected)), '--' + reason)

####################################################################################################
#### UNIT TEST CASE: reflect() ####
args_in = lecture_tree
reason = "Test if None is inputted"
result = a8q2.reflect(args_in)
if lecture_tree != reflect_lecture_tree:
    print('Test failed: reflect(): got', str(tt.to_string_for_testing(args_in)), 'expected', str(tt.to_string_for_testing(reflect_lecture_tree)), '--' + reason)

#### UNIT TEST CASE: reflect() ####
args_in = None
expected = None
reason = "Test if None is inputted"
result = a8q2.reflect(args_in)
if result != expected:
    print('Test failed: reflect(): got', str(tt.to_string_for_testing(result)), 'expected', str(tt.to_string_for_testing(expected)), '--' + reason)
####################################################################################################
print('*** testing complete ***')