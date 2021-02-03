# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Megan Hoang
#
# Date: 1/30/2021
# 
##################################################
#
# Script for Assignment 2: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

import math


##################################################
# Function Definitions
##################################################

# Exercise 1

def average(num1: float, num2: float) -> float:
    """Return the average of num1 and num2.
    >>> average(10,20)
    15.0
    >>> average(2.5, 3.0)
    2.75
    >>> average(32, 19)
    25.5
    """

    return (num1 + num2) / 2


# Exercise 2

def area_of_circle(radius: float) -> float:
    """Return the area of a circle given the radius.
    >>> area_of_circle(2)
    12.57
    >>> area_of_circle(5)
    78.54
    >>> area_of_circle(10)
    314.16
    """

    return math.pi * radius * radius
 
 
# Exercise 3

def volume_of_cylinder(radius: float, height: float) -> float:
    """Return the volume of a cylinder given the radius and height.
    >>> volume_of_cylinder(2, 5)
    62.83
    >>> volume_of_cylinder(5, 5)
    392.70
    >>> volume_of_cylinder(10, 5)
    1570.80
    """

    return area_of_circle(radius) * height
 
    
# Exercise 4
def utility(x: float, y: float, a: float) -> float:
    """Return the utility of a function given x, y, and alpha
    >>> utility(1, 2, 0.5)
    1.41
    >>> utility(5, 7, 0.25)
    6.44
    >>> utility(10, 32, 0.01)
    31.63
    """
    
    return  (x**a * y**(1-a))


# Exercise 5
def logit(x: float, b0: float, b1: float) -> float:
    """Return the utility of a function given x, y, and alpha
    >>> logit(0.5, 1, 2)
    0.881
    >>> logit(0.25, 5, 10)
    0.999
    >>> logit(0.01, 3, 7)
    0.956
    """
    
    return math.exp(b0+x*b1) / (1+ math.exp(b0+x*b1))


##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results. 


print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating average(10,20)")
print("Expected: " + str(15.0))
print("Got: " + str(average(10,20)))


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating average(2.5, 3.0)")
print("Expected: " + str(2.75))
print("Got: " + str(average(2.5, 3.0)))


print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating average(32, 19)")
print("Expected: " + str(25.5))
print("Got: " + str(average(32, 19)))


# Exercise 2
print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating area_of_circle(2)")
print("Expected: " + str(12.57))
print("Got: " + str(round(area_of_circle(2), 2)))

print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating area_of_circle(5)")
print("Expected: " + str(78.54))
print("Got: " + str(round(area_of_circle(5), 2)))

print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating area_of_circle(10)")
print("Expected: " + str(314.16))
print("Got: " + str(round(area_of_circle(10), 2)))


# Exercise 3
print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating volume_of_cylinder(2, 5)")
print("Expected: " + str(62.83))
print("Got: " + str(round(volume_of_cylinder(2, 5), 2)))

print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating volume_of_cylinder(5, 5)")
print("Expected: " + str(392.70))
print("Got: " + str(round(volume_of_cylinder(5, 5), 2)))

print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating volume_of_cylinder(10, 5)")
print("Expected: " + str(1570.80))
print("Got: " + str(round(volume_of_cylinder(10, 5), 2)))


# Exercise 4
print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating utility(1, 2, 0.5)")
print("Expected: " + str(1.41))
print("Got: " + str(round(utility(1, 2, 0.5), 2)))

print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating utility(5, 7, 0.25)")
print("Expected: " + str(6.44))
print("Got: " + str(round(utility(5, 7, 0.25), 2)))

print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating utility(10, 32, 0.01)")
print("Expected: " + str(31.63))
print("Got: " + str(round(utility(10, 32, 0.01), 2)))


# Exercise 5
print("#" + 50*"-")
print("Testing my Examples for Exercise 5.")

print("#" + 50*"-")
print("Exercise 5, Example 1:")
print("Evaluating logit(0.5, 1, 2)")
print("Expected: " + str(0.881))
print("Got: " + str(round(logit(0.5, 1, 2), 3)))

print("#" + 50*"-")
print("Exercise 5, Example 1:")
print("Evaluating logit(0.25, 5, 10)")
print("Expected: " + str(.999))
print("Got: " + str(round(logit(0.25, 5, 10), 3)))

print("#" + 50*"-")
print("Exercise 5, Example 1:")
print("Evaluating logit(0.01, 3, 7)")
print("Expected: " + str(0.956))
print("Got: " + str(round(logit(0.01, 3, 7), 3)))


##################################################
# End
##################################################




    
    

