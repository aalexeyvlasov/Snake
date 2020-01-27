import pygame
import time

pygame.mixer.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")


flag_game = True

x_coord = 45
y_coord = 45
head = [x_coord, y_coord]
x_counter = 0
y_counter = 0

while flag_game:

    #для выхода при нажатии крестика
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag_game = False
#    i = 0
#    while i< 200:
#
#        x_coord = 45 + i
#        y_coord = 45 + i
#
#        i = i+1


#    head = [x_coord, y_coord]
    window.fill(pygame.Color("Black"))
    pygame.draw.rect(window, pygame.Color("Green"), pygame.Rect(head[0], head[1], 10, 10))

    #-->
    if head[0] < 490 and x_counter == 0 and y_counter == 0:
        head[0] += 25
        #head[1] += 25
    else:
        x_counter = 1
        y_counter = 0

    #|
    if head[1] < 480 and x_counter == 1 and y_counter == 0:
        head[1] += 25
        #head[1] -= 25
    else:
        x_counter = 1
        y_counter = 1


    if head[0] > 10 and x_counter == 1 and y_counter == 1:
        head[0] -= 25
        #head[1] -= 25
    else:
        x_counter = 0
        y_counter = 1

    if head[1] > 10 and x_counter == 1 and y_counter == 0:
        head[1] -= 25
        #head[1] -= 25
    else:
        x_counter = 0
        y_counter = 0

    time.sleep(0.2)



    pygame.display.flip()