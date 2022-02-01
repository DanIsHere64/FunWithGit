###########################################################################################
# Name: Daniel Taylor
# Date: 10/20/2021
# Description: Re-write a function recursively instead of iteratively
###########################################################################################

# the algorithm implemented iteratively
def passSomeBeers(bottles):
	while (bottles > 0):
		print("{} bottles of beer on the wall.".format(bottles))
		print("{} bottles of beer.".format(bottles))
		print("Take one down, pass it around.")
		bottles = bottles - 1
		print("{} bottles of beer on the wall.".format(bottles))
		print()

# the algorithm implemented recursively
def passSomeBeersRecursive(bottles):
	if bottles > 2:
		print("{} bottles of beer on the wall.".format(bottles))
		print("{} bottles of beer.".format(bottles))
		print("Take one down, pass it around.")
		bottles = bottles - 1
		print("{} bottles of beer on the wall.".format(bottles))
		passSomeBeersRecursive(bottles)
	elif bottles == 2:
		print("{} bottles of beer on the wall.".format(bottles))
		print("{} bottles of beer.".format(bottles))
		print("Take one down, pass it around.")
		bottles = bottles - 1
		print("{} bottle of beer on the wall.".format(bottles))
		passSomeBeersRecursive(bottles)
	elif bottles == 1:
		print("{} bottle of beer on the wall.".format(bottles))
		print("{} bottle of beer.".format(bottles))
		print("Take one down, pass it around.")
		bottles = bottles - 1
		print("{} bottles of beer on the wall.".format(bottles))

###############################################
# MAIN PART OF THE PROGRAM
###############################################
passSomeBeersRecursive(99)

