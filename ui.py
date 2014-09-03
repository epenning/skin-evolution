import pygame,sys
import random
from pygame.locals import *
from neuralnetwork import *

pygame.init()

# FPS stuff, not really applicable
FPS = 1
FPSCLOCK = pygame.time.Clock()

# set up display
WINDOWSIZE = 344
DISPLAYSURF = pygame.display.set_mode((WINDOWSIZE * 2, WINDOWSIZE))
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

# set up neural network
net = NeuralNet()
net.createNet(3, 3, 2, 2)
popSize = 10
ga = GenAlg(popSize, net)

pop = ga.epochOne(Genome(net.getWeights(), 1, net.getFunctions()))
variety = 4

def main():
	
	global pop
	playing = True
	DISPLAYSURF.fill(WHITE)
	draw_interface()
	pygame.display.update()
	FPSCLOCK.tick(FPS)

	while playing == True:
		
		for event in pygame.event.get():
			if event.type == QUIT:
				playing = False
			if event.type == pygame.MOUSEBUTTONDOWN: # if user clicked on a texture
				mouse_pos = pygame.mouse.get_pos() # returns the (x, y) coordinate of mouse click
				texture_num = get_texture_number_click(mouse_pos) # returns which texture was clicked on (1-9)
				if(texture_num != -1):
					pop = ga.epochOne(pop[texture_num-1])
					DISPLAYSURF.fill(WHITE) # display
					draw_interface()
					pygame.display.update() # update frame
					FPSCLOCK.tick(FPS)
			elif event.type == pygame.KEYDOWN and save(event.key): # if user wants to save
				texture_num = get_texture_number_key(event.key) # get the corresponding texture based on user key input
				rect = get_rect(texture_num) # returns the rect object of selected texture
				sub = DISPLAYSURF.subsurface(rect)
				pygame.image.save(sub, "screenshot.png") # save selected texutre

	pygame.quit()
	sys.exit()

def save(key):
	return (key == pygame.K_1 or key == pygame.K_2 or key == pygame.K_3 or 
		key == pygame.K_4 or key == pygame.K_5 or key == pygame.K_6 or 
		key == pygame.K_7 or key == pygame.K_8 or key == pygame.K_9)

def get_texture_number_click(pos):
	if (pos[0] > 40 and pos[0] < 105 and pos[1] > 40 and pos[1] < 105):
		return 1
	elif (pos[0] > 140 and pos[0] < 205  and pos[1] > 40 and pos[1] < 105):
		return 2
	elif(pos[0] > 240 and pos[0] < 305 and pos[1] > 40 and pos[1] < 105):
		return 3
	elif(pos[0] > 40 and pos[0] < 105 and pos[1] > 140 and pos[1] < 205):
		return 4
	elif(pos[0] > 140 and pos[0] < 205  and pos[1] > 140 and pos[1] < 205):
		return 5
	elif(pos[0] > 240 and pos[0] < 305 and pos[1] > 140 and pos[1] < 205):
		return 6
	elif(pos[0] > 40 and pos[0] < 105 and pos[1] > 240 and pos[1] < 305):
		return 7
	elif(pos[0] > 140 and pos[0] < 205  and pos[1] > 240 and pos[1] < 305):
		return 8
	elif(pos[0] > 240 and pos[0] < 305 and pos[1] > 240 and pos[1] < 305):
		return 9
	else:
		return -1

def get_texture_number_key(key):
	if(key == pygame.K_1):
		return 1
	elif(key == pygame.K_2):
		return 2
	elif(key == pygame.K_3):
		return 3
	elif(key == pygame.K_4):
		return 4
	elif(key == pygame.K_5):
		return 5
	elif(key == pygame.K_6):
		return 6
	elif(key == pygame.K_7):
		return 7
	elif(key == pygame.K_8):
		return 8
	elif(key == pygame.K_9):
		return 9
	else:
		return -1
	
