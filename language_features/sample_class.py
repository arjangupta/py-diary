"""
	Created by Arjan Gupta on 3/26/2018
	Description: Script to show specimen python class
"""

class Animal(object):
	def __init__(self, name):
		self.name = name

print "We created a Animal class instance - a zebra."
zebra = Animal("Marty")
print  "The name of this zebra is", zebra.name