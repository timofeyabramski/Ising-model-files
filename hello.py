#!/usr/bin/env python

class bikes:
	'common base class for bikes'
	bikecount = 0

	def _init_(self, name, cost):
		self.name = name
		self.cost = cost
		bikes.bikecount += 1

	def displayCount(self):
		print "Total number of bikes %d" % self.bikecount

	def displayCount(self):
		print "Name : ", self.name, ", cost: ", self.cost

"This would create first object of bikes class"
bike1 = bikes("Trek Madone", 2000)

"This would create a second object of bikes class"
bike2 = bikes("Cube Agree", 2400)




