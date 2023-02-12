import pygame,random
from gameDisplay import gameDisplay
clock = pygame.time.Clock()
from winner import win
blue = 0,0,255
green = 0,255,0
red= 255,0,0
greendull = 0,90,0
reddull = 90,0,0
bluedull = 0,155,0
pygame.init()
def lvl1(p1skin,p2skin,att1,att2):
	arrowlhov = False
	arrowrhov = False
	arrowdhov = False

	arrowlhovcl = False
	arrowrhovcl = False


	keyahov = False
	keydhov = False
	keywhov = False

	keyahovcl = False
	keydhovcl = False

	p1atckskin=""
	bckgrd=4,156,255
	enemyhlth=100
	plyrhlth=100
	p2bullet=False
	p1countdown=0
	p2countdown=2
	x1=350
	y1=500
	x3=350
	y3=500
	p1bullet=False
	x2=350
	y2=10
	x4=350
	y4=10

	while True:
		Mouse_x, Mouse_y = pygame.mouse.get_pos()
		background_colour=0,200,55
		gameDisplay.fill(background_colour)
		#player
		my_font = pygame.font.Font('amatic-sc.bold.ttf', 30)
		text_surface = my_font.render('health: '+str(plyrhlth)+"%", True, (0, 0, 0))
		
		gameDisplay.blit(text_surface, (4,490))		
		pygame.draw.line(gameDisplay, (6,6,6), (0, 480), (800, 480),(4))
		image1 = pygame.image.load(p1skin)
		gameDisplay.blit(image1, (x1, y1))
#		print()


		#boss
		pygame.draw.line(gameDisplay, (6,6,6), (0, 50), (800, 50),(4))		
		image1 = pygame.image.load(p2skin)
		gameDisplay.blit(image1, (x2, y2))
		
		my_font = pygame.font.Font('amatic-sc.bold.ttf', 30)
		text_surface = my_font.render('health: '+str(enemyhlth)+"%", True, (0, 0, 0))
		
		gameDisplay.blit(text_surface, (4,4))
		

		if plyrhlth <= 0 or enemyhlth<=0:
			win(plyrhlth,enemyhlth)
			
		for event in pygame.event.get():
			

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_a :
					x1-=20
				elif event.key==pygame.K_d:
					x1+=20
				elif event.key == pygame.K_w:
					p1bullet=True
				elif event.key == pygame.K_UP:
					p2bullet=True
				if event.key == pygame.K_LEFT :
					x2-=20
				elif event.key==pygame.K_RIGHT:
					x2+=20
			elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				
				if arrowdhov:
					p2bullet=True


				if arrowlhov:
					arrowlhovcl=True
				else:
					arrowlhovcl=False

				if arrowrhov:
					arrowrhovcl=True
				else:
					arrowrhovcl=False

				if keywhov:
					p1bullet=True
				else:
					p1bullet=False

				if keyahov:
					keyahovcl=True
				else:
					keyahovcl=False

				if keydhov:
					keydhovcl=True
				else:
					keydhovcl=False
#########################################################################
#########################################################################					
		if p1bullet:
			y3-=10
			image1 = pygame.image.load(att1)
			gameDisplay.blit(image1, (x3, y3))
		if y3 == y2 and x3 == x2:
			enemyhlth-= 10
			x3=x1
			y3=y1
			p1bullet=False
		if y3 == 0:
			x3=x1
			y3=y1
			p1bullet=False
		if not p1bullet:
			x3=x1
			y3=y1
##########################################################################
		if p2bullet:
			y4+=10
			image1 = pygame.image.load(att2)
			gameDisplay.blit(image1, (x4, y4))
		if y4 == y1 and x4 == x1:
			plyrhlth-= 10
			x4=x2
			y4=y2
			p2bullet=False

		if y4 == 500:
			x4=x2
			y4=y2
			p2bullet=False

		if not p2bullet:
			x4=x2
			y4=y2
#########################################################################
#########################################################################
		if x1 <= 100:
			x1+=20

		if x2 <= 100:
			x2+=20		

		if x1 >= 790:
			x1-=20

		if x2 >= 790:
			x2-=20

##########################################################################		
################# buttons ################################################

		pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 60, 130, 39))

		my_font = pygame.font.Font('amatic-sc.bold.ttf', 25)
		text_surface = my_font.render('shoot(up arrow)', True, (0, 0, 0))
		gameDisplay.blit(text_surface, (15,60))

##########################################################################

		pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 120, 130, 39))

		my_font = pygame.font.Font('amatic-sc.bold.ttf', 23)
		text_surface = my_font.render('move left( <-- )', True, (0, 0, 0))
		gameDisplay.blit(text_surface, (15,120))

