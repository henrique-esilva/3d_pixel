import pygame, sys, math
from pygame.locals import *

pygame.init()

screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size)
abertura_camera = (60, 60)

camera_posx  = 0
camera_posy  = 0
pre_angle    = 0
camera_angle = 0

tile_space = (50, 50)

coluna = pygame.Surface((4, 30))
coluna.fill( (255, 255, 255) )

arvore = pygame.image.load('./tree.png')

def distanciate_image(image, distance):
	size = image.get_size()
	return pygame.transform.scale(
		image,
		(
			(screen_size[0]/abertura_camera[0])* math.atan(size[0]/distance)*180/math.pi,
			(screen_size[1]/abertura_camera[1])* math.atan(size[1]/distance)*180/math.pi,
		)
	)

def get_horizontal_paralax( x, y ):
	return (x/y) * screen_size[0]

def blit_image( image, posx, posy ):

	distance = ( posx**2 + posy**2 ) ** (1/2)
	observated_angle = math.atan2(posy, posx)
	total_angle = camera_angle + observated_angle

	if distance == 0:
		#print('null distance')
		return 0

	posx = distance * math.cos(total_angle)
	posy = distance * math.sin(total_angle)

	if posy <= 0.01: return 0#print('posy null'); return 0
	distanciated_image = distanciate_image(image, distance)
	size = distanciated_image.get_size()
	screen.blit(
		distanciated_image,
		(
			screen_size[0]/2 -size[0]/2 +get_horizontal_paralax(posx, posy),
			screen_size[1]/2 -size[1]/2
		)
	)

map = [[1 for i in range(5)] for j in range(5)]

def get_real_coordinates( x, y ):
	return ( (x-2)*tile_space[0], y*tile_space[1] )

def get_distance_to_camera( coord ):
	# give real coordinates! without camera_pos discount
	return ( (coord[0]-camera_posx)**2 + (coord[1]-camera_posy)**2 )**0.5

def create_dict_distance_to_coordinate( map ):
	distance_coordinate = {}
	for y in range(len(map)):
		for x in range(len(map[y])):
			distance_coordinate[( get_distance_to_camera( get_real_coordinates(x, y) ), (x,y) )] = (x, y)
	return ( sorted(distance_coordinate.keys())[::-1], distance_coordinate )

def blit_map_according_distance(map, img):
	keys, dicio = create_dict_distance_to_coordinate(map)
	for i in keys:
		if map[ dicio[i][1] ][ dicio[i][0] ]:
			blit_image(arvore, (dicio[i][0]-2)*tile_space[0] -camera_posx, (dicio[i][1])*tile_space[1] -camera_posy)

def blit_map( map, img ):
	for y in range(len(map))[::-1]:
		for x in range(len(map[y])):
			#if map[y][x]: blit_image(arvore, d*math.cos(camera_angle) - camera_posx, d*math.sin(camera_angle) - camera_posy)
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

	if pressed_keys[K_e]:     pre_angle += 1/64
	if pressed_keys[K_q]:     pre_angle -= 1/64
	pre_angle = pre_angle % 2
	camera_angle = pre_angle * math.pi

	#print("%43.0f" % (pre_angle*180))

	blit_map_according_distance(map, arvore)

	#blit_map(map, arvore)

	#blit_image(arvore, (0 - camera_posx)*math.cos(camera_angle), (0 - camera_posy)*math.sin(camera_angle) )

	

	pygame.display.flip()
	screen.fill( (0, 0, 0) )
