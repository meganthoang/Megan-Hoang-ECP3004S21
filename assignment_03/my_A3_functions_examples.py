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
# Testing Script for Assignment 3:
# Function Definitions
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
print("# Examples within script my_A3_functions.py:")
print("#" + 50*"-")


# Run the script to load those definitions.
try:
    exec(open("assignment_03/my_A3_functions.py").read())
    # This puts the function definitions in memory.
except Exception:
    print("Error reading my_A3_functions.py")
    logging.error(traceback.format_exc())
    # This lets the program continue if there is an error.
    # It also records the error message. 




# Import math because my test cases use math.pi
# and math.log
import math



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
print("Exercise 1, Example 1:")
print("Evaluating quad_roots_1(1, -2, 1)")
print("Expected: " + str([1.0, 1.0]))
try:
    print("Got: " + str(quad_roots_1(1, -2, 1)))
except:
    print("Error in quad_roots_1(1, -2, 1)")
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating quad_roots_1(1, 0, -1)")
print("Expected: " + str([1.0, -1.0]))
try:
    print("Got: " + str(quad_roots_1(1, 0, -1)))
except:
    print("Error in quad_roots_1(1, 0, -1)")
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating quad_roots_1(2, 2, -12)")
print("Expected: " + str([2.0, -3.0]))
try:
    print("Got: " + str(quad_roots_1(2, 2, -12)))
except:
    print("Error in quad_roots_1(2, 2, -12)")
    logging.error(traceback.format_exc())


# Continue with the rest of your examples.
# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating quad_roots_real(1, -2, 1)")
print("Expected: " + str([1.0, 1.0]))
try:
    print("Got: " + str(quad_roots_real(1, -2, 1)))
except:
    print("Error in quad_roots_real(1, -2, 1)")
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating quad_roots_real(1, 0, -1)")
print("Expected: " + str([1.0, -1.0]))
try:
    print("Got: " + str(quad_roots_real(1, 0, -1)))
except:
    print("Error in quad_roots_real(1, 0, -1)")
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating quad_roots_real(2, 2, -12)")
print("Expected: " + str([2.0, -3.0]))
try:
    print("Got: " + str(quad_roots_real(2, 2, -12)))
except:
    print("Error in quad_roots_real(2, 2, -12)")
    logging.error(traceback.format_exc())

#--------------------------------------------------

# Additional examples to test out-of-bounds.

print("#" + 50*"-")
print("Exercise 2, Example 4:")
print("Evaluating quad_roots_real(0, 0, 0)")
print("Expected: " + str([247, math.sqrt(math.pi)/11]))
try:
    print("Got: " + str(quad_roots_real(0, 0, 0)))
except:
    print("Error in quad_roots_real(0, 0, 0)")
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 2, Example 5:")
print("Evaluating quad_roots_real(0, 0, 7.0)")
print("Expected: " + str(None))
try:
    print("Got: " + str(quad_roots_real(0, 0, 7.0)))
except:
    print("Error in quad_roots_real(0, 0, 7.0)")
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 2, Example 6:")
print("Evaluating quad_roots_real(0, 4.0, 2.0)")
print("Expected: " + str([-0.5, -0.5]))
try:
    print("Got: " + str(quad_roots_real(0, 4.0, 2.0)))
except:
    print("Error in quad_roots_real(0, 4.0, 2.0)")
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 2, Example 7:")
print("Evaluating quad_roots_real(1.0, 0, 1.0)")
print("Expected: " + str(None))
try:
    print("Got: " + str(quad_roots_real(1.0, 0, 1.0)))
except:
    print("Error in quad_roots_real(1.0, 0, 1.0)")
    logging.error(traceback.format_exc())


#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating utility_positive(0.0, 4.7, 0.5)")
print("Expected: " + str(0.0))
try:
    print("Got: " + str(utility_positive(0.0, 4.7, 0.5)))
except:
    print("Error in utility_positive(0.0, 4.7, 0.5)")
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating utility_positive(1.0, 1.0, 0.75)")
print("Expected: " + str(1.0))
try:
    print("Got: " + str(utility_positive(1.0, 1.0, 0.75)))
except:
    print("Error in utility_positive(1.0, 1.0, 0.75)")
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating utility_positive(4, 16, 0.5)")
print("Expected: " + str(8.0))
try:
    print("Got: " + str(utility_positive(4, 16, 0.5)))
except:
    print("Error in utility_positive(4, 16, 0.5)")
    logging.error(traceback.format_exc())

#--------------------------------------------------

# Additional examples to test out-of-bounds.


print("#" + 50*"-")
print("Exercise 3, Example 4:")
print("Evaluating utility_positive(-1.0, 1.0, 0.5)")
print("Expected: " + str(None))
try:
    print("Got: " + str(utility_positive(-1.0, 1.0, 0.5)))
except:
    print("Error in utility_positive(-1.0, 1.0, 0.5)")
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 3, Example 5:")
print("Evaluating utility_positive(1.0, -1.0, 0.5)")
print("Expected: " + str(None))
try:
    print("Got: " + str(utility_positive(1.0, -1.0, 0.5)))
except:
    print("Error in utility_positive(1.0, -1.0, 0.5)")
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 3, Example 6:")
print("Evaluating utility_positive(1.0, 1.0, -0.5)")
print("Expected: " + str(None))
try:
    print("Got: " + str(utility_positive(1.0, 1.0, -0.5)))
except:
    print("Error in utility_positive(1.0, 1.0, -0.5)")
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 3, Example 7:")
print("Evaluating utility_positive(1.0, 1.0, 1.5)")
print("Expected: " + str(None))
try:
    print("Got: " + str(utility_positive(1.0, 1.0, 1.5)))
except:
    print("Error in utility_positive(1.0, 1.0, 1.5)")
    logging.error(traceback.format_exc())


#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating logit_like(1, 13.7, 0.0, 0.0)")
print("Expected: " + str(math.log(0.5)))
try:
    print("Got: " + str(logit_like(1, 13.7, 0.0, 0.0)))
except:
    print("Error in logit_like(1, 13.7, 0.0, 0.0)")
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating logit_like(0, 0.0, math.log(2), 2.0)")
print("Expected: " + str(math.log(1.0/3.0)))
try:
    print("Got: " + str(logit_like(0, 0.0, math.log(2), 2.0)))
except:
    print("Error in logit_like(0, 0.0, math.log(2), 2.0)")
    logging.error(traceback.format_exc())


print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating logit_like(1, 1.0, 0.0, math.log(5))")
print("Expected: " + str(math.log(5.0/6.0)))
try:
    print("Got: " + str(logit_like(1, 1.0, 0.0, math.log(5))))
except:
    print("Error in logit_like(1, 1.0, 0.0, math.log(5))")
    logging.error(traceback.format_exc())


#--------------------------------------------------

# Additional example to test out-of-bounds.


print("#" + 50*"-")
print("Exercise 4, Example 4:")
print("Evaluating logit_like(7, 1.0, 0.0, math.log(5))")
print("Expected: " + str(None))
try:
    print("Got: " + str(logit_like(7, 1.0, 0.0, math.log(5))))
except:
    print("Error in logit_like(7, 1.0, 0.0, math.log(5))")
    logging.error(traceback.format_exc())

#--------------------------------------------------



print("#" + 50*"-")


##################################################
# End
##################################################
