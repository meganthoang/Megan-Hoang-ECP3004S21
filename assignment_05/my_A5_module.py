# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Megan Hoang
#
# Date: February 28, 2021
# 
##################################################
#
# Sample Script for Assignment 5: Function Definitions
#
##################################################
"""



##################################################
# Import Required Modules
##################################################

# import name_of_module
import numpy as np
# import pandas as pd
# import math
# import doctest

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1
def variance (x:list) -> float:
    """Calculate the variance of a list x.
    >>> variance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    8.25
    >>> variance([1, 1, 1, 1, 1, 1, 1, 1, 1])
    0.0
    >>> variance([1, 2, 8, 4, 6, 9, 15, 1, 18])
    32.99
    """
    mean = sum(x)/len(x)
    deviation = [(i-mean)**2 for i in x]
    result = sum(deviation)/len(x)
    return round(result, 2)


# Exercise 2
def covariance(x:list, y:list) -> float:
    """Calculate the covariance between lists x and y
    >>> covariance([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    -0.2
    >>> covariance([1, 1, 1, 1], [1, 1, 1, 1])
    -1.0
    >>> covariance([1, 2, 8, 4], [6, 9, 15, 1, 18])
    Both lists must be the same length!
    """
    n = len(x)
    if n!= len(y):
        print("Both lists must be the same length!")
        return None
    else:
        meanx = np.mean(x)
        meany = np.mean(y)
        result = 0
        for i in range(0, len(x)):
            result += ((x[i] - meanx) * (y[i] - meany))
        return round(result/(n-1), 2)

    
# Exercise 3
# Be careful with the order of the arguments:
# def ols_slope(x:list, y:list) -> float:
def ols_slope(y:list, x:list) -> float:
    """Calculate the slope coefficients for the linear regression model
    between lists x and y
    >>> ols_slope([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    1.0
    >>> ols_slope([1, 3, 5, 9], [1, 1, 1, 1])
    0.0
    >>> ols_slope([1, 2, 8, 4], [6, 9, 15, 1, 18])
    Both lists must be the same length!
    """
    n = len(x)
    if n!= len(y):
        print("Both lists must be the same length!")
        return None
    else:
        meanx = np.mean(x)
        meany = np.mean(y)
        num = 0
        denom = 0
        for i in range(0, len(x)):
            num += (x[i] - meanx) * (y[i] - meany)
            denom += (x[i] - meanx) ** 2
            
        # return round((num/denom), 2)
        return num/denom
         

# Exercise 4
def ols_intercept(x:list, y:list, beta_hat_1) -> float:
    """Calculate the intercept coefficients for a linear regression model 
    given lists x and y
    >>> ols_intercept([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 1)
    0.0
    >>> ols_intercept([10, 20, 30, 40, 50, 60], [100, 90, 80, 70, 60, 50], 12)
    -345.0
    >>> ols_intercept([1, 3, 5, 7, 9], [11, 13, 15], 7)
    Both lists must be the same length!
    """

    if len(x) != len(y):
        print("Both lists must be the same length!")
        return None
    else:
        meanx = np.mean(x)
        meany = np.mean(y)
        for i in range (len(x)):
            beta_hat_0 = (meany - beta_hat_1 * meanx)
            return round(beta_hat_0, 2)
        
# Exercise 5
# Again, keep the arguments in order:
def ssr(y, x, beta_0, beta_1) -> float:
    """Calculates the sum of squared residuals for 
    the bivariate linear regression model.
    y and x are lists of equal length
    and beta_0 and eta_1 are scalar coefficients. 
    >>> ssr(y = [2, 2, 2], x = [1, 1, 1], beta_0 = 0.5, beta_1 = 0.5)
    3.0
    >>> ssr(y = [3, 0, 3], x = [0, 2, 2], beta_0 = 1.0, beta_1 = 0.5)
    9.0
    >>> ssr(y = [2, 3, 4], x = [1, 2, 3], beta_0 = 1.0, beta_1 = 1.0)
    0.0
    """

    if len(x) != len(y):
        print("Both lists must be the same length!")
        return None
    else: 
        ssr = 0
        for i in range(len(y)):
            ssr_i = (y[i] - beta_0 - beta_1*x[i])**2
            ssr = ssr + ssr_i           
        return ssr

# Exercise 6
def min_ssr(y, x, beta_0_min, beta_0_max, beta_1_min, beta_1_max, step) -> list:
    """Calculate values of beta0 and beta1 that produce the lowest SSR
    >>> min_ssr([1, 2, 3], [4, 5, 6], 1, 2, 1, 2, 0.5)
    [1.5, 1.5]
    >>> min_ssr([1, 1, 1], [30, 27, 24], 2, 5, 3, 8, 0.02)
    [4.980000000000002, 7.980000000000004]
    >>> min_ssr([12, 34, 26], [22, 75, 6], 2, 3, 4, 5, 1)
    [2, 4]
    """
    if len(x) == len(y):
        b_0 = list(np.arange(beta_0_min, beta_0_max, step))
        b_1 = list(np.arange(beta_1_min, beta_1_max, step))
        lowest = 999999
        min_i = 0
        min_j = 0
        for i in range(len(b_0)):
            for j in range(len(b_1)):
                SSR = ssr(x, y, b_0[i], b_1[j])
                if SSR < lowest:
                   lowest = SSR
                   min_i = i
                   min_j = j
        return [b_0[min_i], b_1[min_j]]
    else:
        print("Both lists must be the same length!")
        return None

# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    


##################################################
# End
##################################################