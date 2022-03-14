##########################################################################################
# Name: Daniel Taylor
# Date: 11/1/21
# Description: Comparing run time of two search methods
##########################################################################################
from plot import plot
import math as math

# a function that displays the table
def displayTable(list):
    print("n".ljust(8) + "Seq".ljust(8) + "Bin".ljust (8) + "Perf".ljust(8))
    print("".ljust(32, "-"))
    for index in range(len(list)):
        print(f"{list[index]}".ljust(8) + str(seqSearchComparisons(list[index])).ljust(8) + str(binSearchComparisons(list[index])).ljust(8) + str(math.trunc(seqSearchComparisons(list[index])/binSearchComparisons(list[index]))).ljust(8))


# a function that calculates the average number of comparisons of a sequential search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def seqSearchComparisons(vals):
    return (vals // 2)

# a function that calculates the maximum number of comparisons of a binary search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def binSearchComparisons(vals):
    return math.trunc((math.log(vals, 2) // 1) + 1)

###############################################
# MAIN PART OF THE PROGRAM
###############################################
# get user input for the minimum (make sure that it is >= 0)
while True:
    minVal = int(input("Minimum number of list items (>= 0)? "))
    if minVal < 0:
        print("*ERROR: Minimum must be >= 0!")
        minVal = int(input("Minimum number of list items (>= 0)? "))
    else:
        break

# get user input for the maximum (make sure that is is >= minimum)
while True:
    maxVal = int(input(f"Maximum number of list items (>= min ({minVal}))? "))
    if maxVal < minVal:
        print("*ERROR: Maximum must be >= minimum (100)! ")
        maxVal = int(input(f"Maximum number of list items (>= min ({minVal}))? "))
    else:
        break

# get user input for the interval (make sure that it is >= 1)
while True:
    interval = int(input("The interval between each row of the table (>= 1)? "))
    if interval < 1:
        print("*ERROR: Interval must be >= 1! ")
        interval = int(input("The interval between each row of the table (>= 1)? "))
    else:
        break

# generate the table
listValues = []
for x in range(minVal,maxVal + interval, interval):
    listValues.append(x)
displayTable(listValues)
