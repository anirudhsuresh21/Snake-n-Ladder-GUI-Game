import pygame
from random import randint


#adding the time function of the pygame module to track time
time = pygame.time.Clock()

#initializing the pygame module
pygame.init()
scr_width = 1366
scr_height = 768

#adding icon to the pygame window
ic = pygame.image.load("snake logo.png")
display = pygame.display.set_mode((scr_width,scr_height),pygame.FULLSCREEN)
pygame.display.set_caption("Snake and Ladders Game")
pygame.display.set_icon(ic)
pygame.display.update()

#Pre-defining the colors so that it can be used again and again
black_c = (10, 10, 10)
white_c = (250, 250, 250)
red_c2 = (200, 0, 0)
green_c2 = (0, 200, 0)
blue_c2 = (0, 0, 200)
blue_red = (240, 0, 0)
blue_green = (0, 230, 0)
grey_c = (50, 50, 50)
yellow_c2 = (150, 150, 0)
purple_c = (43, 3, 132)
blue_purple = (60, 0, 190)

#including the necessary images of dice and the snake and ladder board
game_board = pygame.image.load("Snakes_ladders_big_image.png")
d1 = pygame.image.load("dice_image1.png")
d2 = pygame.image.load("dice_image2.png")
d3 = pygame.image.load("dice_image3.png")
d4 = pygame.image.load("dice_image4.png")
d5 = pygame.image.load("dice_image5.png")
d6 = pygame.image.load("dice_image6.png")

#including images of coin
red_c = pygame.image.load("red_c.png")
yellow_c = pygame.image.load("yellow_c.png")
green_c = pygame.image.load("green_c.png")
blue_c = pygame.image.load("blue_c.png")
menu_background = pygame.image.load("introduction.png")
post = pygame.image.load("background.png")

#including the necessary background images
initial_background = pygame.image.load("opening.png")
initial_background1 = pygame.image.load("introduction1.png")
initial_background2 = pygame.image.load("introduction2.png")
initial_background3 = pygame.image.load("introduction3.png")
initial_background4 = pygame.image.load("introduction4.png")
creditations1 = pygame.image.load("CREDITS.png")

#adding music to the game
snake_sound = pygame.mixer.Sound("snake.wav")
sound = pygame.mixer.music.load("music2.wav")
win = pygame.mixer.Sound("win.wav")
lose = pygame.mixer.Sound("lose.wav")
ladder = pygame.mixer.Sound("ladder.wav")

#positioning the mouse
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()


# Message displaying for buttons
def msg_display_scr(text,x,y,fs):
    largeText = pygame.font.SysFont('consolas',fs)
    TextSurf, TextRect = text_obj_scr(text, largeText, white_c)
    TextRect.center = (x,y)
    display.blit(TextSurf,TextRect)


def text_obj_scr(text,font):
    textSurface = font.render(text,True,white_c)
    return textSurface, textSurface.get_recr()


# Message displaying for field
def msg_display1_scr(text, x, y, fs, c):
    largeText = pygame.font.SysFont('consolas', fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x, y)
    display.blit(TextSurf, TextRect)


def text_obj_scr(text, font, c):
    textSurface = font.render(text, True, c)
    return textSurface, textSurface.get_rect()