def get_rect(num_texture):
	if(num_texture == 1):
		return pygame.Rect(40, 40, 64, 64)
	elif(num_texture == 2):
		return pygame.Rect(140, 40, 64, 64)
	elif(num_texture == 3):
		return pygame.Rect(240, 40, 64, 64)
	elif(num_texture == 4):
		return pygame.Rect(40, 140, 64, 64)
	elif(num_texture == 5):
		return pygame.Rect(140, 140, 64, 64)
	elif(num_texture == 6):
		return pygame.Rect(240, 140, 64, 64)
	elif(num_texture == 7):
		return pygame.Rect(40, 240, 64, 64)
	elif(num_texture == 8):
		return pygame.Rect(140, 240, 64, 64)
	elif(num_texture == 9):
		return pygame.Rect(240, 240, 64, 64)
	else:
		return pygame.Rect(0, 0, 1, 1)

def draw_interface():
	global pop
	draw_texture(pop[0], ( 40,  40))  #1
	draw_texture(pop[1], (140,  40))  #2
	draw_texture(pop[2], (240,  40))  #3
	draw_texture(pop[3], ( 40, 140))  #4
	draw_texture(pop[4], (140, 140))  #5
	draw_texture(pop[5], (240, 140))  #6
	draw_texture(pop[6], ( 40, 240))  #7
	draw_texture(pop[7], (140, 240))  #8
	draw_texture(pop[8], (240, 240))  #9
	draw_help()

def draw_help():
	font = pygame.font.SysFont("freeansbold", 20)
	text = font.render("Click on a texture to evolve that texture.", 1, BLACK)
	text2 = font.render("Press 1-9 to save the corresponding image.", 1, BLACK)
	DISPLAYSURF.blit(text, (360, 40))
	DISPLAYSURF.blit(text2, (360, 65))

def draw_texture(genome, start):
	draw_head(genome, start)
	draw_hat(genome, start)
	draw_right_leg(genome, start)
	draw_body(genome, start)
	draw_right_arm(genome, start)
	draw_right_leg_2(genome, start)
	draw_jacket(genome, start)
	draw_right_arm_2(genome, start)
	draw_left_leg_2(genome, start)
	draw_left_leg(genome, start)
	draw_left_arm(genome, start)
	draw_left_arm_2(genome, start)

def draw_head(genome, start):
	# top
	net.putGenome(genome)
	for x in xrange(-4, 4):
		for y in xrange(-12, -4):
			colors = net.update([x,y,1*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 12 + x, start[1] + 12 + y, 1, 1),1)
	# bottom
	for x in xrange(-4, 4):
		for y in xrange(4, 12):
			colors = net.update([x,y,1*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 20 + x, start[1] + -4 + y, 1, 1),1)
	# right
	for x in xrange(4, 12):
		for y in xrange(-4, 4):
			colors = net.update([x,y,1*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + -4 + x, start[1] + 12 + y, 1, 1),1)
	# front
	for x in xrange(-4, 4):
		for y in xrange(-4, 4):
			colors = net.update([x,y,1*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 12 + x, start[1] + 12 + y, 1, 1),1)
	# left
	for x in xrange(-12, -4):
		for y in xrange(-4, 4):
			colors = net.update([x,y,1*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 28 + x, start[1] + 12 + y, 1, 1),1)
	# back
	for x in xrange(-4, 4):
		for y in xrange(-20, -12):
			colors = net.update([x,y,1*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 28 + x, start[1] + 28 + y, 1, 1),1)

