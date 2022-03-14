################################################################
# Name: Daniel Taylor
# Date: 12/08/21
# Description: Counts the number of zeroes written if a person were to 
# write out all the numbers between 1 and a user assigned number
################################################################

from time import time
import math as m

# This asks the ser for a value for it to count to and checks that it is greater than zero
endVal = int(input("What number do you want to count zeroes to? "))
if endVal < 1:
    print("Number must be greater than one.")
    endVal = int(input("What number do you want to count zeroes to? "))

# This counts the number of zeroes up to the given number using string storage
charCount = 0
startTimeChar = float(time())
for i in range(1, endVal + 1):
    x = str(i)
    for char in x:
        if char == "0":
            charCount += 1
endTimeChar = float(time())

# This is counts the number of zeroes up to the given number using mod to find the zeroes
mathCount = 0
startTimeMath = float(time())
for i in range(1, endVal + 1):
    while i > 0:
        if i % 10 == 0:
            mathCount += 1
        i = int(i/10)
endTimeMath = float(time())

# This calculates runtime for both algorithms and prints the amounts they returned with the runtimes
elapsedTimeChar = float(endTimeChar - startTimeChar)
elapsedTimeMath = float(endTimeMath - startTimeMath)
print(f"The number of zeroes written from 1 to {endVal} is {charCount}.")
print(f"This took {elapsedTimeChar} seconds using the string calculation.")
print(f"This took {elapsedTimeMath} seconds using the modulus function.")
