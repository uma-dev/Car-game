import pygame
import time
import random

# constants
display_width = 800
display_height = 600
carWidth = 50
pause = False
level = 1
wins = 0
 #(R,G,B)
skyBlue = (225, 245, 254)
black = (0,0,0)
white = (245,245,245)
blue = (0,0,150)
brightBlue = (45,130,220)
block = (3,20,90)
yellow = (255,100,30)
brightYellow = (255, 190,100)
red = (150,0,0)
brightRed = (250,30,30)
green = (0,140,0)
brightGreen = (30,240,30)
gray = (200,200,220)
brightGray = (190,190,235)

# settings and objects
pygame.init()
gameDisplay = pygame.display.set_mode( ( display_width, display_height) )
pygame.display.set_caption('CAR')
clock = pygame.time.Clock()
carImg = pygame.image.load('raceCar.png')
crashSound = pygame.mixer.Sound ("Crash.ogg")
magic = pygame.mixer.Sound ("Magic.ogg")
#gameIcon = pygame.image.load('carro.png')
#pygame.display.set_icon(gameIcon)

def things_dodged (count):
	font = pygame.font.SysFont (None, 25)
	text = font.render ("Score: " + str(count), True, black)
	gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx,thingy, thingw, thingh])

def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def text_objects (text, font):
	textSurface = font.render (text, True, black)
	return textSurface, textSurface.get_rect()

def text_objects2 (text, font, color):
	textSurface = font.render (text, True, color)
	return textSurface, textSurface.get_rect()

def message_display(text, size):
	largeText = pygame.font.Font('freesansbold.ttf', size)
	textSurf, textRect = text_objects (text, largeText)
	textRect.center = (( display_width/2), (display_height/2))
	gameDisplay.blit (textSurf, textRect)

def quitGame():
	pygame.quit()
	quit()

def printScore ( score ):
	font=pygame.font.Font(None,35)
	scoretext=font.render("Score: "+ str(score), 1,(0,25,255))
	gameDisplay.blit(scoretext, (50,30 ) )

def instructions ():
	font=pygame.font.Font(None,35)
	text=font.render("Use  <-  and  ->  to move the car. Push p to pause", 1,(0,25,115) )
	gameDisplay.blit(text, (115,20) )

def level_1():
	global level
	level = 1
def level_2():
	global level
	level = 2
def level_3():
	global level
	level = 3

def endGame( score, level):
	global wins
	global skyBlue, block
	global carImg
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play (crashSound)
	gameDisplay.fill(white) #clear screen
	message_display('You Crashed', 105)

	if wins == 0:
		if score > 99 and level == 1 or score >85 and level == 2 or score > 69 and level == 3:
			animation ("¡New Car!")
			carImg = pygame.image.load ("raceCar2.png")
			skyBlue = (120,195,255)
			block = (5,70,20)
			wins += 1

	pygame.display.update()
	printScore (score)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitGame()
		button("Play Again",170,450,140,50,green,brightGreen,gameLoop, white)
		button ("Menu",335,450,130,50,blue,brightBlue,gameIntro,white)
		button("Quit",500,450,140,50,red,brightRed,quitGame, white)

		pygame.display.update()
		clock.tick(15)

def gameLevel():
	gameDisplay.fill(white)
	message_display('Chose a Level', 85)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitGame()

		button ("1",260,130,80,27,block,brightBlue,level_1, white)
		button ("2",350,130,80,27,block,brightBlue,level_2, white)
		button ("3",440,130,80,27,block,brightBlue,level_3,white)

		button("Play",190,450,100,50,green,brightGreen,gameLoop,white) 
		button("<--",500,450,100,50,yellow,brightYellow,gameIntro, white)

		pygame.display.update()
		clock.tick(15)


