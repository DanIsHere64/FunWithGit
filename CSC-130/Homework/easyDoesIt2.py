###########################################################################################
# Name: Daniel Taylor
# Date: 10/8/21
# ###########################################################################################

# function that prompts the user for a name and returns it
def name():
    return input("Please enter your name: ")

# function that receives the user's name as a parameter, and prompts the user for an age and returns it
def age(name):
    return input(f"How old are you, {name}? ")

# function that receives the user's name and age as parameters and displays the final output
def prnt(name, age):
    print(f"Hi, {name}. You are {age} years old. Twice your age is {int(age) * 2}.")

###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# get the user's name
userName = name()

# get the user's age
userAge = age(userName)

# display the final output
prnt(userName, userAge)