###########################################################################

		pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 180, 130, 39))

		my_font = pygame.font.Font('amatic-sc.bold.ttf', 23)
		text_surface = my_font.render('move right( --> )', True, (0, 0, 0))
		gameDisplay.blit(text_surface, (14,180))
###############################################################################
####################### borders  ##############################################
########																#######
		my_font = pygame.font.Font('amatic-sc.bold.ttf', 25)				###
		text_surface = my_font.render('P1 CONTROLS', True, (0, 0, 0)) 		###
		gameDisplay.blit(text_surface, (14,450))
						
		my_font = pygame.font.Font('amatic-sc.bold.ttf', 25)				###
		text_surface = my_font.render('P2 CONTROLS', True, (0, 0, 0)) 		###
		gameDisplay.blit(text_surface, (14,240))							###
#																			###
		pygame.draw.line(gameDisplay,greendull, (0, 270), (150, 270) ,6)	###
#		pygame.draw.line(gameDisplay,greendull, (0, 478), (150, 478) ,6)    ###
		pygame.draw.line(gameDisplay,greendull, (150, 233), (150, 50),6)    ###
		pygame.draw.line(gameDisplay,greendull, (150, 233), (150, 478),6)   ###
		if Mouse_x > 0 and Mouse_x < 150:print()


########																#######
###############################################################################
####################### player 1 ##############################################

		pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 280, 130, 39))

		my_font = pygame.font.Font('amatic-sc.bold.ttf', 23)
		text_surface = my_font.render('shoot( w )', True, (0, 0, 0))
		gameDisplay.blit(text_surface, (14,280))
###########################################################################

		pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 340, 130, 39))

		my_font = pygame.font.Font('amatic-sc.bold.ttf', 23)
		text_surface = my_font.render('move left( <-- )', True, (0, 0, 0))
		gameDisplay.blit(text_surface, (14,340))
###########################################################################

		pygame.draw.rect(gameDisplay,blue,pygame.Rect(10, 400, 130, 39))

		my_font = pygame.font.Font('amatic-sc.bold.ttf', 23)
		text_surface = my_font.render('move right( --> )', True, (0, 0, 0))
		gameDisplay.blit(text_surface, (14,400))


############################################################################
####### button cord-testers ################################################ x2 = x1 + 38
#		pygame.draw.line(gameDisplay,red, (10, 330), (139, 330) ,1)
#		pygame.draw.line(gameDisplay,red, (139, 330), (139, 368),1)
#		pygame.draw.line(gameDisplay,red, (139, 368), (10, 368),1)
#		pygame.draw.line(gameDisplay,red, (10, 330), (10, 368),1)

############################################################################
########################## mouse hover checkers ############################
		if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 60 and Mouse_y <=  88:
			arrowdhov = True
			pygame.draw.rect(gameDisplay,green,pygame.Rect(10, 60, 130, 39),2)
		else:
			arrowdhov = False
############################################################################

		if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 120 and Mouse_y <= 158:
			pygame.draw.rect(gameDisplay,green,pygame.Rect(10, 120, 130, 39),2)
			arrowlhov= True
#			print("l")
		else:
			arrowlhov=False
		
############################################################################
		
		if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 180 and Mouse_y <= 218:
			pygame.draw.rect(gameDisplay,green,pygame.Rect(10, 180, 130, 39),2)
			arrowrhov= True
#			print("l")
		else:
			arrowrhov=False
		
#############################################################################
#############################################################################
		if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 280 and Mouse_y <= 318:
			pygame.draw.rect(gameDisplay,green,pygame.Rect(10, 280, 130, 39),2)
			keywhov= True
#			print("l")
		else:
			keywhov=False
		
#############################################################################
		if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 340 and Mouse_y <= 378:
			pygame.draw.rect(gameDisplay,green,pygame.Rect(10, 340, 130, 39),2)
			keyahov= True
#			print("l")
		else:
			keyahov=False
		
#############################################################################
		if Mouse_x >= 10 and Mouse_x <= 139 and Mouse_y >= 400 and Mouse_y <= 438:
			pygame.draw.rect(gameDisplay,green,pygame.Rect(10, 400, 130, 39),2)
			keydhov= True
#			print("l")
		else:
			keydhov=False
		""""""
############################################################################
############################################################################
		if arrowlhovcl:
			x2-=20

		if arrowrhovcl:
			x2+=20

		if keydhovcl:
			x1-=20

		if keyahovcl:
			x1+=20
		arrowlhovcl=False
		arrowrhovcl=False
		keydhovcl=False
		keyahovcl=False

		pygame.display.update()

		
		clock.tick(60)
p2b="bullet2/Lloyd.png"
p1b="bullets/Lloyd.png"
p1p="plyrs/s8.png"
lvl1(p1p,p1p,p2b,p1b)		