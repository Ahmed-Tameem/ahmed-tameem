"""
#Author: Ahmed Tameem
#Date: December 30, 2020
#Purpose: To rename a set of files in a folder
"""

from os import rename

NUMBER_OF_FILES = 10    #Number of files to be renamed

for number in range(1, NUMBER_OF_FILES + 1):
    rename("Lab_" + str(number) + ".m", "ELEC_341_Lab" + str(number) + ".m") #Rename the files to follow a new naming convention
