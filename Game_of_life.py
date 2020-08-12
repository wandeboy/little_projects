
import pygame
import numpy as np
import time

pygame.init()

#ancho y largo de la pantalla
width, height = 700, 700

#creacion de la pantalla
screen = pygame.display.set_mode((height, width))
#color oscuro
background_color = 25, 25, 25
screen.fill(background_color)

#cantidad de celdas en los ejes
number_of_cells_in_x_axis = 75
number_of_cells_in_y_axis = 75

#aritmetica de los lados de las celdas
cells_width = width / number_of_cells_in_x_axis
cells_height = height / number_of_cells_in_y_axis

#Estado de las celdas, Vivas = 1 -- Muertas = 0
game_state = np.zeros((number_of_cells_in_x_axis,
                       number_of_cells_in_y_axis))
"""
#Automata palo
game_state[5, 3] = 1
game_state[5, 4] = 1
game_state[5, 5] = 1
#Automata movil
game_state[21, 21] = 1
game_state[22, 22] = 1
game_state[22, 23] = 1
game_state[21, 23] = 1
game_state[20, 23] = 1
"""
#automata nave
game_state[1, 6] = 1
game_state[1, 7] = 1
game_state[1, 8] = 1
game_state[1, 20] = 1
game_state[1, 21] = 1
game_state[1, 22] = 1
game_state[2, 5] = 1
game_state[2, 9] = 1
game_state[2, 19] = 1
game_state[2, 23] = 1
game_state[3, 4 ] = 1
game_state[3, 5] = 1
game_state[3, 10] = 1
game_state[3, 18] = 1
game_state[3, 23] = 1
game_state[3, 24] = 1
game_state[4, 3] = 1
game_state[4, 5] = 1
game_state[4, 7] = 1
game_state[4, 8] = 1
game_state[4, 10] = 1
game_state[4, 11] = 1
game_state[4, 17] = 1
game_state[4, 18] = 1
game_state[4, 20] = 1
game_state[4, 21] = 1
game_state[4, 23] = 1
game_state[4, 25] = 1
game_state[5, 2] = 1
game_state[5, 3] = 1
game_state[5, 5] = 1
game_state[5, 10] = 1
game_state[5, 12] = 1
game_state[5, 13] = 1
game_state[5, 15] = 1
game_state[5, 16] = 1
game_state[5, 18] = 1
game_state[5, 23] = 1
game_state[5, 25] = 1
game_state[5, 26] = 1
game_state[6, 1] = 1
game_state[6, 6] = 1
game_state[6, 10] = 1
game_state[6, 13] = 1
game_state[6, 15] = 1
game_state[6, 18] = 1
game_state[6, 22] = 1
game_state[6, 27] = 1
game_state[7, 13] = 1
game_state[7, 15] = 1
game_state[8, 1] = 1
game_state[8, 2] = 1
game_state[8, 10] = 1
game_state[8, 11] = 1
game_state[8, 13] = 1
game_state[8, 15] = 1
game_state[8, 17] = 1
game_state[8, 18] = 1
game_state[8, 26] = 1
game_state[8, 27] = 1
game_state[9, 13] = 1
game_state[9, 15] = 1
game_state[10, 7] = 1
game_state[10, 8] = 1
game_state[10, 9] = 1
game_state[10, 19] = 1
game_state[10, 20] = 1
game_state[10, 21] = 1
game_state[11, 7] = 1
game_state[11, 11] = 1
game_state[11, 21] = 1
game_state[12, 7] = 1
game_state[12, 9] = 1
game_state[12, 14] = 1
game_state[12, 15] = 1
game_state[12, 16] = 1
game_state[13, 13] = 1
game_state[13, 16] = 1
game_state[13, 21] = 1
game_state[13, 22] = 1
game_state[14, 16] = 1
game_state[15, 12] = 1
game_state[15, 16] = 1
game_state[16, 12] = 1
game_state[16, 16] = 1
game_state[17, 7] = 1
game_state[17, 16] = 1
game_state[18, 7] = 1
game_state[18, 9] = 1
game_state[18, 13] = 1
game_state[18, 15] = 1
game_state[19, 7] = 1
game_state[19, 8] = 1
game_state[23, 5] = 1
game_state[24, 5] = 1
game_state[24, 7] = 1
game_state[25, 5] = 1
game_state[25, 6] = 1
game_state[29, 3] = 1
game_state[30, 3] = 1
game_state[30, 5] = 1
game_state[31, 3] = 1
game_state[31, 4] = 1
game_state[33, 7] = 1
game_state[33, 8] = 1
game_state[33, 9] = 1
game_state[34, 6] = 1
game_state[34, 9] = 1
game_state[35, 1] = 1
game_state[35, 9] = 1
game_state[36, 1] = 1
game_state[36, 3] = 1
game_state[36, 5] = 1
game_state[36, 9] = 1
game_state[37, 1] = 1
game_state[37, 2] = 1
game_state[37, 5] = 1
game_state[37, 9] = 1
game_state[38, 9] = 1
game_state[39, 6] = 1
game_state[39, 8] = 1



#control de la ejecucion del juego
pause_exect = False

#bucle de ejecucion
while True:

    new_game_state = np.copy(game_state)

    screen.fill(background_color)
    time.sleep(0.1)

    #registro del usuario
    event = pygame.event.get()

    for user_event in event:
        if user_event.type == pygame.KEYDOWN:
            pause_exect = not pause_exect
        
        mouse_click = pygame.mouse.get_pressed()

        if sum(mouse_click) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / cells_width)), int(np.floor(posY / cells_height))
            new_game_state[celX, celY] = not mouse_click[2]

    for y in range(number_of_cells_in_y_axis):
        for x in range(number_of_cells_in_x_axis):

            if not pause_exect:

                #calculamos los vecinos cercanos.
                number_of_neighbors = game_state[(x-1) % number_of_cells_in_x_axis,
                (y-1) % number_of_cells_in_y_axis] + \
                game_state[  x   % number_of_cells_in_x_axis,
                (y-1) % number_of_cells_in_y_axis] + \
                game_state[(x+1) % number_of_cells_in_x_axis,
                (y-1) % number_of_cells_in_y_axis] + \
                game_state[(x-1) % number_of_cells_in_x_axis,
                y % number_of_cells_in_y_axis] + \
                game_state[(x+1) % number_of_cells_in_x_axis,
                y % number_of_cells_in_y_axis ] + \
                game_state[(x-1) % number_of_cells_in_x_axis,
                (y+1) % number_of_cells_in_y_axis] + \
                game_state[  x   % number_of_cells_in_x_axis ,
                (y+1) % number_of_cells_in_y_axis] + \
                game_state[(x+1) % number_of_cells_in_x_axis,
                (y+1) % number_of_cells_in_y_axis]

                #regla 1  
                if game_state[x, y] == 0 and number_of_neighbors == 3:
                    new_game_state[x, y] = 1
                #regla 2      
                elif game_state[x, y] == 1 and (2 > number_of_neighbors or number_of_neighbors > 3):
                    new_game_state[x, y] = 0

            #creacion de celdas
            cell = [(int(  x   * cells_width),int(   y   * cells_height)),
                    (int((x+1) * cells_width),   int(y   * cells_height)),
                    (int((x+1) * cells_width), int((y+1) * cells_height)),
                    (int(  x   * cells_width), int((y+1) * cells_height))]

            #pantalla a dibujar, color, lados del poligono, grosor del borde
            if new_game_state[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), cell, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), cell, 0)

    #Actualizamos el estado del juego
    game_state = np.copy(new_game_state)

    #Actualizamos la pantalla
    pygame.display.flip()

