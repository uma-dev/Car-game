import random

import pygame

# constants
DISPLAY_WIDTH = 1080
DISPLAY_HEIGHT = 720
CAR_WIDTH = 50
PAUSE = False
LEVEL = 1
WINS = 0
# (R,G,B)
skyBlue = (225, 245, 254)
black = (0, 0, 0)
white = (245, 245, 245)
blue = (0, 0, 150)
brightBlue = (45, 130, 220)
block = (3, 20, 90)
yellow = (255, 100, 30)
brightYellow = (255, 190, 100)
red = (150, 0, 0)
brightRed = (250, 30, 30)
green = (0, 140, 0)
brightGreen = (30, 240, 30)
gray = (200, 200, 220)
brightGray = (190, 190, 235)

# settings and objects
pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("CAR")
clock = pygame.time.Clock()
carImg = pygame.image.load("raceCar.png")
crashSound = pygame.mixer.Sound("Crash.ogg")
magic = pygame.mixer.Sound("Magic.ogg")
# gameIcon = pygame.image.load('carro.png')
# pygame.display.set_icon(gameIcon)


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def text_objects2(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_display(text, size):
    large_text = pygame.font.Font("freesansbold.ttf", size)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((DISPLAY_WIDTH // 2), (DISPLAY_HEIGHT // 2))
    gameDisplay.blit(text_surf, text_rect)


def quit_game():
    pygame.quit()
    quit()


def print_score(score):
    font = pygame.font.Font(None, 35)
    scoretext = font.render("Score: " + str(score), 1, (0, 25, 255))
    gameDisplay.blit(scoretext, (50, 30))


def instructions():
    font = pygame.font.Font(None, 35)
    text = font.render(
        "Use  <-  and  ->  to move the car. Push p to pause", 1, (0, 25, 115)
    )
    gameDisplay.blit(text, (115, 20))


def level_1():
    global LEVEL
    LEVEL = 1


def level_2():
    global LEVEL
    LEVEL = 2


def level_3():
    global LEVEL
    LEVEL = 3


def end_game(score, level):
    global WINS
    global skyBlue, block
    global carImg
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crashSound)
    gameDisplay.fill(white)  # clear screen
    message_display("You Crashed", 105)

    if WINS == 0:
        if (
            score > 99
            and level == 1
            or score > 85
            and level == 2
            or score > 69
            and level == 3
        ):
            animation("¡New Car!")
            carImg = pygame.image.load("raceCar2.png")
            skyBlue = (120, 195, 255)
            block = (5, 70, 20)
            WINS += 1

    pygame.display.update()
    print_score(score)
    button_width = 140
    button_height = 50

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        button(
            "Play Again",
            DISPLAY_WIDTH * (1 / 4) - button_width / 2,
            DISPLAY_HEIGHT * (2 / 3),
            button_width,
            button_height,
            green,
            brightGreen,
            game_loop,
            white,
        )
        button(
            "Menu",
            DISPLAY_WIDTH * (1 / 2) - button_width / 2,
            DISPLAY_HEIGHT * (2 / 3),
            button_width,
            button_height,
            blue,
            brightBlue,
            game_intro,
            white,
        )
        button(
            "Quit",
            DISPLAY_WIDTH * (3 / 4) - button_width / 2,
            DISPLAY_HEIGHT * (2 / 3),
            button_width,
            button_height,
            red,
            brightRed,
            quit_game,
            white,
        )

        pygame.display.update()
        clock.tick(15)


def game_level():
    gameDisplay.fill(white)
    message_display("Chose a Level", 80)
    level_button_width = 80
    level_button_height = 30
    nav_button_width = 100
    nav_button_height = 50

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        button(
            "1",
            DISPLAY_WIDTH * (1 / 3) - level_button_width / 2,
            DISPLAY_HEIGHT * (1 / 3),
            level_button_width,
            level_button_height,
            block,
            brightBlue,
            level_1,
            white,
        )
        button(
            "2",
            DISPLAY_WIDTH * (1 / 2) - level_button_width / 2,
            DISPLAY_HEIGHT * (1 / 3),
            level_button_width,
            level_button_height,
            block,
            brightBlue,
            level_2,
            white,
        )
        button(
            "3",
            DISPLAY_WIDTH * (2 / 3) - level_button_width / 2,
            DISPLAY_HEIGHT * (1 / 3),
            level_button_width,
            level_button_height,
            block,
            brightBlue,
            level_3,
            white,
        )

        button(
            "Play",
            DISPLAY_WIDTH * (3 / 8) - nav_button_width / 2,
            DISPLAY_HEIGHT * (2 / 3),
            nav_button_width,
            nav_button_height,
            green,
            brightGreen,
            game_loop,
            white,
        )
        button(
            "<--",
            DISPLAY_WIDTH * (5 / 8) - nav_button_width / 2,
            DISPLAY_HEIGHT * (2 / 3),
            nav_button_width,
            nav_button_height,
            yellow,
            brightYellow,
            game_intro,
            white,
        )

        pygame.display.update()
        clock.tick(15)


def button(message, x, y, width, height, ic, ac, action, color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, width, height), border_radius=10)
        if click[0] == 1:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, width, height), border_radius=12)

    small_text = pygame.font.SysFont("arial", 16)
    text_surf, text_rect = text_objects2(message, small_text, color)
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    gameDisplay.blit(text_surf, text_rect)


