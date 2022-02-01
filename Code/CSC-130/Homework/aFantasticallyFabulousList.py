###########################################################################################
# Name: Daniel Taylor
# Date: 12/27/21
# Description: List manipulation
###########################################################################################

# function that:
def fillList():
    listLength = int(input("How many integers would you add to the list? ")) # (1) prompts the user for a list size
    list = []
    while listLength > 0: # (2) prompts the user for the integers to store in the list (corresponding to the list size)
        list.append(int(input("Enter and integer: ")))   # (3) creates the list
        listLength -= 1  
    return list       # (4) returns the list

# sorting algorithm
def sortList(list):
    doRepeat = False
    index = 1
    for _ in list:
        if index < len(list) and list[index] < list[index - 1]:
            i = list.pop(index)
            list.insert(index - 1, i)
            doRepeat = True
        index += 1
    if doRepeat == True:
        sortList(list)

###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################


# create the list
nums = fillList()

#sorts the list
sortedNums = []
for x in nums:
    sortedNums.append(x)
sortList(sortedNums)

# reverse list
reverseList = []
for x in nums:
    reverseList.insert(0, x)

# display information about the list using the list functions discussed in class
print(f"The original list: {nums}")
print(f"The length of the list is {len(nums)}.")
print(f"The minimum value in the list is {sortedNums[0]}.")
print(f"The maximum value in the list is {sortedNums[len(sortedNums) - 1]}.")
print(f"The reversed list: {reverseList}")
print(f"The sorted list: {sortedNums}")