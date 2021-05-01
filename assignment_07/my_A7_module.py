# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Megan Hoang
#
# Date: 4/14/2021
# 
##################################################
#
# Sample Script for Assignment 7: 
# Function Definitions
#
##################################################
"""


##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1
def g(x: float) -> float:
    """Return the output of a function g(x) given x
    >>> g(6)
    1536
    >>> g(0)
    0
    >>> g(36)
    1767456
    """
    
    return (x-2)*x*(x+2)**2

def g_prime(x: float) -> float:
    """Return the first derivative of a function g(x) given x
    >>> g_prime(6)
    1024
    >>> g_prime(0)
    -8
    >>> g_prime(36)
    194104
    """
    
    return 4*x**3 + 6*x**2 - 8*x - 8


def g_2prime(x: float) -> float:
    """Return the second derivative of a function g(x) given x
    >>> g_2prime(6)
    496
    >>> g_2prime(0)
    -8
    >>> g_2prime(36)
    15976
    """
    
    return 4*(3*x**2 + 3*x - 2)


# Exercise 2
def newton_g_opt(x_0: float, maxiter: float, tol: float) -> float:
    """Return the second derivative of a function g(x) given x
    >>> newton_g_opt(20, 10, 5)
    2.0551046866861795
    >>> newton_g_opt(6, 10, 1)
    2.0019133364041592
    >>> newton_g_opt(1, 10, 0)
    1
    """
    x = x_0
    # if(g(x) < tol):
    #     return x
    for i in range(maxiter):
        # x1 = x - (g(x)/g_prime(x))
        x1 = x - (g_prime(x)/g_2prime(x))
        x = x1
        # if(g(x) < tol):
        if(abs(g_prime(x1)) < tol):
            return x1
    # return x_0 - g(x_0)/g_prime(x_0)




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