def draw_hat(genome, start):
	net.putGenome(genome)
	# top
	for x in xrange(-4, 4):
		for y in xrange(-12, -4):
			colors = net.update([x,y,2*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 44 + x, start[1] + 12 + y, 1, 1),1)
	# bottom
	for x in xrange(-4, 4):
		for y in xrange(4, 12):
			colors = net.update([x,y,2*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 52 + x, start[1] + -4 + y, 1, 1),1)
	# right
	for x in xrange(4, 12):
		for y in xrange(-4, 4):
			colors = net.update([x,y,2*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 28 + x, start[1] + 12 + y, 1, 1),1)
	# front
	for x in xrange(-4, 4):
		for y in xrange(-4, 4):
			colors = net.update([x,y,2*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 44 + x, start[1] + 12 + y, 1, 1),1)
	# left
	for x in xrange(-12, -4):
		for y in xrange(-4, 4):
			colors = net.update([x,y,2*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 60 + x, start[1] + 12 + y, 1, 1),1)
	# back
	for x in xrange(-4, 4):
		for y in xrange(-20, -12):
			colors = net.update([x,y,2*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 60 + x, start[1] + 28 + y, 1, 1),1)

def draw_right_leg(genome, start):
	net.putGenome(genome)
	# top
	for x in xrange(-2, 2):
		for y in xrange(-10, -6):
			colors = net.update([x,y,3*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 6 + x, start[1] + 26 + y, 1, 1),1)
	# bottom
	for x in xrange(-2, 2):
		for y in xrange(6, 10):
			colors = net.update([x,y,3*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 10 + x, start[1] + 10 + y, 1, 1),1)
	# right
	for x in xrange(2, 6):
		for y in xrange(-6, 6):
			colors = net.update([x,y,3*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + -2 + x, start[1] + 26 + y, 1, 1),1)
	# front
	for x in xrange(-2, 2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,3*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 6 + x, start[1] + 26 + y, 1, 1),1)
	# left
	for x in xrange(-6, -2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,3*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 14 + x, start[1] + 26 + y, 1, 1),1)
	# back
	for x in xrange(6, 10):
		for y in xrange(-6, 6):
			colors = net.update([x,y,3*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 6 + x, start[1] + 26 + y, 1, 1),1)

def draw_body(genome,start):
	net.putGenome(genome)
	# top
	for x in xrange(-4, 4):
		for y in xrange(-10, -6):
			colors = net.update([x,y,4*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 24 + x, start[1] + 26 + y, 1, 1),1)
	# bottom
	for x in xrange(-4, 4):
		for y in xrange(6, 10):
			colors = net.update([x,y,4*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 32 + x, start[1] + 10 + y, 1, 1),1)
	# right
	for x in xrange(-8, -4):
		for y in xrange(-6, 6):
			colors = net.update([x,y,4*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 24 + x, start[1] + 26 + y, 1, 1),1)
	# front
	for x in xrange(-4, 4):
		for y in xrange(-6, 6):
			colors = net.update([x,y,4*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 24 + x, start[1] + 26 + y, 1, 1),1)
	# back
	for x in xrange(8, 16):
		for y in xrange(-6, 6):
			colors = net.update([x,y,4*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 24 + x, start[1] + 26 + y, 1, 1),1)
	# left
	for x in xrange(4, 8):
		for y in xrange(-6, 6):
			colors = net.update([x,y,4*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 24 + x, start[1] + 26 + y, 1, 1),1)

def draw_right_arm(genome, start):
	net.putGenome(genome)
	# top
	for x in xrange(-2, 2):
		for y in xrange(-10, -6):
			colors = net.update([x,y,5*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 46 + x, start[1] + 26 + y, 1, 1),1)
	# bottom
	for x in xrange(-2, 2):
		for y in xrange(6, 10):
			colors = net.update([x,y,5*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 50 + x, start[1] + 10 + y, 1, 1),1)
	# right
	for x in xrange(2, 6):
		for y in xrange(-6, 6):
			colors = net.update([x,y,5*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 38 + x, start[1] + 26 + y, 1, 1),1)
	# front
	for x in xrange(-2, 2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,5*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 46 + x, start[1] + 26 + y, 1, 1),1)
	# left
	for x in xrange(-6, -2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,5*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 54 + x, start[1] + 26 + y, 1, 1),1)
	# back
	for x in xrange(6, 10):
		for y in xrange(-6, 6):
			colors = net.update([x,y,5*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 46 + x, start[1] + 26 + y, 1, 1),1)