#coin movement function
def movement(a):
    l1 = [[406, 606], [456, 606], [506, 606], [556, 606], [606, 606], [656, 606], [706, 606], [756, 606], [806, 606],
          [856, 606], [906, 606], [906, 560], [856, 560], [806, 560], [756, 560], [706, 560], [656, 560], [606, 560],
          [556, 560], [506, 560], [456, 560], [456, 506], [506, 506], [556, 506], [606, 506], [656, 506], [706, 506],
          [756, 506], [806, 506], [856, 506], [906, 506], [906, 460], [856, 460], [806, 460], [756, 460], [706, 460],
          [656, 460], [606, 460], [556, 460], [506, 460], [456, 460], [456, 406], [506, 406], [556, 406], [606, 406],
          [656, 406], [706, 406], [756, 406], [806, 406], [856, 406], [906, 406], [906, 360], [856, 360], [806, 360],
          [756, 360], [706, 360], [656, 360], [606, 360], [556, 360], [506, 360], [456, 360], [456, 306], [506, 306],
          [556, 306], [606, 306], [656, 306], [706, 306], [756, 306], [806, 306], [856, 306], [906, 306], [906, 260],
          [856, 260], [806, 260], [756, 260], [706, 260], [656, 260], [606, 260], [556, 260], [506, 260], [456, 260],
          [456, 206], [506, 206], [556, 206], [606, 206], [656, 206], [706, 206], [756, 206], [806, 206], [856, 206],
          [906, 206], [906, 160], [856, 160], [806, 160], [756, 160], [706, 160], [656, 160], [606, 160], [556, 160],
          [506, 160], [456, 160]]
    l2 = l1[a]
    x = l2[0] - 25
    y = l2[1] - 25
    return x, y


def text_objects1(text, font):
    textSurface = font.render(text, True, grey_c)
    return textSurface, textSurface.get_rect()

#function to find if the user has found a ladder
def ladders(x):
    #usage of arrays/lists according to the project requirements
    lad1 = [1,4,9,28,21,51,80,72]
    lad2 = [38,14,31,84,42,67,99,91]
    global idn, val, idn1, val1
    if x in lad1:
        idn = lad1.index(x)
        val = lad2[idn]
        return val
    else:
        return x

#function to find if the user has found a snake
def snakes(x):
    #usage of arrays/lists according to the project requirements
    sna1 = [17,54,62,64,87,93,95,98]
    sna2 = [7,34,19,60,36,73,75,79]
    global idn, val, idn1, val1
    if x in sna1:
        idn1 = sna1.index(x)
        val1 = sna2[idn1]
        return val1
    else:
        return x

#function for the dice movement   
def dice(d):
    if d == 1:
        d = d1
    elif d == 2:
        d = d2
    elif d == 3:
        d = d3
    elif d == 4:
        d = d4
    elif d == 5:
        d = d5
    elif d == 6:
        d = d6

    time_clock = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time_clock < 1000:
        display.blit(d, (300, 500))
        pygame.display.update()

