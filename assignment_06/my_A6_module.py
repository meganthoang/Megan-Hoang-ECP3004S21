# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Megan Hoang
#
# Date: March 20, 2021
# 
##################################################
#
# Sample Script for Assignment 6: 
# Function Definitions
#
##################################################
"""


"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for the script my_A6_tests.py.
##################################################
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module



##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1
def z_squared_diff(x: float, z: float) -> float:
    """    
    Returns the value x^2 − z
    >>> z_squared_diff(2, 1)
    3
    >>> z_squared_diff(19, 3)
    358
    >>> z_squared_diff(4, 8)
    8
    """
    return (x ** 2) - z


# Exercise 2
def sqrt_z_bisect(z: float, a_0: float, b_0: float, num_iter: float) -> float:
    """    
    Calculates the square root of z using the bisection method.
    >>> sqrt_z_bisect(7, 10, 10, 1)
    10.0
    >>> sqrt_z_bisect(19, 6, 2, 4)
    4.375
    >>> sqrt_z_bisect(4, 8, 12, 3)
    11.75
    """
    a = a_0
    b = b_0
    for i in range(num_iter):
        m = (a + b) / 2.0
        if z_squared_diff(m, z) * z_squared_diff(a, z) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2.0


# Exercise 3
def z_squared_diff_prime(x: float, z: float) -> float:
    """    
    Returns the derivative of x^2 − z
    >>> z_squared_diff_prime(2, 1)
    4
    >>> z_squared_diff_prime(19, 3)
    38
    >>> z_squared_diff_prime(4, 8)
    8
    """
    return 2 * x;


# Exercise 4
def sqrt_z_newton(z: float, x0: float, tol: float, num_iter: float) -> float:
    """    
    Uses Newton's method to find the square root of z
    >>> sqrt_z_newton(8, 2, 1, 10)
    Warning: Maximum number of iterations has been reached
    3.0
    >>> sqrt_z_newton(10, 20, 3, 5)
    Warning: Maximum number of iterations has been reached
    10.25
    >>> sqrt_z_newton(16, 12, 4, 8)
    Warning: Maximum number of iterations has been reached
    6.666666666666667
    """
    f = z_squared_diff(x0, z)
    if abs(f) < tol:
        return x0
    x = x0
    for i in range(num_iter):
        x1 = x - (z_squared_diff(x, z)) / (z_squared_diff_prime(x, z))
        x = x1
        f = z_squared_diff(x1, z)
        if abs(f) < tol:
            return x1
        print("Warning: Maximum number of iterations has been reached")
        return x1

# Exercise 5
def z_squared_mid(x: float, z: float) -> float:
    """    
    Finds the root of a function using the fixed-point method.
    >>> z_squared_mid(2, 1)
    0.5
    >>> z_squared_mid(19, 3)
    1.5
    >>> z_squared_mid(4, 8)
    4.0
    """
    return (1/2) * ((z/x) * x)


# Exercise 6
def sqrt_z_fixed(z: float, x0: float, tol: float, num_iter: float) -> float:
    """    
    Uses the fixed-point method to find the square root of z
    >>> sqrt_z_fixed(8, 2, 1, 10)
    Warning: Maximum number of iterations has been reached
    3.0
    >>> sqrt_z_fixed(10, 20, 3, 5)
    Warning: Maximum number of iterations has been reached
    10.25
    >>> sqrt_z_fixed(16, 12, 4, 8)
    Warning: Maximum number of iterations has been reached
    6.666666666666667
    """
    f = z_squared_mid(x0, z)
    if abs(f-x0) < tol:
        return x0
    x = x0
    for i in range(num_iter):
        x1 = z_squared_mid(x, z)
        f = z_squared_mid(x1, z)
        if abs(f-x1) < tol:
            return x1
        x = x1
        print("Warning: Maximum number of iterations has been reached")
        return x1
    


# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstrings
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# The tests are implemented below -- but only
# when the script is run, not when it is imported. 


if __name__ == "__main__":
    import doctest
    doctest.testmod()

##################################################
# End
##################################################