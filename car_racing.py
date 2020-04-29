import pygame
from pygame.locals import *

import time
import random

pygame.init()
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

car_width = 50
car_height = 100
# pygame.mixer.music.load("Highway_to_hell.mp3")
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car Racing Game")
clock = pygame.time.Clock()


carImg = pygame.image.load("car1.png")
car2Img = pygame.image.load("car2.png")
bgImg = pygame.image.load("back2.jpg")
crash_img = pygame.image.load("crash.png")
logo = pygame.image.load("logo.png")


def intro():
    intro = True
    menu1_x = 200
    menu1_y = 400
    menu2_x = 500
    menu2_y = 400
    menu_width = 100
    menu_height = 50
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.set_icon(carImg)

        pygame.draw.rect(gameDisplay, black, (200, 400, 100, 50))
        pygame.draw.rect(gameDisplay, black, (500, 400, 100, 50))

        gameDisplay.fill(black)
        message_display("CAR RACING PROJECT", 65,
                        display_width / 2, display_height / 2)
        message_display("By Aaryamann and Ananya", 30,
                        display_width/2, display_height/2 + 70)
        message_display("S1", 45, display_width / 2, display_height / 2 + 130)
        gameDisplay.blit(logo, ((display_width / 2) - 100, 10))
        pygame.draw.rect(gameDisplay, green, (200, 400, 100, 50))
        pygame.draw.rect(gameDisplay, red, (500, 400, 100, 50))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if menu1_x < mouse[0] < menu1_x + menu_width and menu1_y < mouse[1] < menu1_y + menu_height:
            pygame.draw.rect(gameDisplay, blue, (200, 400, 100, 50))
            if click[0] == 1:
                intro = False
        if menu2_x < mouse[0] < menu2_x + menu_width and menu2_y < mouse[1] < menu2_y + menu_height:
            pygame.draw.rect(gameDisplay, blue, (500, 400, 100, 50))
            if click[0] == 1:
                pygame.quit()
                quit()

        message_display("Start", 40, menu1_x + menu_width /
                        2, menu1_y + menu_height / 2)
        message_display("Quit", 40, menu2_x + menu_width /
                        2, menu2_y + menu_height / 2)

        pygame.display.update()
        clock.tick(50)


def highscore(count):
    font = pygame.font.SysFont(None, 55)
    text = font.render("Score : " + str(count), True, white)
    gameDisplay.blit(text, (0, 0))
    if count > 1000 and count < 1200:
        message_display("Level 2", 60, display_width / 2, display_height / 2)
        pygame.display.update()
    elif count > 2000 and count < 2200:
        message_display("Level 3", 60, display_width / 2, display_height / 2)
        message_display("Nice Skills", 60, display_width /
                        2, display_height / 2 + 100)
    elif count > 3000 and count < 3200:
        message_display("Level 4", 60, display_width / 2, display_height / 2)
    elif count > 4000 and count < 4200:
        message_display("Level 5", 60, display_width / 2, display_height / 2)
        message_display("Keep Going!", 60, display_width /
                        2, display_height / 2 + 100)
    elif count > 5000 and count < 5200:
        message_display("Level 6", 60, display_width / 2, display_height / 2)
        message_display("The road is now narrower", 60,
                        display_width / 2, display_height / 2 + 100)
    elif count > 6000 and count < 6200:
        message_display("Level 7", 60, display_width / 2, display_height / 2)
    elif count > 7000 and count < 7200:
        message_display("Level 8", 60, display_width / 2, display_height / 2)
        message_display("WOAAH!", 60, display_width /
                        2, display_height / 2 + 100)
    elif count > 8000 and count < 8200:
        message_display("Level 9", 60, display_width / 2, display_height / 2)
        message_display("Almost there!", 60, display_width /
                        2, display_height / 2 + 100)
    elif count > 9000 and count < 9200:
        message_display("Level 10", 60, display_width / 2, display_height / 2)
    elif count > 10000:
        message_display("Congratulations You Won!", 60,
                        display_width / 2, display_height / 2)
        pygame.display.update()
        time.sleep(2)
        gameloop()


def draw_things(thingx, thingy, thing):
    gameDisplay.blit(thing, (thingx, thingy))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text, size, x, y):
    font = pygame.font.Font("freesansbold.ttf", size)
    text_surface, text_rectangle = text_objects(text, font)
    text_rectangle.center = (x, y)
    gameDisplay.blit(text_surface, text_rectangle)


def crash(x, y):
    gameDisplay.blit(crash_img, (x, y))
    message_display("You Crashed!", 115, display_width /
                    2, display_height / 2 - 100)
    message_display("GAME OVER", 115, display_width /
                    2, display_height / 2 + 100)
    pygame.display.update()
    time.sleep(2)
    gameloop()


def gameloop():
    # pygame.mixer.music.play(-1)
    bg_x1 = (display_width / 2) - (360 / 2)
    bg_x2 = (display_width / 2) - (360 / 2)
    bg_y1 = 0
    bg_y2 = -600
    bg_speed = 6
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
    thing_speed = 3
    count = 0
    gameExit = False

    while not gameExit:

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
            crash(car_x, car_y)
        if car_x < road_start_x:
            crash(car_x - car_width, car_y)

        if car_y < thing_starty + thingh:
            if car_x >= thing_startx and car_x <= thing_startx + thingw:
                crash(car_x - 25, car_y - car_height / 2)
            if car_x + car_width >= thing_startx and car_x + car_width <= thing_startx + thingw:
                crash(car_x, car_y - car_height / 2)

        gameDisplay.fill(black)
        gameDisplay.blit(bgImg, (bg_x1, bg_y1))
        gameDisplay.blit(bgImg, (bg_x2, bg_y2))
        gameDisplay.blit(logo, (10, (display_height / 2) - 100))
        gameDisplay.blit(logo, (display_width - 200 -
                                10, (display_height / 2) - 100))
        car(car_x, car_y)
        draw_things(thing_startx, thing_starty, car2Img)
        highscore(count)
        count += 1
        thing_starty += thing_speed

        if thing_starty > display_height:
            thing_startx = random.randrange(
                road_start_x, road_end_x - car_width)
            thing_starty = -200

        bg_y1 += bg_speed
        bg_y2 += bg_speed

        if bg_y1 >= display_height:
            bg_y1 = -600

        if bg_y2 >= display_height:
            bg_y2 = -600

        if count > 1000:
            thing_speed = 5
        if count > 2000:
            thing_speed = 7
        if count > 3000:
            thing_speed = 8
        if count > 4000:
            thing_speed = 9
        if count > 5000:
            thing_speed = 10
        if count > 6000:
            thing_speed = 10.5
        if count > 7000:
            thing_speed = 11
        if count > 8000:
            thing_speed = 11.5
        if count > 9000:
            thing_speed = 12
        if count > 5000:
            road_start_x = (display_width/2) - 25
            road_end_x = (display_width/2) + 25
        pygame.display.update()
        clock.tick(100)


intro()
gameloop()