def draw_right_leg_2(genome, start):
	net.putGenome(genome)
	# top
	for x in xrange(-2, 2):
		for y in xrange(-10, -6):
			colors = net.update([x,y,6*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 6 + x, start[1] + 42 + y, 1, 1),1)
	# bottom
	for x in xrange(-2, 2):
		for y in xrange(6, 10):
			colors = net.update([x,y,6*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 10 + x, start[1] + 26 + y, 1, 1),1)
	# right
	for x in xrange(2, 6):
		for y in xrange(-6, 6):
			colors = net.update([x,y,6*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + -2 + x, start[1] + 42 + y, 1, 1),1)
	# front
	for x in xrange(-2, 2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,6*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 6 + x, start[1] + 42 + y, 1, 1),1)
	# left
	for x in xrange(-6, -2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,6*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 14 + x, start[1] + 42 + y, 1, 1),1)
	# back
	for x in xrange(6, 10):
		for y in xrange(-6, 6):
			colors = net.update([x,y,6*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 6 + x, start[1] + 42 + y, 1, 1),1)

def draw_jacket(genome, start):
	net.putGenome(genome)
	# top
	for x in xrange(-4, 4):
		for y in xrange(-10, -6):
			colors = net.update([x,y,7*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 24 + x, start[1] + 42 + y, 1, 1),1)
	# bottom
	for x in xrange(-4, 4):
		for y in xrange(6, 10):
			colors = net.update([x,y,7*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 32 + x, start[1] + 26 + y, 1, 1),1)
	# right
	for x in xrange(-8, -4):
		for y in xrange(-6, 6):
			colors = net.update([x,y,7*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 24 + x, start[1] + 42 + y, 1, 1),1)
	# front
	for x in xrange(-4, 4):
		for y in xrange(-6, 6):
			colors = net.update([x,y,7*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 24 + x, start[1] + 42 + y, 1, 1),1)
	# back
	for x in xrange(8, 16):
		for y in xrange(-6, 6):
			colors = net.update([x,y,7*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 24 + x, start[1] + 42 + y, 1, 1),1)
	# left
	for x in xrange(4, 8):
		for y in xrange(-6, 6):
			colors = net.update([x,y,7*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 24 + x, start[1] + 42 + y, 1, 1),1)

def draw_right_arm_2(genome, start):
	net.putGenome(genome)
	# top
	for x in xrange(-2, 2):
		for y in xrange(-10, -6):
			colors = net.update([x,y,8*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 46 + x, start[1] + 42 + y, 1, 1),1)
	# bottom
	for x in xrange(-2, 2):
		for y in xrange(6, 10):
			colors = net.update([x,y,8*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 50 + x, start[1] +26 + y, 1, 1),1)
	# right
	for x in xrange(2, 6):
		for y in xrange(-6, 6):
			colors = net.update([x,y,8*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 38 + x, start[1] + 42 + y, 1, 1),1)
	# front
	for x in xrange(-2, 2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,8*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 46 + x, start[1] + 42 + y, 1, 1),1)
	# left
	for x in xrange(-6, -2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,8*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 54 + x, start[1] + 42 + y, 1, 1),1)
	# back
	for x in xrange(6, 10):
		for y in xrange(-6, 6):
			colors = net.update([x,y,8*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 46 + x, start[1] + 42 + y, 1, 1),1)

