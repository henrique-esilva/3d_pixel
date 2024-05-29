import pygame, sys, math
from pygame.locals import *

pygame.init()

def distanciate_image(image, distance, screen_size):
	size = image.get_size()
	return pygame.transform.scale(
		image,
		(
			(screen_size[0]/60)* math.atan(size[0]/distance)*180/math.pi,
			(screen_size[1]/60)* math.atan(size[1]/distance)*180/math.pi,
		)
	)

def get_horizontal_paralax( x, y ):
	return x/y

def blit_image(image, posx, posy, screen, screen_size):
	distance = ( posx**2 + posy**2 ) ** (1/2)
	if posy <= 0: return 0
	distanciated_image = distanciate_image(image, distance, screen_size)
	size = distanciated_image.get_size()
	screen.blit(
		distanciated_image,
		(
			screen_size[0]/2 -size[0]/2 +get_horizontal_paralax(posx*500, posy),
			screen_size[1]/2 -size[1]/2
		)
	)

