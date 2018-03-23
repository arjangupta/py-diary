"""
	Created by Arjan Gupta on 3/23/2018
	Description: A recursive positive integer factorial program for practice
"""

# Only calculates for positive integers
def calc_factorial(n):
	if n < 0: # bad input
		return "not computable because the number is negative"
	elif n == 0 or n == 1: # stop recursing when n is 1 or 0
		return 1
	else: # resursion rule
		return n * calc_factorial(n-1)

num = 5
print "The factorial of", num, "is", calc_factorial(num)