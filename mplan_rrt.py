#Implementing Rapidly Exploring Random Trees for Motion Planning

import random
from math import sqrt, atan2, cos, sin 		#Importing important trigonometric maths functions
import pygame, sys
from pygame.locals import *


def intialize_pygame(config_space_x, config_space_y):				#Setup the pygame environment and ensure returning all created 
	pygame.init()													# terms
	window_size = [int(config_space_x), int(config_space_y)]
	sc = pygame.display.set_mode(window_size)
	pygame.display.set_caption('Rapidly Exploring Random Trees -  Akshay Kumar')
	wh = 255, 240, 200
	re = 255,0,0
	black = 20, 20, 40
	sc.fill(black)
	return sc, wh, re


def main(config_space_x, config_space_y, x_init, y_init, step_size, num_nodes=5000, x_goal=0, y_goal=0):
	count = num_nodes					# Number of nodes to be created
	#Initialize the pygame screen
	screen, white, red = intialize_pygame(config_space_x, config_space_y)		# Extract the pygame surface and the colours 
	# pygame.draw.line(screen, red, (x_goal, y_goal), (x_init, y_init))
	Tau = []
	Tau.append(tuple((x_init, y_init)))											# Create the list containing the coordinates of the 
																				# nodes are tuples
	while count<10000:
		x_rand, y_rand = random.random() * config_space_x, random.random() * config_space_y		# Random Point generation 
		x_nn, y_nn = Tau[0][0], Tau[0][1]
		# print ("random", x_rand, y_rand)
		for i in range(0, len(Tau)):
			dist_rho = sqrt((Tau[i][0]-x_rand)**2 + (Tau[i][1]-y_rand)**2)
			dist_pho = sqrt((x_nn-x_rand)**2 + (y_nn-y_rand)**2 )				# Calculating the distance between the random point
																				# and each existing node 
			if dist_rho<=dist_pho:
				minn = dist_rho
				x_nn, y_nn = Tau[i][0], Tau[i][1]								# Deciding the nerest node to the random point
		# print ("minn", minn)	
		# print("step", step_size)
		if  minn<=step_size:
			x_new, y_new = float(format(x_rand, '0.2f')),  float(format(y_rand, '0.2f'))				# Deciding the new node to		
		else:																							# either be the new random 			
			x_new = float(format(step_size*cos(atan2((y_rand-y_nn),(x_rand- x_nn))) + x_nn, '0.2f'))	# point or a single step point
			y_new = float(format(step_size*sin(atan2((y_rand-y_nn),(x_rand- x_nn))) + y_nn, '0.2f'))	# in its direction
			print ("-------------------------I am here ------------------------------")
		print ("xnew and ynew", x_new, y_new)	
		Tau.append(tuple((x_new, y_new)))										# Adding the new node to the list of existing nodes	
		dist_to_goal = sqrt((x_new - x_goal)**2 + (y_new - y_goal)**2)				
		if (dist_to_goal<step_size):
			pygame.draw.line(screen, red, (x_goal, y_goal), (x_new, y_new))
		count = count + 1
		minn=0	
		pygame.draw.line(screen, white, (x_nn, y_nn), (x_new, y_new))
		# pygame.draw.line(screen, red, (x_new, y_new), (x_new, y_new), 10)		# Visualisation of the random tree
		pygame.display.update()
		# print (x_rand, y_rand) 
		for e in pygame.event.get():
			if e.type ==QUIT or (e.type ==KEYUP and e.type == K_ESCAPE):
				sys.exit("Leaving")
	# print ("Tau", Tau)

if __name__ == '__main__':
    main(1000,800,500,400,8,5000, 750, 620)



