# One source file is used to answer Question 1 and two source files are used to answer Question 3.
# The files are called Data.txt, AnimalData.txt and ColourData.txt
# A class declaration can be used to declare a record.
# A list is an alternative to an array.

# 1 A program reads data from a file and searches for specific data.
# (a) The main program needs to read 25 integer data items from the text file Data.txt into a
# local 1D array, DataArray

# (i) Write program code to declare the local array DataArray

DataArray = []

with open('Data.txt', 'r') as file:
    for line in file.readlines():
        print(line)
