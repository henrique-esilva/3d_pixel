from functions import *

pygame.init()

screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size)

camera_posx = 0
camera_posy = 0

coluna = pygame.Surface((4, 30))
coluna.fill( (255, 255, 255) )

arvore = pygame.image.load('./arvore1.png')

map = [[1 for i in range(10)] for j in range(10)]

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
			if map[y][x]: blit_image(arvore, (x-5)*50 -camera_posx, (y)*50 -camera_posy, screen, screen_size)

	pygame.display.flip()
	screen.fill( (0, 0, 0) )
