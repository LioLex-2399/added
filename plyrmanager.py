import pygame
from gameDisplay import gameDisplay
import time
import random
from lvl import lvl1
pygame.init()
clock = pygame.time.Clock()
def plyrmanage (skin1,skin2):

	ackskin2=""
	ackskin=""
	time3=0
	if skin1 == "plyrs/s1.png":
		ackskin="bullets/ein.gif"

	if skin1 == "plyrs/s2.png":
		ackskin="bullets/kleb.png"

	if skin1 == "plyrs/s3.png":
		ackskin="bullets/nya.png"

	if skin1 == "plyrs/s4.png":
		ackskin="bullets/skylor.png"

	if skin1 == "plyrs/s5.png":
		ackskin="bullets/zane.png"

	if skin1 == "plyrs/s6.png":
		ackskin="bullets/cole.png"

	if skin1 == "plyrs/s7.png":
		ackskin="bullets/kai.png"

	if skin1 == "plyrs/s8.png":
		ackskin="bullets/Lloyd.png"

	if skin1 == "plyrs/s9.png":
		ackskin="bullets/jay.png"


	#player 2 bullet control
	if skin2 == "plyrs/s1.png":
		ackskin2="bullet2/ein.gif"

	if skin2 == "plyrs/s2.png":
		ackskin2="bullet2/kleb.png"

	if skin2 == "plyrs/s3.png":
		ackskin2="bullet2/nya.png"

	if skin2 == "plyrs/s4.png":
		ackskin2="bullet2/skylor.png"

	if skin2 == "plyrs/s5.png":
		ackskin2="bullet2/zane.png"

	if skin2 == "plyrs/s6.png":
		ackskin2="bullet2/cole.png"

	if skin2 == "plyrs/s7.png":
		ackskin2="bullet2/kai.png"

	if skin2 == "plyrs/s8.png":
		ackskin2="bullet2/Lloyd.png"

	if skin2 == "plyrs/s9.png":
		ackskin2="bullet2/jay.png"


	
	lvl1(skin1,skin2,ackskin2,ackskin)
		
	