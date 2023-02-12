##############################
#readying modules n packages##
##############################

#import
import pygame
import time
#import random
from gameDisplay import (
gameDisplay
)


#from gameDisplay import (
#gameDisplay
#)

#from disp import display_height,display_width,gameDisplay,display
clock = pygame.time.Clock()
pygame.init()
#

#
blue = 0,0,255
green = 0,255,0
red= 255,0,0
greendull = 0,90,0
reddull = 90,0,0
bluedull = 0,155,0
##############################
##############################
#pygame
##############################
###########gameDisplay############
##############################
#defining the gameDisplay width & height along with using them to create a gameDisplay and add a name n icon to it

#gameDisplay

#gameDisplay name
LEFT = 3
RIGHT = 1
block_color = (53,115,255)
m=time
##############################
##############################

background_colour=0,0,50
gameDisplay.fill(background_colour)
def mainmenu():
	Mouse_x, Mouse_y = pygame.mouse.get_pos()


	hvrbutton1=False
	hvrbutton2=False
	button1clr=green
	
	while True:
		Mouse_x, Mouse_y = pygame.mouse.get_pos()

		
		for event in pygame.event.get():
			

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_q :
					pygame.quit()
					quit()
					break
				if event.key == pygame.K_s:
					import skins
					skins.SkinGallery()
					break
			elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
				if hvrbutton1:
					import skins
					skins.SkinGallery()
				if hvrbutton2:
					pygame.quit()
					quit()
					
##########################################
##########################################
		font1 =pygame.font.SysFont('chalkduster.ttf', 72)
		img1 = font1.render('Coolesium!', True, blue)
		gameDisplay.blit(img1, (200, 300))

##########################################
############### play button ##############
		pygame.draw.rect(gameDisplay,button1clr,pygame.Rect(90, 400, 150, 60))
##########################################
##########################################
		font2 = pygame.font.SysFont('chalkduster.ttf', 40)
		img2 = font2.render('Start(s)', True, greendull)
		if Mouse_x >= 90 and Mouse_x <= 239 and Mouse_y >= 400 and Mouse_y <= 459:
			hvrbutton1=True
			pygame.draw.rect(gameDisplay,greendull,pygame.Rect(90, 400, 150, 60),  4)
		else:
			hvrbutton1=False
			button1clr = green
		gameDisplay.blit(img2, (125, 410))

##########################################
############### quit button ##############

		pygame.draw.rect(gameDisplay,red,pygame.Rect(490, 400, 150, 60))
##########################################
##########################################
		font2 = pygame.font.SysFont('chalkduster.ttf', 40)
		img2 = font2.render('Quit(q)', True, reddull)
	
		gameDisplay.blit(img2, (510, 410))
		if Mouse_x >= 490 and Mouse_x <= 639 and Mouse_y >= 400 and Mouse_y <= 459:
			hvrbutton2=True
			pygame.draw.rect(gameDisplay,reddull,pygame.Rect(490, 400, 150, 60),  4)
		else:
			hvrbutton2=False
			button1clr=green
		#		pygame.draw.line(gameDisplay,blue, (490, 400), (490, 459) ,3)
		#		pygame.draw.line(gameDisplay,blue, (490, 459), (639, 459),3)
		#		pygame.draw.line(gameDisplay,blue, (639, 459), (639, 400),3)
		#		pygame.draw.line(gameDisplay,blue, (490, 400), (639, 400),3)	
##########################################
##########################################
		
		pygame.display.update()
		clock.tick(60)
#SkinGallery()
mainmenu()
#plyskin="plyrs/s3.png"

#pygame.quit()
#quit()