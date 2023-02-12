import pygame

from gameDisplay import(
gameDisplay
) 
from time import sleep
pygame.init()
pygame.font.init()
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
blue = 0,0,255
green = 0,255,0
red= 255,0,0
greendull = 0,90,0
reddull = 90,0,0
bluedull = 0,155,0
LEFT = 3
RIGHT = 1
clock = pygame.time.Clock()
background_colour=255,255,255
gameDisplay.fill(background_colour)
def Skinmanager(skin):

	global s1
	plyskin=plyrskin
	s1="plyrs/s1.png"
	s2="plyrs/s2.png"
	s3="plyrs/s3.png"
	s4="plyrs/s4.png"
	s5="plyrs/s5.png"
	s6="plyrs/s6.png"
	s7="plyrs/s7.png"
	s8="plyrs/s8.png"
	s9="plyrs/s9.png"
	
	s9p="plyrs-3-3/pixil-frame-0.png"
	s8p="plyrs-3-3/pixil-frame-1.png"
	s7p="plyrs-3-3/pixil-frame-2.png"
	s6p="plyrs-3-3/pixil-frame-3.png"
	s5p="plyrs-3-3/pixil-frame-4.png"
	s4p="plyrs-3-3/pixil-frame-5.png"
	s3p="plyrs-3-3/pixil-frame-6.png"
	s2p="plyrs-3-3/pixil-frame-7.png"
	s1p="plyrs-3-3/pixil-frame-8.png"
	bckgrd=1,4,54
	gameDisplay.fill(bckgrd)
	skin1p="plyr-3/1.png"
	while True:
		#######################################
		if skin == s1:
			skin1p=s1p
			keydis="1"
		if skin == s2:
			skin1p=s2p
			keydis="2"			
		if skin == s3:
			skin1p=s3p
			keydis="3"
		if skin == s4:
			skin1p=s4p
			keydis="4"		
		if skin == s5:
			skin1p=s5p
			keydis="5"			
		if skin == s6:
			skin1p=s6p
			keydis="6"			
		if skin == s7:
			skin1p=s7p
			keydis="7"											   
		if skin == s8:
			skin1p=s8p
			keydis="8"											   
		if skin == s9:
			skin1p=s9p
			keydis="9"
		import skins2
		skins2.SkinGallery2(skin,skin1p)




#	plyrskin=plyskin
plyrskin=""
pygame.font.init()
Skinmanager(s1)
###################################
###################################
###################################