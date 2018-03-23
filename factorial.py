"""
	Created by Arjan Gupta on 3/23/2018
	Description: A recursive positive integer factorial program for practice
"""

# Only calculates for positive integers
def calc_factorial(n):
	# Stop recursing when n is 1
	if n == 1:
		return n
	elif n <= 0:
		return "Factorial "

num = 5
print "The factorial of", num, "is", calc_factorial(num)