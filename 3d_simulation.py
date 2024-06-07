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
pre_angle    = 0
camera_angle = 0

tile_space = (25, 25)

coluna = pygame.Surface((4, 30))
coluna.fill( (255, 255, 255) )

arvore = pygame.image.load('tree.png')
esqueleto = pygame.image.load('skeleton.png')

def distanciate_image(image, distance):
	size = image.get_size()
	return pygame.transform.scale(
		image,
		(
			screen_size[0]* ((math.atan(size[0]/distance)*180/math.pi)/120),
			screen_size[1]* ((math.atan(size[1]/distance)*180/math.pi)/ 60),
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

tree_map = [[0 for i in range(10)] for j in range(10)]
for i in range(10)[::2]:
	for j in range(10)[::2]:
		tree_map[i][j] = 1

skt_map  = [[0 for i in range(10)] for j in range(10)]
skt_map[7][3] = 1

maps = {
	arvore: tree_map,
	esqueleto: skt_map,
}

def render_multimap(dicio, tam):
	for y in range(tam[1])[::-1]:
		for x in range(tam[0]):
			for img, map in dicio.items():
				if map[y][x]: blit_image(img, (x-tam[0]/2)*tile_space[0] -camera_posx, y*tile_space[1] -camera_posy)

def blit_map(map, img):
	for y in range(len(map))[::-1]:
		for x in range(len(map[y])):
			if map[y][x]: blit_image(img, (x-2)*25 -camera_posx, (y)*25 -camera_posy)

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

	render_multimap(maps, (10, 10))

	pygame.display.flip()
	screen.fill( (0, 0, 0) )
