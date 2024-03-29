# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Megan Hoang
#
# Date: 4/23/2021
# 
##################################################
#
# Script for Assignment 8: 
# Databases
#
##################################################
"""
import os # To set working directory
import sqlite3
import csv
# import pandas as pd # To read and inspect data

# cities = pd.read_csv('c:/Users/megan/OneDrive/Desktop/US_cap_cities_pop.csv')
# states = pd.read_csv('c:/Users/megan/OneDrive/Desktop/US_state_pop_area.csv')

# Set our Directory
os.getcwd()
path = "C:\\Users\\megan\\OneDrive\\Desktop\\"
os.chdir(path)
os.getcwd()


# Question 1
# (a) Create the database
con = sqlite3.connect('population.db')
cur = con.cursor()

# (b) Create a table
cur.execute('CREATE TABLE Density(State TEXT, Population INTEGER, Land_Area REAL)')

# (c) Insert the data from the table above
open_file = open('US_state_pop_area.csv')
states = csv.reader(open_file)
cur.executemany('INSERT INTO Density VALUES (?, ?, ?)', states)
# cur.execute("INSERT INTO Density (State, Population, Land_Area) VALUES (?, ?, ?) ;", states)

# (d) Retrieve the contents of the table
cur.execute("SELECT * FROM Density")
cur.fetchall()

# (e) Retrieve the population
cur.execute("SELECT Population FROM Density")
for row in cur.fetchall():
 print(row)

# (f) Retrieve the states that have populations of less than one million
cur.execute('''SELECT State FROM Density WHERE Population < 1000000''')
for row in cur.fetchall():
  print(row)
  
# (g) Retrieve the states that have populations of less than one million or greater than five million
cur.execute('''SELECT State FROM Density
 WHERE Population < 1000000
 OR Population > 5000000''')
for row in cur.fetchall():
 print(row)
 
# (h) Retrieve the states that do not have populations of less than one million or greater than five million.
cur.execute('''SELECT State FROM Density
 WHERE NOT(Population < 1000000
 OR Population > 5000000)''')
for row in cur.fetchall():
 print(row)
 
# (i) Retrieve the populations of states that have a land area greater than 200,000 square miles
cur.execute('''SELECT State FROM Density
 WHERE Land_Area > 200000''')
for row in cur.fetchall():
 print(row)
 
 
# (j) Retrieve the states along with their population densities (population divided by land area).
cur.execute('SELECT State, Population / Land_Area FROM Density')
for row in cur.fetchall():
 print(row)



# Question 2
# Read in the file and create a new table
open_file = open("US_cap_cities_pop.csv")
cities = csv.reader(open_file)

cur.execute('CREATE TABLE Capitals(State TEXT, Capital TEXT, Area REAL, Population INTEGER)')
cur.executemany('INSERT INTO Capitals VALUES (?, ?, ?, ?)', cities)

# (a) Retrieve the contents of the table.
cur.execute("SELECT * FROM Capitals")
cur.fetchall()

# (b) Retrieve the populations of the states and capitals (in a list of tuples)
cur.execute('''SELECT Density.Population, Capitals.Population
 FROM Capitals INNER JOIN Density
 WHERE Capitals.State = Density.State''')
for row in cur.fetchall():
 print(row)

# (c) Retrieve the land area of the states whose capitals that have populations greater than 100,000.
cur.execute('''SELECT Density.Land_Area
 FROM Capitals INNER JOIN Density
 WHERE Capitals.State = Density.State
 AND Capitals.Population > 100000''')
for row in cur.fetchall():
 print(row)
 
# (d) Retrieve the states with land densities greater than ten people per square mile and capital city populations more than 500,000.
cur.execute('''SELECT Density.State
 FROM Capitals INNER JOIN Density
 WHERE Capitals.State = Density.State
 AND Density.State / Density.Land_Area < 2
 AND Capitals.State > 500000''')
for row in cur.fetchall():
 print(row)
 
# Should be density < 10

# (e) Retrieve the total land area of the US.
cur.execute('SELECT SUM(Land_Area) FROM Density')
print(cur.fetchone())

# (f) Retrieve the average population of the capital cities.
cur.execute('SELECT AVG(Population) FROM Capitals')
print(cur.fetchone())

# (g) Retrieve the lowest population of the capital cities.
cur.execute('SELECT MIN(Population) FROM Capitals')
print(cur.fetchone())

# (h) Retrieve the highest population of the states or territories.
cur.execute('SELECT MAX(Population) FROM Density')
print(cur.fetchone())

# (i) Retrieve the states that have land densities within 0.5 persons per square mile of one another.
# Have each pair of states reported only once.
cur.execute('''SELECT A.State, B.State
 FROM Density A INNER JOIN Density B
 WHERE A.State < B.State
 AND ABS(A.State / A.Land_Area - B.State / B.Land_Area) <
0.5''')
for row in cur.fetchall():
 print(row)

cur.execute('''SELECT A.State, A.Population / A.Land_Area AS PopDensity
 FROM Density A 
 ORDER BY PopDensity''')
for row in cur.fetchall():
 print(row)

# (j)  Revisit item (b) above: Retrieve the populations of the states and capitals (in a list of tuples
# of the form [state name, state population, capital population]), except modify the query as follows
 
# (j - i) List only the rows corresponding to states but not territories
cur.execute('''SELECT State, Population, Capitals.Population
 FROM Capitals''')
for row in cur.fetchall():
 print(row)
 
# This won't work without joining to Density


# (j - ii) List all rows corresponding to both states and territories. Leave any missing values as None.
cur.execute('''SELECT Density.State, Density.Population, Capitals.Population
 FROM Capitals INNER JOIN Density
 WHERE Capitals.State = Density.State''')
for row in cur.fetchall():
 print(row)

# This is the answer to 2ji.

# Q 2jii requires a left join. 




# The commit method saves the changes. 
con.commit()

# Close the connection when finished. 
con.close()
