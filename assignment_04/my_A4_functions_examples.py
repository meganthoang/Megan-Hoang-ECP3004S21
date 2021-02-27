# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: 
#
# Date:
# 
##################################################
#
# Suggested Solutions for Assignment 4: 
# Examples to Test Functions with Examples
# This version has exception handling, 
# in case the scripts throw errors.
#
##################################################
"""



##################################################
# Import Required Modules
##################################################

# Import functions for handling exceptions.
import traceback
import logging
import sys
# This redirects errors to the output file (or stdout). 
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


# Import the function definitions from my_functions.py

print("#" + 50*"-")
print("# Importing function definitions")
print("# Doctest for script my_A4_functions.py:")
print("#" + 50*"-")


# Run the script to load those definitions.
try:
    exec(open("assignment_04/my_A4_functions.py").read())
    # This puts the function definitions in memory.
except Exception:
    print("Error reading my_A4_functions.py")
    logging.error(traceback.format_exc())
    # This lets the program continue if there is an error.
    # It also records the error message. 



# Import math and numpy because my test cases use 
# np.arrays and math.log
import math
import numpy as np





##################################################
# Run the solution examples to test these functions
##################################################


# Test the examples and print the results.

print("#" + 50*"-")
print("# Testing with examples in solutions")
print("#" + 50*"-")

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Note that it is extra cautious to")
print("send numpy arrays in the correct shape,")
print("in case the function is sensitive to the specification.")
print("I test with both arrays and lists, so that")
print("it might work for either specification.")

#--------------------------------------------------

print("#" + 50*"-")
print("Exercise 1, Example 1:")
eval_str = "matrix_multiply(np.array([[1., 2.], [3., 4.]]), np.array([1., 1.]).reshape(2,1))"
ans_str = str("array([[3.],[7.]])")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        matrix_multiply(np.array([[1., 2.], [3., 4.]]), np.array([1., 1.]).reshape(2,1))
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 1, Example 1:")
eval_str = "matrix_multiply([[1., 2.], [3., 4.]], [[1.], [1.]])"
ans_str = str("array([[3.],[7.]])")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        matrix_multiply([[1., 2.], [3., 4.]], [[1.], [1.]])
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 1, Example 2:")
eval_str = "matrix_multiply(list(range(4)), [[5.],[5.],[5.],[5.]])"
ans_str = str("array([[30.]])")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        matrix_multiply(list(range(4)), [[5.],[5.],[5.],[5.]])
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 1, Example 3:")
eval_str = "matrix_multiply(np.array([[1], [2]]), np.array([[3, 4]]))"
ans_str = str("array([[3., 4.],[6., 8.]])")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        matrix_multiply(np.array([[1], [2]]), np.array([[3, 4]]))
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 1, Example 3:")
eval_str = "matrix_multiply([[1], [2]], [[3, 4]])"
ans_str = str("array([[3., 4.],[6., 8.]])")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        matrix_multiply([[1], [2]], [[3, 4]])
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())


#--------------------------------------------------

# Additional examples to test out-of-bounds.

print("#" + 50*"-")
print("Exercise 1, Example 4:")
eval_str = "matrix_multiply(np.array([[1., 2.], [3., 4.]]), np.array([[3, 4]]))"
ans_str = str("Error: Matrices are not conformable...")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        matrix_multiply(np.array([[1., 2.], [3., 4.]]), np.array([[3, 4]]))
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Notice that the examples are simple sums of integers")
print("and one corner case evaluates to zero.")

#--------------------------------------------------

print("#" + 50*"-")
print("Exercise 2, Example 1:")
eval_str = "ssr_loops([2, 2, 2], [1, 1, 1], 0.5, 0.5)"
ans_str = str("3.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        ssr_loops([2, 2, 2], [1, 1, 1], 0.5, 0.5)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 2, Example 2:")
eval_str = "ssr_loops([3, 0, 3], [0, 2, 2], 1.0, 0.5)"
ans_str = str("9.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        ssr_loops([3, 0, 3], [0, 2, 2], 1.0, 0.5)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 2, Example 3:")
eval_str = "ssr_loops([2, 3, 4], [1, 2, 3], 1.0, 1.0)"
ans_str = str("0.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        ssr_loops([2, 3, 4], [1, 2, 3], 1.0, 1.0)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Notice that these are the same examples")
print("as for ssr_loops because the function")
print("performs the same calculations.")

#--------------------------------------------------

print("#" + 50*"-")
print("Exercise 3, Example 1:")
eval_str = "ssr_vec(np.array([2, 2, 2]), np.array([1, 1, 1]), 0.5, 0.5)"
ans_str = str("3.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        ssr_vec(np.array([2, 2, 2]), np.array([1, 1, 1]), 0.5, 0.5)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 3, Example 2:")
eval_str = "ssr_vec(np.array([3, 0, 3]), np.array([0, 2, 2]), 1.0, 0.5)"
ans_str = str("9.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        ssr_vec(np.array([3, 0, 3]), np.array([0, 2, 2]), 1.0, 0.5)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 3, Example 3:")
eval_str = "ssr_vec(np.array([2, 3, 4]), np.array([1, 2, 3]), 1.0, 1.0)"
ans_str = str("0.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        ssr_vec(np.array([2, 3, 4]), np.array([1, 2, 3]), 1.0, 1.0)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Notice that the first simple example is the same")
print("as one from Assignment 3.")
print("These should still work with only one observation.")

#--------------------------------------------------

print("#" + 50*"-")
print("Exercise 4, Example 1:")
eval_str = "logit_like_sum([1], [13.7], 0.0, 0.0)"
ans_str = str("-0.6931471805599453")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        logit_like_sum([1], [13.7], 0.0, 0.0)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 4, Example 2:")
eval_str = "logit_like_sum([1, 1, 1], [13.7, 12, 437], 0.0, 0.0)"
ans_str = str("-2.0794415416798357")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        logit_like_sum([1, 1, 1], [13.7, 12, 437], 0.0, 0.0)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 4, Example 3:")
eval_str = "logit_like_sum([1, 0], [1, 1], 0.0, math.log(2))"
ans_str = str("-1.504077396776274")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        logit_like_sum([1, 0], [1, 1], 0.0, math.log(2))
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 4, Example 4:")
eval_str = "logit_like_sum([1, 0], [2, 3], math.log(5), math.log(2))"
ans_str = str("-3.762362230873739")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        logit_like_sum([1, 0], [2, 3], math.log(5), math.log(2))
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

#--------------------------------------------------

print("#" + 50*"-")
print("Testing the corner case with non-binary y.")

print("#" + 50*"-")
print("Exercise 4, Example 5:")
eval_str = "logit_like_sum([1, 7], [2, 3], math.log(5), math.log(2))"
ans_str = str("Error: Observations in y must be either zero or one.")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        logit_like_sum([1, 7], [2, 3], math.log(5), math.log(2))
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

#--------------------------------------------------


print("#" + 50*"-")


##################################################
# End
##################################################
