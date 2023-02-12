import pygame
from gameDisplay import(
gameDisplay
) 
blue = 0,0,255
green = 0,255,0
red= 255,0,0
greendull = 0,90,0
reddull = 90,0,0
bluedull = 0,155,0
LEFT = 3
RIGHT = 1
pygame.init()
#import lvl
from time import sleep
import random
plyrskin="plyrs/s1.png"
s1="plyrs/s1.png"
s2="plyrs/s2.png"
s3="plyrs/s3.png"
s4="plyrs/s4.png"
s5="plyrs/s5.png"
s6="plyrs/s6.png"
s7="plyrs/s7.png"
s8="plyrs/s8.png"
s9="plyrs/s9.png"
s1p2="plyrs-3-3/pixil-frame-0.png"
s2p2="plyrs-3-3/pixil-frame-1.png"
s3p2="plyrs-3-3/pixil-frame-8.png"
s4p2="plyrs-3-3/pixil-frame-2.png"
s5p2="plyrs-3-3/pixil-frame-3.png"
s6p2="plyrs-3-3/pixil-frame-4.png"
s7p2="plyrs-3-3/pixil-frame-5.png"
s8p2="plyrs-3-3/pixil-frame-6.png"
s9p2="plyrs-3-3/pixil-frame-7.png"

clock = pygame.time.Clock()
background_colour=255,255,255
gameDisplay.fill(background_colour)
def SkinGallery2(skin1,skin1p):
	key1=pygame.K_1
	key2=pygame.K_2
	key3=pygame.K_3
	key4=pygame.K_4
	key5=pygame.K_5
	key6=pygame.K_6
	key7=pygame.K_7
	key8=pygame.K_8
	skin1p=skin1p
	s1h=False
	s2h=False
	s3h=False
	s4h=False
	s5h=False
	s6h=False
	s7h=False
	s8h=False
	s9h=False

	s1ho=False
	s2ho=False
	s3ho=False
	s4ho=False
	s5ho=False
	s6ho=False
	s7ho=False
	s8ho=False
	s9ho=False
	skin2p=s9p2
	skin1=skin1
	plyskin="none"
	s1="plyrs/s1.png"
	s2="plyrs/s2.png"
	s3="plyrs/s3.png"
	s4="plyrs/s4.png"
	s5="plyrs/s5.png"
	s6="plyrs/s6.png"
	s7="plyrs/s7.png"
	s8="plyrs/s8.png"
	s9="plyrs/s9.png"
	
	s1p="plyr-2/p1p.png"
	s2p="plyr-2/p2p.png"
	s3p="plyr-2/p3p.png"    
	s4p="plyr-2/p4p.png"
	s5p="plyr-2/p5p.png"
	s6p="plyr-2/p6p.png"
	s7p="plyr-2/p7p.png"
	s8p="plyr-2/p8p.png"
	s9p="plyr-2/p9p.png"
	bckgrd=1,4,54
	gameDisplay.fill(bckgrd)
	while True:


		font1 = pygame.font.Font('amatic-sc.bold.ttf', 40)
		img1 = font1.render('player 2 menu ', True, (200,240,0))
		gameDisplay.blit(img1, (500, 13))
		image2 = pygame.image.load(skin1p)
		gameDisplay.blit(image2, (600, 500))
		image2 = pygame.image.load(skin2p)
		gameDisplay.blit(image2, (700, 500))
		
		image1 = pygame.image.load(s1)
		gameDisplay.blit(image1, (40, 10))
		
		image2 = pygame.image.load(s2)
		gameDisplay.blit(image2, (80, 10))		
		image3 = pygame.image.load(s3)
		gameDisplay.blit(image3, (120, 10))
		image4 = pygame.image.load(s4)
		gameDisplay.blit(image4, (160, 10))
		image5 = pygame.image.load(s5)
		gameDisplay.blit(image5, (200, 10))
		image6 = pygame.image.load(s6)
		gameDisplay.blit(image6, (240, 10))
		image7 = pygame.image.load(s7)
		gameDisplay.blit(image7, (280, 10))
		image8 = pygame.image.load(s8)
		gameDisplay.blit(image8, (320, 10))
		image9 = pygame.image.load(s9)
		gameDisplay.blit(image9, (360, 10))
		Mouse_x, Mouse_y = pygame.mouse.get_pos()
		
