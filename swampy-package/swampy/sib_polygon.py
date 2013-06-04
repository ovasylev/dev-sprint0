# Polygon excercise from Week 0

# Name: Olha Vasylevska


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

# This is where you put code to move bob

#-------------- square() function:-----------

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)

bob.delay=0.01
square(bob, 150)

#-------------- polygon() function:----------

def polygon(t, length, n):
	for i in range(n):
		fd(t, length)
		lt(t, 360/n)
		
bob.delay=0.01		
polygon(bob, 45, 11)

#-------------- circle() function:-----------

import math

def circle(t, r, n):
	circ = 2 * math.pi * r
	length = circ/n
	polygon(t, length, n)
	
bob.delay=0.01		
circle(bob, 75, 40)

#-------------- arc() function:---------------

# s - the length of the arc
# n - number of segments
# seg_angle - the angle between segments

def arc(t, r, theta):
	s=(float(theta)/180)*math.pi*r
	n=int(s)+1
	seg_angle=float(theta)/n

	for i in range(n):
		fd(t, 1)
		lt(t, seg_angle)

bob.delay=0.01

# call the arc() function
arc(bob, 80, 90)


wait_for_user()					
