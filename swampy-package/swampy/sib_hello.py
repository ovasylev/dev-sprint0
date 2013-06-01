# Hello excercise from Week 0

# Name: Olha Vasylevska


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob


def h(t, dist):
	rt(t)
	fd(t, dist)
	pu(t)
	bk(t, dist/2)
	lt(t)
	pd(t)
	fd(t, dist*0.4)
	lt(t)
	pu(t)
	fd(t, dist/2)
	pd(t)
	bk(t, dist)
	pu(t)
	fd(t, dist)
	rt(t)
	fd(t, dist*0.15)
	pd(t)

def e(t, dist):
	rt(t)
	fd(t, dist)
	lt(t)
	fd(t, dist*0.4)
	pu(t)
	lt(t)
	fd(t, dist/2)
	pd(t)
	lt(t)
	fd(t, dist*0.4)
	pu(t)
	rt(t)
	fd(t, dist/2)
	pd(t)
	rt(t)
	fd(t, dist*0.4)
	pu(t)
	fd(t, dist*0.15)
	pd(t)

def l(t, dist):
	rt(t)
	fd(t, dist)
	lt(t)
	fd(t, dist*0.4)
	lt(t)
	pu(t)
	fd(t, dist)
	rt(t)
	fd(t, dist*0.15)
	pd(t)

def o(t, dist):
	rt(t)
	fd(t, dist)
	lt(t)
	fd(t, dist*0.4)
	lt(t)
	fd(t, dist)
	rt(t)
	bk(t, dist*0.4)
	pu(t)
	fd(t, dist*0.4)
	fd(t, dist*0.15)
	pd(t)

h(bob, 50)
e(bob, 50)
l(bob, 50)
l(bob, 50)
o(bob, 50)



wait_for_user()					