#		image = pygame.image.load(plyskin)
#		gameDisplay.blit(image, (300, 400))
		for event in pygame.event.get():
			

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_1 :
					plyskin=s1
				if event.key == pygame.K_2:
					plyskin=s2
				if event.key == pygame.K_3 :
					plyskin=s3
				if event.key == pygame.K_4:
					plyskin=s4
				if event.key == pygame.K_5 :
					plyskin=s5
				if event.key == pygame.K_6:
					plyskin=s6
				if event.key == pygame.K_7 :
					plyskin=s7
				if event.key == pygame.K_8:
					plyskin=s8
				if event.key == pygame.K_9 :
					plyskin=s9
				if event.key == pygame.K_RETURN:
					if not plyskin == "none":
						import plyrmanager
						plyrmanager.plyrmanage(skin1,plyskin)
				if not event.key == pygame.K_RETURN:
					pass
				else:
					pass
			elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
				if s1h:
					s1ho=True
					s2ho=False
					s3ho=False
					s4ho=False
					s5ho=False
					s6ho=False
					s7ho=False
					s8ho=False
					s9ho=False
				if s2h:
					s1ho=False
					s2ho=True
					s3ho=False
					s4ho=False
					s5ho=False
					s6ho=False
					s7ho=False
					s8ho=False
					s9ho=False
				if s3h:
					s1ho=False
					s2ho=False
					s3ho=True
					s4ho=False
					s5ho=False
					s6ho=False
					s7ho=False
					s8ho=False
					s9ho=False
				if s4h:
					s1ho=False
					s2ho=False
					s3ho=False
					s4ho=True
					s5ho=False
					s6ho=False
					s7ho=False
					s8ho=False
					s9ho=False
				if s5h:
					s1ho=False
					s2ho=False
					s3ho=False
					s4ho=False
					s5ho=True
					s6ho=False
					s7ho=False
					s8ho=False
					s9ho=False
				if s6h:
					s1ho=False
					s2ho=False
					s3ho=False
					s4ho=False
					s5ho=False
					s6ho=True
					s7ho=False
					s8ho=False
					s9ho=False
				if s7h:
					s1ho=False
					s2ho=False
					s3ho=False
					s4ho=False
					s5ho=False
					s6ho=False
					s7ho=True
					s8ho=False
					s9ho=False
				if s8h:
					s1ho=False
					s2ho=False
					s3ho=False
					s4ho=False
					s5ho=False
					s6ho=False
					s7ho=False
					s8ho=True
					s9ho=False
				if s9h:
					s1ho=False
					s2ho=False
					s3ho=False
					s4ho=False
					s5ho=False
					s6ho=False
					s7ho=False
					s8ho=False
					s9ho=True


		
		if plyskin == s1:
			image = pygame.image.load(s1p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s9p2

			
		if plyskin == s2:
			image = pygame.image.load(s2p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s8p2

			
		if plyskin == s3:
			image = pygame.image.load(s3p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s7p2


		if plyskin == s4:
			image = pygame.image.load(s4p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s6p2

		
		if plyskin == s5:
			image = pygame.image.load(s5p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s5p2

			
		if plyskin == s6:
			image = pygame.image.load(s6p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s4p2

			
		if plyskin == s7:
			image = pygame.image.load(s7p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s3p2

			
		if plyskin == s8:
			image = pygame.image.load(s8p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s2p2

			
		if plyskin == s9:
			image = pygame.image.load(s9p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s1p2


		if s1ho:
			image = pygame.image.load(s1p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s9p2

			
		if s2ho:
			image = pygame.image.load(s2p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s8p2

			
		if s3ho:
			image = pygame.image.load(s3p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s7p2


		if s4ho:
			image = pygame.image.load(s4p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s6p2

		
		if s5ho:
			image = pygame.image.load(s5p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s5p2

			
		if s6ho:
			image = pygame.image.load(s6p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s4p2

			
		if s7ho:
			image = pygame.image.load(s7p)
			gameDisplay.blit(image, (200, 300))
			skin2p = s3p2

											
		if s8ho:					   
			image = pygame.image.load(s8p)	   
			gameDisplay.blit(image, (200, 300))
			skin2p = s2p2

											
		if s9ho:					   
			image = pygame.image.load(s9p)	   
			gameDisplay.blit(image, (200, 300))
			skin2p = s1p2

	
		##tips!##
		pygame.draw.rect(gameDisplay, (100,100,205), (9,90,150,450),(2000))
		font1 = pygame.font.Font('amatic-sc.bold.ttf', 32)
		img1 = font1.render('___tips!___', True, (0,255,0))
		gameDisplay.blit(img1, (12, 93))



		
		font1 = pygame.font.Font('amatic-sc.bold.ttf', 22)
		img1 = font1.render('-use the keys 1 to 9 ', True, (2,240,0))
		gameDisplay.blit(img1, (12, 143))		

		font1 = pygame.font.Font('amatic-sc.bold.ttf', 22)
		img1 = font1.render('to navigate through ', True, (2,240,0))
		gameDisplay.blit(img1, (12, 163))

		font1 = pygame.font.Font('amatic-sc.bold.ttf', 22)
		img1 = font1.render('skins', True, (2,240,0))
		gameDisplay.blit(img1, (12, 183))

		font1 = pygame.font.Font('amatic-sc.bold.ttf', 22)
		img1 = font1.render('- finished yet?   ', True, (2,240,0))
		gameDisplay.blit(img1, (12, 203))

		
		font1 = pygame.font.Font('amatic-sc.bold.ttf', 22)
		img1 = font1.render('press "Enter" if yes', True, (2,240,0))
		gameDisplay.blit(img1, (12, 223))

		if Mouse_y >= 10 and Mouse_y <= 33 and Mouse_x >= 39 and Mouse_x <=63 :
			pygame.draw.rect(gameDisplay,green,pygame.Rect(40, 10, 24, 24),1)
			s1h=True
			s2h=False
			s3h=False
			s4h=False
			s5h=False
			s6h=False
			s7h=False
			s8h=False
			s9h=False
		if Mouse_y >= 10 and Mouse_y <= 33 and Mouse_x >= 79 and Mouse_x <=103 :
			pygame.draw.rect(gameDisplay,green,pygame.Rect(80, 10, 24, 24),1)
			s1h=False
			s2h=True
			s3h=False
			s4h=False
			s5h=False
			s6h=False
			s7h=False
			s8h=False
			s9h=False
		if Mouse_y >= 10 and Mouse_y <= 33 and Mouse_x >= 119 and Mouse_x <=143 :
			pygame.draw.rect(gameDisplay,green,pygame.Rect(120, 10, 24, 24),1)
			s1h=False
			s2h=False
			s3h=True
			s4h=False
			s5h=False
			s6h=False
			s7h=False
			s8h=False
			s9h=False
		if Mouse_y >= 10 and Mouse_y <= 33 and Mouse_x >= 159 and Mouse_x <=183 :
			pygame.draw.rect(gameDisplay,green,pygame.Rect(160, 10, 24, 24),1)
			s1h=False
			s2h=False
			s3h=False
			s4h=True
			s5h=False
			s6h=False
			s7h=False
			s8h=False
			s9h=False
		if Mouse_y >= 10 and Mouse_y <= 33 and Mouse_x >= 199 and Mouse_x <=223 :
			pygame.draw.rect(gameDisplay,green,pygame.Rect(200, 10, 24, 24),1)
			s1h=False
			s2h=False
			s3h=False
			s4h=False
			s5h=True
			s6h=False
			s7h=False
			s8h=False
			s9h=False
		if Mouse_y >= 10 and Mouse_y <= 33 and Mouse_x >= 239 and Mouse_x <=263 :
			pygame.draw.rect(gameDisplay,green,pygame.Rect(240, 10, 24, 24),1)
			s1h=False
			s2h=False
			s3h=False
			s4h=False
			s5h=False
			s6h=True
			s7h=False
			s8h=False
			s9h=False
		if Mouse_y >= 10 and Mouse_y <= 33 and Mouse_x >= 279 and Mouse_x <=303 :
			pygame.draw.rect(gameDisplay,green,pygame.Rect(280, 10, 24, 24),1)
			s1h=False
			s2h=False
			s3h=False
			s4h=False
			s5h=False
			s6h=False
			s7h=True
			s8h=False
			s9h=False
		if Mouse_y >= 10 and Mouse_y <= 33 and Mouse_x >= 319 and Mouse_x <=343 :
			pygame.draw.rect(gameDisplay,green,pygame.Rect(320, 10, 24, 24),1)
			s1h=False
			s2h=False
			s3h=False
			s4h=False
			s5h=False
			s6h=False
			s7h=False
			s8h=True
			s9h=False
		if Mouse_y >= 10 and Mouse_y <= 33 and Mouse_x >= 359 and Mouse_x <=383 :
			pygame.draw.rect(gameDisplay,green,pygame.Rect(360, 10, 24, 24),1)
			s1h=False
			s2h=False
			s3h=False
			s4h=False
			s5h=False
			s6h=False
			s7h=False
			s8h=False
			s9h=True		
		pygame.display.update()
		clock.tick(60)
s9="plyrs/s9.png"
s9po="plyrs-3-3/pixil-frame-0.png"
SkinGallery2(s9,s9po)

pygame.font.init()
