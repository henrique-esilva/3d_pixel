import pygame, sys
from pygame.locals import *
from math import sin, cos, pi, tan
import math

screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size)

white_dot = pygame.Surface((1,1))
white_dot.fill((255,255,255))

movx = 0
movy = 0
central_point = [200, 200]
radius = 64
pre_angle = 0

minus_plus = (K_MINUS, K_EQUALS)

def keys_increment(keys, k_set, root, rad=0.01):
	if keys[k_set[0]]:
		root -= rad
	if keys[k_set[1]]:
		root += rad
	return root

def increment(root, rad):
	return root + rad

map = [(i*30, j*30) for i in range(5) for j in range(5)]

timer_clock = pygame.time.Clock()
while True:
	timer_clock.tick(24)
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT: sys.exit()

	pressed_keys = pygame.key.get_pressed()

	pre_angle = keys_increment(pressed_keys, minus_plus, pre_angle)
	pre_angle = pre_angle % 2

	movx = keys_increment(pressed_keys, (K_LEFT, K_RIGHT), movx, 5)
	movy = keys_increment(pressed_keys, (K_UP,    K_DOWN), movy, 5)

	for point in map:
		diffx = point[0]-(central_point[0]+movx)
		diffy = point[1]-(central_point[1]+movy)
		distance = (diffx**2 + diffy**2) ** 0.5

		if distance != 0:

			point_cos = cos(math.acos( diffx/distance ) + pre_angle*pi)
			point_sin = sin(math.asin( diffy/distance ) + pre_angle*pi)

			screen.blit( white_dot, (
				distance *cos(pre_angle*pi) + central_point[0],
				distance *cos(pre_angle*pi) + central_point[1])
			)

			#screen.blit( white_dot, (
			#	distance *cos(pre_angle*pi) + central_point[0],
			#	distance *cos(pre_angle*pi) + central_point[1])
			#)
			#screen.blit( white_dot, ( distance *cos(pre_angle*pi), distance *sin(pre_angle*pi) )

			#screen.blit( white_dot, (
			#	(point[0]-movx *cos(pre_angle*pi))+central_point[0],
			#	(point[1]-movy *sin(pre_angle*pi))+central_point[1]))
			#screen.blit(white_dot, (central_point[0] + radius * sin(pre_angle*pi), central_point[1] + radius * cos(pre_angle*pi)))
		#screen.blit(white_dot, (central_point[0] + radius * sin(pre_angle*pi), central_point[1] + radius * cos(pre_angle*pi)))

	screen.blit(white_dot, central_point)

	pygame.display.flip()
	screen.fill( (0, 0, 0) )
