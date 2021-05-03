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
# Script for Question 3
#
##################################################
"""

##################################################
# Import Required Modules
##################################################

# import name_of_module
import os # To set working directory
import sqlite3
import csv



##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
path = "C:\\Users\\megan\\OneDrive\\Desktop\\"
os.chdir(path)
os.getcwd()


#--------------------------------------------------
# Question 3, part a
#--------------------------------------------------


# Read the US roads data into Python.

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('CREATE TABLE Roads(State TEXT, Miles REAL, Speed_Limit REAL)')

open_file = open('US_state_roads.csv')
roads = csv.reader(open_file)
cur.executemany('INSERT INTO Roads VALUES (?, ?, ?)', roads)



#--------------------------------------------------
# Question 3, part b
#--------------------------------------------------


# List the states and speed limits 
# for the states with speed limits greater than or equal to 75 mph. 


cur.execute('''SELECT State FROM Roads WHERE Speed_Limit >= 75''')
for row in cur.fetchall():
  print(row)


#--------------------------------------------------
# Question 3, part c
#--------------------------------------------------

# i. Calculate the average length of road miles across all states. 

cur.execute('SELECT AVG(Miles) FROM Roads')
print(cur.fetchone())


# ii. Calculate the average length of road miles 
# for the states with speed limits greater than or equal to 75 mph. 

cur.execute('SELECT AVG(Miles) FROM Roads WHERE Speed_Limit >= 75')
print(cur.fetchone())


#--------------------------------------------------
# Question 3, part d
#--------------------------------------------------

# Read in the Density data from Assignment 8.


# (b) Create a table
cur.execute('CREATE TABLE Density(State TEXT, Population REAL, Land_Area REAL)')

# (c) Insert the data from the table above
open_file = open('US_state_pop_area.csv')
states = csv.reader(open_file)
cur.executemany('INSERT INTO Density VALUES (?, ?, ?)', states)
# cur.execute("INSERT INTO Density (State, Population, Land_Area) VALUES (?, ?, ?) ;", states)



#--------------------------------------------------
# Question 3, part e
#--------------------------------------------------


# i. Calculate a list of the state names 
# and the number of lane miles per person. 
# List them in increasing order from highest to lowest 
# lane miles per person.


cur.execute('''SELECT Density.State, (Roads.Miles / Density.Population)
 FROM Roads INNER JOIN Density
 WHERE Roads.State = Density.State
 ORDER BY (Roads.Miles / Density.Population) ASC ''')
for row in cur.fetchall():
 print(row)


# ii. Calculate a list of the state names 
# and the number of lane miles per square mile of land area. 
# List them in increasing order from highest to lowest 
# lane miles per square mile.


cur.execute('''SELECT Density.State, (Roads.Miles / Density.Land_Area)
 FROM Roads INNER JOIN Density
 WHERE Roads.State = Density.State
 ORDER BY (Roads.Miles / Density.Land_Area) ASC''')
for row in cur.fetchall():
 print(row)


# The commit method saves the changes. 
con.commit()

# Close the connection when finished. 
con.close()



##################################################
# End
##################################################



