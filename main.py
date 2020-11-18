import random
import time
import pygame
from pygame.locals import *

pygame.mixer.init()
pygame.mixer.music.load('assets/music.mp3')
pygame.mixer.music.play()

pygame.init()
display_width = 800
display_height = 600

# outrun inspired color scheme
bg = (13, 2, 33)
white = (236, 239, 244)
green = (77, 164, 166)
red = (255, 56, 100)
blue = (94, 129, 172)
cyan = (45, 226, 230)

car_width = 50
car_height = 100
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Synthwave")
clock = pygame.time.Clock()

carImg = pygame.image.load("assets/car.png")
car2Img = pygame.image.load("assets/taxi.png")
bgImg = pygame.image.load("assets/grid.png")
crash_img = pygame.image.load("assets/crash.png")
logo = pygame.image.load("assets/logo.png")

level_up_msgs = ["Nice Going", "ZOOOM ZOOOM", "Hit the nozzz bruh",
                 "oops! roadkill", "Eyes on the road", "Hit the nozz bruh", "oops! roadkill", "almost there", "we going too fast boi", "WOOAHH"]

# reads highscore from first line of the file
with open('highscore.txt') as f:
    highscore = f.readline().strip()
    # highscore is taken as 0 if  the file is empty
    if not highscore:
        highscore = "0"


def intro():
    intro = True
    menu1_x = 140
    menu1_y = 400
    menu2_x = 460
    menu2_y = 400
    menu1_width = 80
    menu2_width = 120
    menu_height = 50
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.set_icon(carImg)

        gameDisplay.fill(bg)
        # message_display("Synthave", 65, display_width / 2, display_height / 2)
        message_display("A driving game with chill vibes", 30, display_width/2, display_height/2 + 50)
        message_display("Highest Score: " + highscore, 30, display_width/2, display_height/2 + 200)
        # gameDisplay.blit(logo, ((display_width / 2) - 100, 10))
        gameDisplay.blit(logo, (display_width/2 - 180, 0))

        pygame.draw.rect(gameDisplay, green, (140, 400, 220, 50))
        pygame.draw.rect(gameDisplay, red, (460, 400, 180, 50))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if menu1_x < mouse[0] < menu1_x + menu1_width + 130 and menu1_y < mouse[1] < menu1_y + menu_height:
            pygame.draw.rect(gameDisplay, cyan, (140, 400, 220, 50))
            if click[0] == 1:
                intro = False

        if menu2_x < mouse[0] < menu2_x + menu2_width + 60 and menu2_y < mouse[1] < menu2_y + menu_height:
            pygame.draw.rect(gameDisplay, cyan, (460, 400, 180, 50))
            if click[0] == 1:
                pygame.quit()
                quit()

        message_display("Vroom Now", 40, menu1_x + 70 + menu1_width/2, menu1_y + menu_height/2)
        message_display("Run Away", 40, menu2_x + 30 + menu2_width/2, menu2_y + menu_height/2)

        pygame.display.update()
        clock.tick(60)

    gameloop()


def curr_score(count):
    font = pygame.font.SysFont("Arial", 40)
    text = font.render("Score : " + str(count), True, white)
    gameDisplay.blit(text, (0, 0))
    level = count/1000 + 1

    if level == 1:
        message_display("Level 1", 60, 680, 100)
        pygame.display.update()

    else:
        message_display("Level "+str(level), 60, display_width - 120, 100)
        message_display(level_up_msgs[level-2], 20, 680, 160)
    if count > 10000:
        update_highscore(count)
        message_display("Congratulations You Won!", 60, display_width/2, display_height/2)
        pygame.display.update()
        time.sleep(2)
        intro()


def draw_things(thingx, thingy, thing):
    gameDisplay.blit(thing, (thingx, thingy))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text, size, x, y):
    font = pygame.font.SysFont("Roboto", size)
    text_surface, text_rectangle = text_objects(text, font)
    text_rectangle.center = (x, y)
    gameDisplay.blit(text_surface, text_rectangle)


def crash(x, y):
    gameDisplay.blit(crash_img, (x, y))
    message_display("You Crashed!", 115, display_width/2, display_height/2 - 100)
    message_display("GAME OVER", 115, display_width/2, display_height/2 + 100)
    pygame.display.update()
    time.sleep(2)
    intro()


def get_speed(count):
    speed = 5
    if count > 1000 and count <= 5000:
        speed += count/1000
    elif count > 5000 and count <= 6000:
        speed = 10
    elif count > 6000 and count <= 9000:
        speed = 10 + (count - 5000)/2000
    elif count > 9000:
        speed = 12
    return speed


def update_highscore(count):
    if count > int(highscore):
        with open('highscore.txt', "w") as f:
            f.write(str(count))


def gameloop():
    count = 0
    thing_speed = get_speed(count)

    bg_x1 = (display_width / 2) - (360 / 2)
    bg_x2 = (display_width / 2) - (360 / 2)
    bg_y1 = 0
    bg_y2 = -600
    bg_speed_change = 0
    car_x = ((display_width / 2) - (car_width / 2))
    car_y = (display_height - car_height)
    car_x_change = 0
    road_start_x = (display_width / 2) - 180
    road_end_x = (display_width / 2) + 180

    thing_startx = random.randrange(road_start_x, road_end_x - car_width)
    thing_starty = -600
    thingw = 50
    thingh = 100
    gameExit = False

    while not gameExit:

        bg_speed = get_speed(count) + 3
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x_change = -5
                elif event.key == pygame.K_RIGHT:
                    car_x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_x_change = 0

        car_x += car_x_change

        if car_x > road_end_x - car_width:
            update_highscore(count)
            crash(car_x, car_y)

        if car_x < road_start_x:
            update_highscore(count)
            crash(car_x - car_width, car_y)

        if car_y < thing_starty + thingh:
            if car_x >= thing_startx and car_x <= thing_startx + thingw:
                update_highscore(count)
                crash(car_x - 25, car_y - car_height / 2)
            if car_x + car_width >= thing_startx and car_x + car_width <= thing_startx + thingw:
                update_highscore(count)
                crash(car_x, car_y - car_height / 2)

        gameDisplay.fill(bg)
        gameDisplay.blit(bgImg, (bg_x1, bg_y1))
        gameDisplay.blit(bgImg, (bg_x2, bg_y2))
        # gameDisplay.blit(logo, (10, (display_height / 2) - 100))
        # gameDisplay.blit(logo, (690, (display_height / 2) - 100))
        car(car_x, car_y)
        draw_things(thing_startx, thing_starty, car2Img)
        curr_score(count)
        count += 1
        thing_starty += thing_speed

        if thing_starty > display_height:
            thing_startx = random.randrange(
                road_start_x, road_end_x - car_width)
            thing_starty = -200

        bg_y1 += bg_speed
        bg_y2 += bg_speed
        thing_speed = get_speed(count)

        if bg_y1 >= display_height:
            bg_y1 = -600

        if bg_y2 >= display_height:
            bg_y2 = -600

        # if count > 5000:
        #     road_start_x = (display_width/2) - 25
        #     road_end_x = (display_width/2) + 25

        pygame.display.update()
        clock.tick(60)

intro()
