# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Megan Hoang
#
# Date: May 3rd, 2021
# 
##################################################
#
# Script for Final Exam: 
# Module with Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for a script that you might call
# my_midterm_tests.py (but is not graded).
##################################################
##################################################
"""



##################################################
# Import Required Modules
##################################################

# import name_of_module
import pandas as pd # we typically use this function to read in & manipulate files
import os # We use this to set our working directory
import sqlite3 # This is the sql module we saw with Assignment 8
import csv
import numpy as np 
import math # this module gives us a variety of math functions like abs, round, etc.
import doctest # this is our testing module
from typing import List, Tuple
import os # To set working directory
# import numpy as np # Not needed here but often useful
import pandas as pd # To read and inspect data
# from sklearn.linear_model import LogisticRegression

# import statsmodels.formula.api as smf # Another way to estimate logistic regression
import statsmodels.api as sm # Another way to estimate logistic regression

# Need exponential function in likelihood function. 
import numpy as np
# And np arrays are used in calculation. 

# Import scipy package for optimization
# from scipy import optimize
from scipy.optimize import minimize


##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1


def ln_check(x: float, a: float) -> float:
    """
    
    Calculates calculates the difference between math.log(x) 
	and some candidate value a, which is a guess of the value of math.log(x).
    
    >>> ln_check(math.exp(7), 3)
    4.0
    >>> ln_check(math.exp(10), 1)
    9.0
    >>> ln_check(math.exp(22), 22)
    0.0
    
    """
    
    return math.log(x) - a



# Exercise 2


def calc_e(x0: float, max_iter: float, tol: float) -> float:
    """
    Preconditions: x_0, iter, tol > 0
    
    Calculates the base of the natural logarithm.
    
    >>> calc_e(2, 10, 0.001)
    Max Iterations Reached
    2048.0
    >>> calc_e(2.718281064358138, 100, 0.0001)
    2.718281064358138
    >>> calc_e(2.7, 100, 1)
    2.7
    
    """
    # Find the value of x for which ln(x) - 1 = 0
    # Uses Newton's Method
    if abs(ln_check(x0, 1)) < tol:
        return x0
    x = x0
    for i in range(max_iter):
        # The derivative of log(x) = 1/x
        # The derivative of 1/x is -1/x**2
        x_next = x - ((1/x) / (-1/(x**2)))
        if abs(ln_check(x_next, 1)) < tol:
            return x_next
            break
        x = x_next
    print("Max Iterations Reached")
    return x



# Exercise 3


def SSR_conc(beta_1: float, y: List[float], x: List[float]) -> float:
    """
    Calculates the sum of squared residuals 
    for the linear regression model,
    as a function of the slope coefficient only, 
    concentrating out the intercept.
    
    
    >>> SSR_conc(1.0, [3, -3, 3], [1, 1, 1])
    24.0
    >>> SSR_conc(9.0, [1, 2, 3], [3, 2, 1])
    443.0
    >>> SSR_conc(2.0, [20, 20, 20], [20, 20, 20])
    0.0
    
    """
    # calculate y-bar (average of y values in list)
    numelem = 0.0
    total_y = 0.0
    for i in range(len(y)):
        total_y += y[i]
        numelem += 1
    y_bar = total_y / numelem
    
    # reset numelem and calculate x-bar (average of x values in list)
    numelem = 0.0
    total_x = 0.0
    for j in range(len(x)):
        total_x += x[i]
        numelem += 1
    x_bar = total_x / numelem
    
    # Use the relation b0 = y-bar - (x-bar * beta-1) to return the value of b0
    beta_0 = y_bar - (x_bar * beta_1)
    
    # Now, calculate the value of SSR within a loop
    ssr = 0
    for k in range(len(y)):
        ssr += (y[k] - beta_0 - (beta_1 * x[k])) ** 2
    return ssr


# Exercise 4


def ols_slope_conc(y: List[float], x: List[float]) -> float:
    """
    Calculates the estimated slope coefficient 
    for the linear regression model,
    by minimizing the concentrated sum of squared resduals, 
    which concentrates out the intercept.
    
    >>> ols_slope_conc([2, 1, 2], [1, 0, 1])
    0.6666666581095642
    >>> ols_slope_conc([1, 1, 1], [1, 1, 1])
    0.0
    >>> ols_slope_conc([1, 15, 30], [1, 5, 10])
    1.232704406634623
    """
    #minimum = minimize(SSR_conc, 0, args=(y, x), method = None)
    minimum = minimize(SSR_conc, 0, args=(y, x), method='BFGS', options = {'xtol': 1e-8, 'maxiter': 1000, 'disp': False})
    # scipy's .minimize function returns an OptimizeResult object
    # We want to look at the x value, which is an array that stores one value
    # so we return the value at index 0 of the array
    return minimum.x[0]


# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstrings above
# with the proper formatting. 

# Test all functions with three examples each. 
# One example is already provided. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# Add code so that the tests are implemented below 
# -- but only when the script is run,
# not when it is imported. 

if __name__ == "__main__":
    import doctest
    doctest.testmod()

##################################################
# End
##################################################
