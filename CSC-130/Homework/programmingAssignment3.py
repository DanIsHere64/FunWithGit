###########################################################################################
# Name: Daniel Taylor
# Date: 10/13/21 
# Description: Performs statistical analysis with user-defined functions instead of python's
# built in math functions
###########################################################################################

# function that prompts the user to enter an integer and returns it
def getNumber():
    return input("Enter an integer: ")

# function that sorts a set of three integers and puts them in a list

def sortNumbers(a, b, c):
    if a == b == c:
        sortedList = [a, b, c]
    elif a == b < c:
        sortedList = [a, b, c]
    elif a == c < b:
        sortedList = [a, c, b]
    elif b == c < a:
        sortedList = [b, c, a]
    elif a == b > c:
        sortedList = [c, a, b]
    elif a == c > b:
        sortedList = [b, a, c]
    elif c == b > a:
        sortedList = [a, b, c]
    elif a < b < c:
        sortedList = [a, b, c]
    elif a < c < b:
        sortedList = [a, c, b]
    elif b < a < c:
        sortedList = [b, a, c]
    elif b < c < a:
        sortedList = [b, c, a]
    elif c < a < b:
        sortedList = [c, a, b]
    elif c < b < a:
        sortedList = [c, b, a]
    return sortedList

# function that receives three integers as parameters and returns the minimum of the three

def minimum(sortedList):
    return sortedList[0]

# function that receives three integers as parameters and returns the maximum of the three

def maximum(sortedList):
    return sortedList[2]

# function that receives three integers as parameters, and calculates and returns the mean

def average(sortedList):
    return (sortedList[0] + sortedList[1] + sortedList[2])/3

# function that receives three integers as parameters, and calculates and returns the median

def median(sortedList):
    return sortedList[1]

# function that receives three integers as parameters, and calculates and returns the mode

def mode(sortedList):
    if sortedList[0] != sortedList[1] and sortedList[1] != sortedList[2] and sortedList[0] != sortedList[2]:
        return "undefined"
    elif sortedList[1] == sortedList[0] == sortedList[2]:
        return sortedList[0]
    elif sortedList[0] == sortedList[1] or sortedList[1] == sortedList[2]:
        return sortedList[1]

# function that receives three integers as parameters, and calculates and returns the range

def getRange(sortedList):
    return sortedList[2] - sortedList[0]

###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# get three integers from the user

int1 = int(getNumber())
int2 = int(getNumber())
int3 = int(getNumber())

# sort the numbers and enter them into a list

sortedList = sortNumbers(int1, int2, int3)

# determine and display the minimum value

print(f"The minimum value is {minimum(sortedList)}.")

# determine and display the maximum value

print(f"The maximum value is {maximum(sortedList)}.")

# calculate and display the mean

print(f"The mean is {average(sortedList)}.")

# calculate and display the median

print(f"The median is {median(sortedList)}.")

# calculate and display the mode

print(f"The mode is {mode(sortedList)}.")

# calculate and display the range

print(f"The range is {getRange(sortedList)}.")