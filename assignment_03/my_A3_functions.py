# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Megan Hoang
#
# Date: February 9, 2021
# 
##################################################
#
# Script for Assignment 3: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module
import math


##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def quad_roots_1(x: float, a: float, b: float, c: float) -> float:
    """Calculate the real-valued roots of the quadratic equation 
    given x, a, b, c
    >>> quad_roots_1(0.5, 2, -5, -3)
    [-.5, 3]
    >>> quad_roots_1(-1.15, 5, -2, -9)
    [-1.15, 1.55]
    >>> quad_roots_1(-2.54, 1, -1, -9)
    [-2.54, 3.54]    
    """
    x1 = -b + (b**2 - 4*a*c)**(1/2)
    x1 = x1/(2*a)
    x2 = -b - (b**2 - 4*a*c)**(1/2)
    x2 = x2/(2*a)
    return [x1, x2]
 

# Exercise 2
def quad_roots_real(x: float, a: float, b: float, c: float) -> float:
    """Calculate the real-valued roots of the quadratic equation
    given x, a, b, c. Account for when the discriminant<0
    >>> quad_roots_real(0.5, 2, -5, -3)
    [-.5, 3]
    >>> quad_roots_real(-1.15, 5, -2, -9)
    [-1.15, 1.55]
    >>> quad_roots_real(-2.54, 1, -1, -9)
    [-2.54, 3.54]    
    """
    if b**2 - 4*a*c < 0:
        print("error: The discriminant is negative")
        return None
    
    return quad_roots_1(x, a, b, c)

# Exercise 3
def utility_positive(x: float, y: float, a: float) -> float:
    """Return the utility of a function given x, y, and alpha.
    Print error messages whenever an input is negative
    >>> utility_positive(1, 2, 0.5)
    1.41
    >>> utility_positive(5, 7, 0.25)
    6.44
    >>> utility_positive(-10, 32, 0.01)
    None + "x is negative"
    """
    
    if x<0 or y<0 or a<0:
        if x<0:
            print("x is negative")
        if y<0:
            print("y is negative")
        if a<0:
            print("a is negative")
        return None
    else :
      return  (x**a * y**(1-a))


# Exercise 4
def logit_like(y: int, x: float, b0: float, b1: float) -> float: 
    """Calculate the log-likelihood of the logit function
    >>> logit_like(0, 1, 2, 0.5)
    1.08
    >>> logit_like(6, 3, 2, 9)
    None
    >>> logit_like(10, 3, 8, 9)
    None
    """
    
    exp = math.exp(b0+x*b1)
    exp = math.log(exp/(1+exp))
    if y==0:
        return 1-exp
    elif y==1:
        return exp


# Only function definitions above this point. 


##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results. 

# Exercise 1

print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating quad_roots_1(0.5, 2, -5, -3)")
print("Expected: " + str([-.5, 3]))
print("Got: " + str(quad_roots_real(0.5, 2, -5, -3)))

print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating quad_roots_1(-1.15, 5, -2, -9)")
print("Expected: " + str([-1.15, 1.55]))
print("Got: " + str(quad_roots_real(-1.15, 5, -2, -9)))

print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating quad_roots_1(-2.54, 1, -1, -9)")
print("Expected: " + str([-2.54, 3.54]))
print("Got: " + str(quad_roots_real(-2.54, 1, -1, -9)))

# Exercise 2

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating quad_roots_real(0.5, 2, -5, -3)")
print("Expected: " + str([-.5, 3]))
print("Got: " + str(quad_roots_real(0.5, 2, -5, -3)))

print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating quad_roots_real(-1.15, 5, -2, -9)")
print("Expected: " + str([-1.15, 1.55]))
print("Got: " + str(quad_roots_real(-1.15, 5, -2, -9)))

print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating quad_roots_real(-2.54, 1, -1, -9)")
print("Expected: " + str([-2.54, 3.54]))
print("Got: " + str(quad_roots_real(-2.54, 1, -1, -9)))


# Exercise 3
print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating utility_positive(1, 2, 0.5)")
print("Expected: " + str(1.41))
print("Got: " + str(round(utility_positive(1, 2, 0.5), 2)))

print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating utility_positive(5, 7, 0.25)")
print("Expected: " + str(6.44))
print("Got: " + str(round(utility_positive(5, 7, 0.25), 2)))

print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating utility_positive(10, 32, 0.01)")
print("Expected: " + "x is negative + None" )
print("Got: " + str(utility_positive(-10, 32, 0.01)))


# Exercise 4

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating logit_like(0, 1, 2, 0.5)")
print("Expected: " + str(1.08))
print("Got: " + str(logit_like(0, 1, 2, 0.5)))

print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating logit_like(6, 3, 2, 9)")
print("Expected: " + "None")
print("Got: " + str(logit_like(6, 3, 2, 9)))


print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating logit_like(10, 3, 8, 9)")
print("Expected: " + "None")
print("Got: " + str(logit_like(10, 3, 8, 9)))


##################################################
# End
##################################################