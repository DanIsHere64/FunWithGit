######################################################################################################################
# Name: Daniel Taylor
# Date: 12/15/21
# Description: Compares sortiung algorithms based on their number of comparisons and swaps
######################################################################################################################

def getList():
#	return [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]
#	return [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]
	return [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]
#	return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#	return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#	return [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]

# the bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def bubble_sort(the_list):
    n = len(the_list)
    comparisons = 0
    swaps = 0
    # Pass through the list n - 1 times
    for i in range(1, n):

        # Go from the first item to the last unsorted item. 
        for j in range(1, n - i + 1):
            comparisons += 1
            if the_list[j] < the_list[j-1]:
                temp = the_list[j-1]
                the_list[j-1] = the_list[j]
                the_list[j] = temp
                swaps += 1
    return comparisons, swaps

# the optimized bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def optimized_bubble_sort(the_list):
    n = len(the_list)
    comparisons = 0
    swaps = 0

    # Pass through the list n - 1 times
    for i in range(1, n):
        swapped = False
        # Go from the first item to the last unsorted item. 
        for j in range(1, n - i + 1):
            comparisons += 1
            if the_list[j] < the_list[j-1]:
                temp = the_list[j-1]
                the_list[j-1] = the_list[j]
                the_list[j] = temp
                swapped = True
                swaps += 1
        if swapped == False:
            break
    return comparisons, swaps

# the selection sort function
# input: a list of integers
# output: a number of comparisons and swaps
def selection_sort(the_list):
    n = len(the_list)
    comparisons = 0
    swaps = 0
    for i in range(n-1):
        min_index = i # index of the smallest item
        for j in range(i+1, n):  # sequential search for smallest item
            comparisons += 1
            if the_list[j] < the_list[min_index]:
                min_index = j
                
        temp = the_list[i]
        the_list[i] = the_list[min_index]
        the_list[min_index] = temp
        swaps += 1
    return comparisons, swaps

# the insertion sort function
# input: a list of integers
# output: a number of comparisons and swaps
def insertion_sort(the_list):
    n = len(the_list)
    i = 1
    comparisons = 0
    swaps = 0
    while i < n:
        comparisons += 1
        if the_list[i-1] > the_list[i]:
            temp = the_list[i]  # don't erase current item from memory
            j = i - 1
            comparisons += 1
            # shift each item to the right that needs to be shifted
            while j >= 0 and the_list[j] > temp:    # repeat?
                the_list[j+1] = the_list[j] #shift
                j -= 1                  # move down
                the_list[j+1] = temp    # place temp
                swaps += 1
                comparisons += 1
        i += 1
    return comparisons, swaps

bubble = bubble_sort(getList())
optimized = optimized_bubble_sort(getList())
selection = selection_sort(getList())
insertion = insertion_sort(getList())

# the main part of the program
plot(bubble, optimized, selection, insertion)