def draw_left_leg_2(genome, start):
	net.putGenome(genome)
	# top
	for x in xrange(-2, 2):
		for y in xrange(-10, -6):
			colors = net.update([x,y,9*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 6 + x, start[1] + 58 + y, 1, 1),1)
	# bottom
	for x in xrange(-2, 2):
		for y in xrange(6, 10):
			colors = net.update([x,y,9*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 10 + x, start[1] + 42 + y, 1, 1),1)
	# right
	for x in xrange(2, 6):
		for y in xrange(-6, 6):
			colors = net.update([x,y,9*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + -2 + x, start[1] + 58 + y, 1, 1),1)
	# front
	for x in xrange(-2, 2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,9*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 6 + x, start[1] + 58 + y, 1, 1),1)
	# left
	for x in xrange(-6, -2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,9*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 14 + x, start[1] + 58 + y, 1, 1),1)
	# back
	for x in xrange(-10, -6):
		for y in xrange(-6, 6):
			colors = net.update([x,y,9*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 22 + x, start[1] + 58 + y, 1, 1),1)

def draw_left_leg(genome, start):
	net.putGenome(genome)
	# top
	for x in xrange(-2, 2):
		for y in xrange(-10, -6):
			colors = net.update([x,y,10*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 22 + x, start[1] + 58 + y, 1, 1),1)
	# bottom
	for x in xrange(-2, 2):
		for y in xrange(6, 10):
			colors = net.update([x,y,10*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 26 + x, start[1] + 42 + y, 1, 1),1)
	# right
	for x in xrange(2, 6):
		for y in xrange(-6, 6):
			colors = net.update([x,y,10*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 14 + x, start[1] + 58 + y, 1, 1),1)
	# front
	for x in xrange(-2, 2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,10*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 22 + x, start[1] + 58 + y, 1, 1),1)
	# left
	for x in xrange(-6, -2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,10*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 30 + x, start[1] + 58 + y, 1, 1),1)
	# back
	for x in xrange(-10, -6):
		for y in xrange(-6, 6):
			colors = net.update([x,y,10*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 38 + x, start[1] + 58 + y, 1, 1),1)

def draw_left_arm(genome, start):
	net.putGenome(genome)
	# top
	for x in xrange(-2, 2):
		for y in xrange(-10, -6):
			colors = net.update([x,y,11*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 38 + x, start[1] + 58 + y, 1, 1),1)
	# bottom
	for x in xrange(-2, 2):
		for y in xrange(6, 10):
			colors = net.update([x,y,11*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 42 + x, start[1] + 42 + y, 1, 1),1)
	# right
	for x in xrange(2, 6):
		for y in xrange(-6, 6):
			colors = net.update([x,y,11*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 30 + x, start[1] + 58 + y, 1, 1),1)
	# front
	for x in xrange(-2, 2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,11*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 38 + x, start[1] + 58 + y, 1, 1),1)
	# left
	for x in xrange(-6, -2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,11*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 46 + x, start[1] + 58 + y, 1, 1),1)
	# back
	for x in xrange(-10, -6):
		for y in xrange(-6, 6):
			colors = net.update([x,y,11*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 54 + x, start[1] + 58 + y, 1, 1),1)

def draw_left_arm_2(genome, start):
	net.putGenome(genome)
	# top
	for x in xrange(-2, 2):
		for y in xrange(-10, -6):
			colors = net.update([x,y,12*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 54 + x, start[1] + 58 + y, 1, 1),1)
	# bottom
	for x in xrange(-2, 2):
		for y in xrange(6, 10):
			colors = net.update([x,y,12*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 58 + x, start[1] + 42 + y, 1, 1),1)
	# right
	for x in xrange(2, 6):
		for y in xrange(-6, 6):
			colors = net.update([x,y,12*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 46 + x, start[1] + 58 + y, 1, 1),1)
	# front
	for x in xrange(-2, 2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,12*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 54 + x, start[1] + 58 + y, 1, 1),1)
	# left
	for x in xrange(-6, -2):
		for y in xrange(-6, 6):
			colors = net.update([x,y,12*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 62 + x, start[1] + 58 + y, 1, 1),1)
	# back
	for x in xrange(-10, -6):
		for y in xrange(-6, 6):
			colors = net.update([x,y,12*variety])
			pygame.draw.rect(DISPLAYSURF, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (start[0] + 70 + x, start[1] + 58 + y, 1, 1),1)


main()