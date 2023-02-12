import pygame
from gameDisplay import gameDisplay

clock = pygame.time.Clock()
def win(ply1hlth,ply2hlth):
	ply1 = False
	ply2 = False
	if ply1hlth <= 0 and ply2hlth >=0:
		ply2 = True
		
	if ply2hlth <= 0 and ply1hlth >=0:
		ply1 = True
		
#	if ply1hlth <= 0 and ply2hlth <=0:
	#	ply2 = False
	#	ply1 = False

	
	while True:
		background_colour=0,200,55
		gameDisplay.fill(background_colour)
		if ply1:
			font1 = pygame.font.Font('amatic-sc.bold.ttf', 60)
			img1 = font1.render('Player 1 won!', True, (0,0,255))
			gameDisplay.blit(img1, (200, 200))			
		elif ply2:
			font1 = pygame.font.Font('amatic-sc.bold.ttf', 60)
			img1 = font1.render('Player 2 won!', True, (0,255,0))
			gameDisplay.blit(img1, (200, 200))
		for event in pygame.event.get():
			

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		pygame.display.update()
		clock.tick(60)			