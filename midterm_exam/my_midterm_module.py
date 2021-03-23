# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:35:22 2021

@author: megan
"""

# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Megan Hoang
#
# Date: March 8th, 2021
# 
##################################################
#
# Sample Script for Midterm Exam: 
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

"""
Truly excellent work!
Perfect, except I will deduct 0.000000000000001 points 
for the error in Exercise 2 (but then round to the nearest 1%).
"""




##################################################
# Import Required Modules
##################################################

# import name_of_module
import numpy as np
import doctest


##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1


def in_budget(x: float, y: float, p_x: float, p_y: float, w: float) -> bool:
    """
    Preconditions: x, y, w >= 0 and p_x, p_y > 0
    
    Calculates returns a boolean indicator 
    of whether the consumer's expenditure 
    is less than or equal to wealth.
    
    >>> in_budget(3, 1, 10, 25, 100)
    True
    >>> in_budget(1, 1, 10, 10, 20)
    True
    >>> in_budget(400, 100, 10, 25, 10)
    False
    """

    if (((x*p_x) + (y*p_y)) <= w):
        return True
    else:
        return False



# Exercise 2


def calc_bundle(p_x: float, p_y: float, w: float, alpha: float):
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    
    >>> calc_bundle(10, 20, 120, 1.0/3.0)
    [4.0, 4.0]
    >>> calc_bundle(15, 3, 33, 1)
    [2.2, 0.0]
    >>> calc_bundle(10, 10, 100, 0.5)
    [5.0, 5.0]
    
    """
    x_star = alpha/p_x * w
    y_star = (1-alpha)/p_y * w
    
    return [x_star, y_star]



# Exercise 3


def y_solve(x_star: float, p_x: float, p_y: float, w: float) -> float:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= x_star <= w/p_x
    
    Calculates the remaining expenditure on good y, 
    given an expenditure x_star in good x.
    
    >>> y_solve(5, 5, 10, 100)
    7.5
    >>> y_solve(20, 5, 10, 100)
    0.0
    >>> y_solve(4, 15, 20, 200)
    7.0
    
    """
    y_star = (w - (x_star * p_x)) / p_y
    
    return y_star


# Exercise 4


def one_loop_bundle(p_x: float, p_y: float, w: float, alpha: float, step):
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    It searches over a loop on x_star and assigns the remaining
    wealth to y using y_solve.
    
    >>> one_loop_bundle(5, 10, 100, 0.25, 0.01)
    [5.0, 7.5]
    >>> one_loop_bundle(15, 3, 300, 0.5, 0.1)
    [10.0, 50.0]
    >>> one_loop_bundle(10, 10, 100, 1, 1)
    [9.0, 1.0]
    """
    x_star = 0
    y_temp = 0
    y_star = 0
    max_util = 0
    
    # list of all possible values of x
    x_star_list = np.arange(0, w/p_x, step)
    
    for i in range(len(x_star_list)):
        y_temp = y_solve(x_star_list[i], p_x, p_y, w)
        if ((x_star_list[i]**alpha * y_temp**(1-alpha)) > max_util):
            max_util = x_star_list[i]**alpha * y_temp**(1-alpha)
            y_star = y_temp
            x_star = x_star_list[i]
    
    return [x_star, y_star]



# Exercise 5


def util_in_budget(x: float, y: float, p_x: float, p_y: float, w, alpha) -> float:
    """Calculates the value of the Cobb-Douglass utility
    function for consumption goods x and y with exponent alpha.
    It restricts x and y to non-negative values and 
    alpha to the unit interval.
    It also restricts the calculation to bundles [x, y] within budget w, 
    otherwise it assigns zero.
    
    >>> util_in_budget(4, 4, 10, 20, 120, 1.0/3.0)
    4.0
    >>> util_in_budget(5, 5, 10, 10, 500, 1.0)
    5.0
    >>> util_in_budget(-1, 8, 10, 30, 172, 0.5)
    0
    """
    if ((in_budget(x, y, p_x, p_y, w) == True) and (x>=0) and (y>=0) and (alpha<=1) and (alpha>=0)):
        return (x**alpha * y**(1-alpha))
    else:
        return 0



# Exercise 6


def two_loop_bundle(p_x: float, p_y: float, w, alpha, step):
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    It searches over two loops on x_star and y_star.
    
    Note that there is no error handling
    because that is taken care of in util_in_budget() and np.arange(). 
    
    >>> two_loop_bundle(10, 25, 100, 0.5, 0.01)
    [5.0, 2.0]
    >>> two_loop_bundle(10, 10, 100, 0.25, 0.1)
    [2.5, 7.5]
    >>> two_loop_bundle(33, 16, 700, .6, 1)
    [12.0, 19.0]
    """
    x_star_list = np.arange(0, w/p_x, step)
    y_star_list = np.arange(0, w/p_y, step)

    max_util = 0
    i_max = None
    j_max = None
    
    for i in range(len(x_star_list)):
        for j in range(len(y_star_list)):
            x_star = x_star_list[i]
            y_star = y_star_list[j]
            
            util_ij = util_in_budget(x_star, y_star, p_x, p_y, w, alpha)
        
            if util_ij > max_util:
                max_util = util_ij
                i_max = i
                j_max = j
                
    # At the end, if a lowest value was found, 
    # output those values.
    if (i_max is not None and j_max is not None):
        return [x_star_list[i_max], y_star_list[j_max]]
    else:
        return None



# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstrings above
# with the proper formatting. 

# Test all functions with three examples each. 

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