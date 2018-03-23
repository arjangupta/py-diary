"""
	Created by Arjan Gupta on 3/23/2018
	Description: A recursive positive integer factorial program for practice
"""

# Only calculates for positive integers
def calc_factorial(n):
	# Stop recursing when n is 1
	if n < 0:
		return "not computable because the number is negative"
	elif n == 0 or n == 1:
		return 1
	else:
		return n * calc_factorial(n-1)

num = 5
print "The factorial of", num, "is", calc_factorial(num)