#adding the buttons which is necessary for the function
# of mute and unmute music and show credits
def button2(t, xm, ym, x, y, wid, hei, int, after, fast):
    # mouse position
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(display, after, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(display, int, [x, y, wid, hei])
    msg_display_scr(t, (x + wid + x) / 2, (y + hei + y) / 2, fast)


# Buttons for playing:
def button1(t, xm, ym, x, y, wid, hei, int, after, fast):
    # mouse position
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(display, after, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(display, after, [x, y, wid, hei])
    msg_display_scr(t, (x + wid + x) / 2, (y + hei + y) / 2, fast)


#function for each turn of the user
def turn(sc, lefted, section):
    d = randint(1, 6)
    if d == 6:
        six = True
    else:
        six = False
    p = dice(d)
    sc += d
    if sc <= 100:
        #calling the fuction to check if the player has found a ladder
        laddle = ladders(sc)
        if laddle != sc:
            lefted = True
            pygame.mixer.Sound.play(ladder)
            time_clock = pygame.time.get_ticks()
            sc = laddle
        #calling the fuction to check if the player has found a snake
        sink = snakes(sc)
        if sink != sc:  
            section = True
            pygame.mixer.Sound.play(snake_sound)
            sc = sink
    # checks if player score is not grater than 100
    else:  
        sc -= d
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 1500:
            msg_display1_scr("Can't move!", 650, 50, 35, black_c)
            pygame.display.update()
    return sc, lefted, section, six

#Function to Quit the Game
def Quit():
    pygame.quit()
    quit()


# Buttons:
def button(t, xm, ym, x, y, wid, hei, int, after, fast, best):
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(display, after, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if best == 1:
                choice()
            elif best == 5:
                return 5
            elif best == 0:
                Quit()
            elif best == "s" or best == 2 or best == 3 or best == 4:
                return best
            elif best == 7:
                choice()
            else:
                return True

    else:
        pygame.draw.rect(display, after, [x, y, wid, hei])
    msg_display_scr(t, (x + wid + x) / 2, (y + hei + y) / 2, fast)


def introduction():
    time_clock = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time_clock < 2500:
        display.blit(initial_background, (0, 0))
        pygame.display.update()
    while True:
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            display.blit(initial_background1, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            display.blit(initial_background2, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            display.blit(initial_background3, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            display.blit(initial_background4, (0, 0))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
        pygame.display.update()


def creditation():
    while True:
        display.blit(creditations1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if button("Back", mouse[0], mouse[1], scr_width / 2 - 100, 700, 200, 50, red_c2, blue_red, 25, 20):
            main_menu()

        pygame.display.update()


# Main Menu
def main_menu():
    pygame.mixer.music.play(-1)

    m = True
    while m:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        display.blit(menu_background, (0, 0))
        button("Play", mouse[0], mouse[1], (scr_width / 2 - 100), (scr_height / 2), 200, 100, green_c2,
               blue_green, 60, 1)

        button("Quit", mouse[0], mouse[1], (scr_width / 2 - 100), (scr_height / 2) + 200, 200, 100, red_c2,
               blue_red, 60, 0)

        mouse = pygame.mouse.get_pos()
        if button2("Mute Music", mouse[0], mouse[1], 1166, 0, 200, 50, purple_c, blue_purple, 25):
            pygame.mixer.music.pause()
        if button2("Play Music", mouse[0], mouse[1], 1166, 75, 200, 50, purple_c, blue_purple, 25):
            pygame.mixer.music.unpause()
        if button2("Credits", mouse[0], mouse[1], 1166, 150, 200, 50, purple_c, blue_purple, 25):
            creditation()

        pygame.display.update()


# Options Menu:
def choice():
    f = True
    while f == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        best1 = best2 = best3 = best4 = best5 = -1
        display.blit(menu_background, (0, 0))
        # Single player button
        best1 = button("Single Player", mouse[0], mouse[1], (scr_width / 2 - 150), 250, 300, 50, green_c2,
                       blue_green, 30, "s")
        # 2 player button
        best2 = button("2 Players", mouse[0], mouse[1], (scr_width / 2) - 150, 350, 300, 50, green_c2,
                       blue_green, 30, 2)
        # 3 player
        best3 = button("3 Players", mouse[0], mouse[1], (scr_width / 2) - 150, 450, 300, 50, green_c2,
                       blue_green, 30, 3)
        # 4 player
        best4 = button("4 Players", mouse[0], mouse[1], (scr_width / 2) - 150, 550, 300, 50, green_c2,
                       blue_green, 30, 4)
        # Back button
        best5 = button("Back", mouse[0], mouse[1], 0, 650, 200, 50, red_c2, blue_red, 30, 5)
        if best5 == 5:
            main_menu()
        if best1 == "s":
            playing(21)
        if best2 == 2:
            playing(2)
        if best3 == 3:
            playing(3)
        if best4 == 4:
            playing(4)

        pygame.display.update()


def playing(best):
    best6 = -1
    time1 = 3000
    if best6 == 7:
        choice()
    display.blit(post, (0, 0))
    display.blit(game_board, (scr_width / 2 - 250, scr_height / 2 - 250))
    xcr = xcy = xcg = xcb = 406 - 25
    ycr = ycy = ycg = ycb = 606 - 25
    display.blit(red_c, (xcy, ycy))
    if 5 > best > 1 or best == 21:
        display.blit(yellow_c, (xcy, ycy))

    if 5 > best > 2 or best == 21:
        display.blit(green_c, (xcg, ycg))

    if 5 > best > 2:
        display.blit(blue_c, (xcb, ycb))
    gamer1 = "Player 1"
    gamer1score = 0
    if best == 21:
        gamer2 = "Computer"
        gamer2score = 0
    if 5 > best > 1:
        gamer2 = "Player 2"
        gamer2score = 0
    if 5 > best > 2:
        gamer3 = "Player 3"
        gamer3score = 0
    if 5 > best > 3:
        gamer4 = "Player 4"
        gamer4score = 0
    tips = 1
    play = True
    while True:
        less = False
        set = False
        time1 = 3000
        display.blit(post, (0, 0))
        display.blit(game_board, (scr_width / 2 - 250, scr_height / 2 - 250))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        if best == 21:
            if button1("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, red_c, grey_c, 30):
                if tips == 1:
                    gamer1score, less, set, six = turn(gamer1score, less, set)
                    if not six:
                        tips += 1
                    xcr, ycr = movement(gamer1score)
                    if gamer1score == 100:
                        time1 = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            msg_display1_scr("Player 1 Wins", 650, 50, 50, blue_c)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break

            button1("Computer", mouse[0], mouse[1], 400, 700, 200, 50, yellow_c, grey_c, 30)
            if True:
                if tips == 2:
                    gamer2score, less, set, six = turn(gamer2score, less, set)
                    xcy, ycy = movement(gamer2score)
                    if not six:
                        tips += 1
                        if best < 3 or best == 21:
                            tips = 1

                    if gamer2score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            msg_display1_scr("Computer Wins", 650, 50, 50, black_c)
                            pygame.mixer.Sound.play(lose)
                            pygame.display.update()
                        break
        if 5 > best > 1:
            if button1("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, red_c, grey_c, 30):
                if tips == 1:
                    gamer1score, less, set, six = turn(gamer1score, less, set)
                    xcr, ycr = movement(gamer1score)
                    if not six:
                        tips += 1
                    if gamer1score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            msg_display1_scr("Player 1 Wins", 650, 50, 50, black_c)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break

            if button1("Player 2", mouse[0], mouse[1], 400, 700, 200, 50, yellow_c, grey_c, 30):
                if tips == 2:
                    gamer2score, less, set, six = turn(gamer2score, less, set)
                    xcy, ycy = movement(gamer2score)
                    if not six:
                        tips += 1
                        if best < 3:
                            tips = 1

                    if gamer2score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            msg_display1_scr("Player 2 Wins", 650, 50, 50, black_c)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break

        if 5 > best > 2:
            if button1("Player 3", mouse[0], mouse[1], 700, 700, 200, 50, green_c, grey_c, 30):
                if tips == 3:
                    gamer3score, less, set, six = turn(gamer3score, less, set)
                    xcg, ycg = movement(gamer3score)
                    if not six:
                        tips += 1
                        if best < 4:
                            tips = 1

                    if gamer3score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            msg_display1_scr("Player 3 Wins", 650, 50, 50, black_c)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break

        if 5 > best > 3:
            if button1("Player 4", mouse[0], mouse[1], 1000, 700, 200, 50, blue_c, grey_c, 30):
                if tips == 4:
                    gamer4score, less, set, six = turn(gamer4score, less, set)
                    xcb, ycb = movement(gamer4score)
                    if not six:
                        tips += 1
                        if best < 5:
                            tips = 1

                    if gamer4score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            msg_display1_scr("Player 4 Wins", 650, 50, 50, black_c)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break

        best6 = button("Back", mouse[0], mouse[1], 0, 0, 200, 50, red_c, blue_red, 30, 7)
        display.blit(red_c, (xcr, ycr))
        if 5 > best > 1 or best == 21:
            display.blit(yellow_c, (xcy + 2, ycy))

        if 5 > best > 2:
            display.blit(green_c, (xcg + 4, ycg))

        if 5 > best > 3:
            display.blit(blue_c, (xcb + 6, ycb))

        if less:
            time_clock = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time_clock < 2000:
                msg_display1_scr("There's a Ladder!", 650, 50, 35, black_c)
                pygame.display.update()
        if set:
            time_clock = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time_clock < 2000:
                msg_display1_scr("There's a Snake!", 650, 50, 35, black_c)
                pygame.display.update()

        time.tick(7)
        pygame.display.update()


introduction()
main_menu()
    #thank you ma'am for this opportunity ;)