def button(message, x, y, width, height, ic, ac, action, color):

	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x+width > mouse[0] > x and y+height > mouse[1] > y:
		pygame.draw.rect(gameDisplay, ac,(x,y,width,height), border_radius=4)
		if click[0] == 1:
			action()
	else:
		pygame.draw.rect(gameDisplay, ic,(x,y,width,height), border_radius=12)

	smallText = pygame.font.SysFont("arial",22)
	textSurf, textRect = text_objects2 (message, smallText, color)
	textRect.center = ( (x+(width/2)), (y+(height/2)) )
	gameDisplay.blit(textSurf, textRect)

def unPaused():
	global pause
	pygame.mixer.music.unpause()
	pause = False

def paused():

	global pause

	pygame.mixer.music.pause()
	gameDisplay.fill (white)
	message_display("Pause", 100)

	while pause:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				quitGame()

		button("Continue",170,450,110,50,green,brightGreen,unPaused, white)
		button("Quit",520,450,110,50,red,brightRed,quitGame, white)

		pygame.display.update()
		clock.tick(15)


def animation( message ):
	pygame.mixer.music.load ("Doh_De_Oh.mp3")
	pygame.mixer.music.play()

	for i in range (2,65):
		gameDisplay.fill(white)
		message_display ( message,i*2 )
		pygame.display.update()
		pygame.time.delay (13)


def gameIntro():
	animation("Dodge it")
	x = 30
	y = 65
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitGame()

		gameDisplay.fill(white)
		message_display ("A bit Race", 115)
		car (x,y)
		x += 2
		if x  > display_width:
			x += - (display_width + carWidth)


		button ("?",display_width-50,0,50,50,gray,brightGray,instructions,block)

		button ("GO", 150,470,100,50, green, brightGreen, gameLoop, white)
		button ("Level", 342,470,100,50, blue, brightBlue, gameLevel, white )
		button ("Quit", 550,470,100,50, red, brightRed, quitGame, white)

		pygame.display.update()
		clock.tick(30)


def gameLoop( ):
	global pause
	global level
	pygame.mixer.music.load ("Sound.mp3")
	pygame.mixer.music.play(-1)
	x = (display_width  * 0.45 )
	y = (display_height * 0.82 )

	x_change = 0

	thing_startx = random.randrange (0,display_width-100)
	if level == 1:
		thing_speed = 3
		thing_height = 30
		thing_width = 30
		thing_starty = -600
	if level == 2:
		thing_speed = 7
		thing_width = 35
		thing_height = 40
		thing_starty = -300
	if level == 3:
		thing_speed = 10
		thing_width = 40
		thing_height = 50
		thing_starty = -100


	score = 0
	gameExit = False

	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -9
				elif event.key == pygame.K_RIGHT:
					x_change = 9
				elif event.key == pygame.K_p:
					pause = True
					paused()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT: 
					x_change = 0


		x += x_change
		gameDisplay.fill (skyBlue)

		#things(thingx, thingy, thingw, thingh, color)
		things(thing_startx, thing_starty, thing_width, thing_height, block )
		thing_starty += thing_speed
		car (x,y)
		things_dodged (score)

		if x > display_width - carWidth or x < 0:
			endGame ( score, level )

		if thing_starty > display_height:
			thing_starty = 0-thing_height
			thing_startx = random.randrange (0, int (display_width-thing_width) )
			score += 1
			if score % 5 == 0 and score < 20:
				thing_speed += 0.8
				thing_width += (score * 1.19)
			if score > 20 and score %10 == 0:
				thing_speed += 0.3
				thing_width += (score)
			if score > 90:
				pygame.mixer.Sound.play (magic)

		if  (x+carWidth/2 ) < thing_startx:
			thing_startx += -1.25		#go to
		else:					#the
			thing_startx += 1.25		#car

		if ( 570 > thing_starty > 474): #between the car in y axis
			if x > thing_startx and x < thing_width + thing_startx or x + carWidth > thing_startx and x +carWidth < thing_startx + thing_width :
				endGame ( score, level )

		pygame.display.update () #flip
		clock.tick (62)

gameIntro()
pygame.quit()
quit()























