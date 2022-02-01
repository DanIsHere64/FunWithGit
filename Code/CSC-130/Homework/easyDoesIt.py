##################################################################################################
# Name: Daniel Taylor
# Date: 10/4/21
# Description: Takes input for a user's name and their age. Then, it prints their name and their
#              age doubled
##################################################################################################

# prompt the user for a name and an age
name = input("Please enter your name: ")
age = input(f"How old are you, {name}? ")

# display the final output
print(f"Hi, {name}. You are {age} years old. Twice your age is {2 * int(age)}.")