def unpause():
    global PAUSE
    pygame.mixer.music.unpause()
    PAUSE = False


def paused():
    global PAUSE
    pygame.mixer.music.pause()
    gameDisplay.fill(white)
    message_display("Pause", 100)
    button_width = 100
    button_height = 50

    while PAUSE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        button(
            "Continue",
            DISPLAY_WIDTH * (2 / 5) - button_width / 2,
            DISPLAY_HEIGHT * (2 / 3),
            button_width,
            button_height,
            green,
            brightGreen,
            unpause,
            white,
        )
        button(
            "Quit",
            DISPLAY_WIDTH * (4 / 5) - button_width / 2,
            DISPLAY_HEIGHT * (2 / 3),
            button_width,
            button_height,
            red,
            brightRed,
            quit_game,
            white,
        )
        pygame.display.update()
        clock.tick(15)


def animation(message):
    pygame.mixer.music.load("Doh_De_Oh.mp3")
    pygame.mixer.music.play()

    for i in range(2, 65):
        gameDisplay.fill(white)
        message_display(message, i * 2)
        pygame.display.update()
        pygame.time.delay(13)


def game_intro():
    animation("Dodge it")
    x = 30
    y = 65
    button_width = 100
    button_height = 50
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        gameDisplay.fill(white)
        message_display("A bit Race", 115)
        car(x, y)
        x += 2
        if x > DISPLAY_WIDTH:
            x += -(DISPLAY_WIDTH + CAR_WIDTH)

        button(
            "?", DISPLAY_WIDTH - 50, 0, 50, 50, gray, brightGray, instructions, block
        )
        button(
            "GO",
            DISPLAY_WIDTH * (1 / 4) - button_width / 2,
            DISPLAY_HEIGHT * (2 / 3),
            button_width,
            button_height,
            green,
            brightGreen,
            game_loop,
            white,
        )
        button(
            "Level",
            DISPLAY_WIDTH * (1 / 2) - button_width / 2,
            DISPLAY_HEIGHT * (2 / 3),
            button_width,
            button_height,
            blue,
            brightBlue,
            game_level,
            white,
        )
        button(
            "Quit",
            DISPLAY_WIDTH * (3 / 4) - button_width / 2,
            DISPLAY_HEIGHT * (2 / 3),
            button_width,
            button_height,
            red,
            brightRed,
            quit_game,
            white,
        )
        pygame.display.update()
        clock.tick(30)


def game_loop():
    global PAUSE
    global LEVEL
    pygame.mixer.music.load("Sound.mp3")
    pygame.mixer.music.play(-1)
    x = DISPLAY_WIDTH * 0.45
    y = DISPLAY_HEIGHT * 0.82
    x_change = 0
    thing_startx = random.randrange(0, DISPLAY_WIDTH - 100)

    if LEVEL == 1:
        thing_speed = 3
        thing_height = 30
        thing_width = 30
        thing_starty = -600
    if LEVEL == 2:
        thing_speed = 7
        thing_width = 35
        thing_height = 40
        thing_starty = -300
    if LEVEL == 3:
        thing_speed = 10
        thing_width = 40
        thing_height = 50
        thing_starty = -100

    score = 0
    game_exit = False

    while not game_exit:

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
                    PAUSE = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(skyBlue)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(score)

        if x > DISPLAY_WIDTH - CAR_WIDTH or x < 0:
            end_game(score, LEVEL)

        if thing_starty > DISPLAY_HEIGHT:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, int(DISPLAY_WIDTH - thing_width))
            score += 1
            if score % 5 == 0 and score < 20:
                thing_speed += 0.8
                thing_width += score * 1.19
            if score > 20 and score % 10 == 0:
                thing_speed += 0.3
                thing_width += score
            if score > 90:
                pygame.mixer.Sound.play(magic)

        if (x + CAR_WIDTH / 2) < thing_startx:
            thing_startx += -1.25  # go to
        else:  # the
            thing_startx += 1.25  # car

        if 570 > thing_starty > 474:  # between the car in y axis
            if (
                x > thing_startx
                and x < thing_width + thing_startx
                or x + CAR_WIDTH > thing_startx
                and x + CAR_WIDTH < thing_startx + thing_width
            ):
                end_game(score, LEVEL)

        pygame.display.update()  # flip
        clock.tick(62)


game_intro()
pygame.quit()
quit()
