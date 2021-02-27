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
# Testing Script for Assignment 4:
# Testing Function Definitions with doctest
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


# Import doctest to test functions from docstring.
import doctest



##################################################
# Testing with doctest module
##################################################

# Use the doctest module to test the examples in the docstring

print("#" + 50*"-")
print("# Testing with doctest module")
print("#" + 50*"-")

# Run testmod to test examples in the docstrings
# of the functions in this module.
doc_out = doctest.testmod()
print(doc_out)


print("#" + 50*"-")


##################################################
# End
##################################################
