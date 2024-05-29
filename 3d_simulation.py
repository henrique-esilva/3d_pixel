import pygame, sys, math
from pygame.locals import *

pygame.init()

screen_size = (800, 400)
screen = pygame.display.set_mode(screen_size)

#quadrado = pygame.Surface((10, 10))
#quadrado.fill( (255, 0, 0) )
#distancia_quadrado = 2
#horizontal_quadrado = 0

camera_posx = 0
camera_posy = 0

coluna = pygame.Surface((4, 30))
coluna.fill( (255, 255, 255) )

arvore = pygame.image.load('./arvore1.png')

def distanciate_image(image, distance):
	size = image.get_size()
	return pygame.transform.scale(
		image,
		(
			(screen_size[0]/120)* math.atan(size[0]/distance)*180/math.pi,
			(screen_size[1]/60)* math.atan(size[1]/distance)*180/math.pi,
		)
	)

def get_horizontal_paralax( x, y ):
	return x/y

def blit_image(image, posx, posy):
	distance = ( posx**2 + posy**2 ) ** (1/2)
	if posy <= 0: return 0
	distanciated_image = distanciate_image(image, distance)
	size = distanciated_image.get_size()
	screen.blit(
		distanciated_image,
		(
			screen_size[0]/2 -size[0]/2 +get_horizontal_paralax(posx*500, posy),
			screen_size[1]/2 -size[1]/2
		)
	)

map = [[1 for i in range(5)] for j in range(5)]

def blit_map(map, img):
	for y in range(len(map))[::-1]:
		for x in range(len(map[y])):
			if map[y][x]: blit_image(arvore, (x-2)*50 -camera_posx, (y)*50 -camera_posy)

clock = pygame.time.Clock()
while True:
	clock.tick(24)
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			sys.exit()

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[K_RIGHT]: camera_posx += 1
	if pressed_keys[K_LEFT]:  camera_posx -= 1
	if pressed_keys[K_UP]:    camera_posy += 1
	if pressed_keys[K_DOWN]:  camera_posy -= 1

	for y in range(len(map))[::-1]:
		for x in range(len(map[y])):
			if map[y][x]: blit_image(arvore, (x-2)*50 -camera_posx, (y)*50 -camera_posy)

	pygame.display.flip()
	screen.fill( (0, 0, 0) )
