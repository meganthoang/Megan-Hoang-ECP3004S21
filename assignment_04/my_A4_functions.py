# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Megan Hoang
#
# Date: 02/21/2021
# 
##################################################
#
# Sample Script for Assignment 4: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

import pandas as pd
import numpy as np
import math
import doctest

##################################################
# Function Definitions
##################################################

# Exercise 1
def matrix_multiply(mat_1, mat_2):
    """Calculate the log-likelihood of the logit function
    >>> matrix_multiply(np.array([[10, 9, 8], [7, 6, 5]], dtype = int), np.array([[1, 2, 3], [4, 5, 6]], dtype = int))
    [[46. 65. 84.]
     [31. 44. 57.]]
    array([[46., 65., 84.],
           [31., 44., 57.]])
    >>> matrix_multiply(np.array([[1, 2, 3], [4, 5, 6]], dtype = int), np.array([[10, 9, 8], [7, 6, 5]], dtype = int))
    [[24. 21. 18.]
     [75. 66. 57.]]
    array([[24., 21., 18.],
           [75., 66., 57.]])
    >>> matrix_multiply(np.array([[100, 48, 30], [20, 68, 38]], dtype = int), np.array([[9, 6, 8], [9, 3, 5]], dtype = int))
    [[1332.  744. 1040.]
     [ 792.  324.  500.]]
    array([[1332.,  744., 1040.],
           [ 792.,  324.,  500.]])
    """
    if len(mat_2) != len(mat_1):
        print("The matrices are not conformable")
        return None;
    else:
        result = np.zeros([len(mat_1), len(mat_2[0])])
        for i in range(len(mat_1)):
            for j in range(len(mat_2[0])):
                for k in range(len(mat_2)):
                    result[i][j] += mat_1[i][k]*mat_2[k][j]
        print(result)
        return result


# Exercise 2
df = pd.DataFrame({'hours':[10, 4, 6, 8, 12, 15, 14, 16, 13, 7, 10, 8, 6, 2, 8],
                   'score':[100, 35, 59, 79, 98, 100, 89, 57, 63, 91, 99, 77, 85, 63, 71]})
y = df['score']
x = df['hours']
def ssr_loops(y, x, beta_0, beta_1):
    """Calculate the sum of squared residuals of the regression model
    >>> ssr_vec(y1, x1, 2, 9)
    17631
    >>> ssr_vec(y1, x1, 6, 3)
    33839
    >>> ssr_vec(y1, x1, 0.5, 0.9)
    75925.68000000001
    """
    
    result = 0
    for i in range(len(y)):
        result += (y[i] - beta_0 - (beta_1 * x[i]))**2
    return result

# Exercise 3
vec = np.array([[10, 4, 6, 8, 12, 15, 14, 16, 13, 7, 10, 8, 6, 2, 8],
                   [100, 35, 59, 79, 98, 100, 89, 57, 63, 91, 99, 77, 85, 63, 71]])
y1 = vec[1]
x1 = vec[0]
def ssr_vec(y, x, beta_0, beta_1):
    """Calculate the sum of squared residuals of the regression model
    >>> ssr_vec(y1, x1, 2, 9)
    17631
    >>> ssr_vec(y1, x1, 6, 3)
    33839
    >>> ssr_vec(y1, x1, 0.5, 0.9)
    75925.68000000001
    """

    result = np.sum((y[0:] - beta_0 - (beta_1 * x[0:]))**2)
    return result


# Exercise 4
y = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
x = np.array([[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]])

def logit_like_sum(y, x, beta_0, beta_1): 
    """Calculate the log-likelihood of the logit function
    >>> logit_like_sum(y, x, 2, 0.5)
    
    >>> logit_like_sum(y, x, 2, 9)
    
    >>> logit_like_sum(y, x, 8, 9)
    
    """
    
    result = 0
    exp = 0
    for i in range(len(y)) :
        if y[i] == 0:
            exp = math.exp(beta_0+x[i]*beta_1)
            exp = math.log(exp/(1+exp))
            result += exp
        else:
            exp = 1-math.exp(beta_0+x[i]*beta_1)
            exp = math.log(exp/(1+exp))
            result += exp
    return result
    


##################################################
# Test the examples in your docstrings
##################################################

# Question 2: Test using the doctest module. 
doctest.testmod()

##################################################
# End
##################################################