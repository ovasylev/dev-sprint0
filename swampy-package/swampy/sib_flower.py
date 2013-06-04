# Flower excercise (4.2) from Week 0

# Name:Olha Vasylevska


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

# This is where you put code to move bob

import math


def arc(t, r, theta):
	s=(float(theta)/180)*math.pi*r
	n=int(s)+1
	seg_angle=float(theta)/n

	for i in range(n):
		fd(t, 1)
		lt(t, seg_angle)


def petal(t, r, angle):
	for i in range(2):
		arc(t, r, angle)
		lt(t, 180-angle)

def flower(t, r, n, angle):
	for i in range(n):
		petal(t, r, angle)
		lt(t, 360.0/n)

bob.delay=0.01

flower(bob, 65, 7, 55)

pu(bob)
fd(bob, 150)
pd(bob)

flower(bob, 40, 10, 75)

pu(bob)
fd(bob, 150)
pd(bob)

flower(bob, 120, 20, 20)


wait_for_user()					