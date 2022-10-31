#connect4 game
#Created by Christos Mappouras

#imported libraries
import sys
import math
import numpy
import pygame


#global variables
ROW = 6
COL = 7

BLUE = (0,0,235)
BLACK = (0,0,0)
PURPLE = (220,0,220)
GREEN = (0,220,0)
WHITE = (220,220,220)

SQUARES = 100

#RADIUS
RAD = int(SQUARES/2 - 10)

play = True
time = 0
round = 0

#FUNCTIONS
def drop(body, nextrow, droptocol, piece):
    body[nextrow][droptocol] = piece

def valid_spot(body, droptocol):
    return body[ROW-1][droptocol] == 0

def get_row(body, droptocol):
    for row in range(ROW):
        if body[row][droptocol] == 0:
            return row

#creates the board
def make_body():
    body = numpy.zeros((ROW, COL))
    return body

#flips the board
def connect4_body(body):
    flip = numpy.flip(body, 0)
    print(flip)

#when a player wins function
def win(body, piece):
    #horizontal wins
    for w in range(COL-3):
        for c in range(ROW):
            if body[c][w] == piece and body[c][w+1] == piece and body[c][w+2] == piece and body[c][w+3] == piece:
                return True

    #vertical wins
    for e in range(COL):
        for r in range(ROW-3):
            if body[r][e] == piece and body[r+1][e] == piece and body[r+2][e] == piece and body[r+3][e] == piece:
                return True

    #left diagonal
    for w in range(COL-3):
        for c in range(ROW-3):
            if body[c][w] == piece and body[c+1][w+1] == piece and body[c+2][w+2] == piece and body[c+3][w+3] == piece:
                return True

    #right diagonal
    for e in range(COL-3):
        for r in range(3, ROW):
            if body[r][e] == piece and body[r-1][e+1] == piece and body[r-2][e+2] == piece and body[r-3][e+3] == piece:
                return True

def tie(body):
    for e in range(COL):
        if round == 42:
            return True


#drawing board
def draw_body(body):
    for i in range(COL):
        for w in range(ROW):
            #draw - Drawing simple shapes
            #https://www.pygame.org/docs/ref/draw.html
            pygame.draw.rect(window, BLUE, (i*SQUARES, w*SQUARES+SQUARES, SQUARES, SQUARES) )
            pygame.draw.circle(window, BLACK, (int(i*SQUARES+SQUARES/2), int(w*SQUARES+SQUARES+SQUARES/2)), RAD)

    for i in range(COL):
        for w in range(ROW):
            if body[w][i] == 1:
                pygame.draw.circle(window, GREEN, (int(i*SQUARES+SQUARES/2), height-int(w*SQUARES+SQUARES/2)), RAD)
            elif body[w][i] == 2:
                pygame.draw.circle(window, PURPLE, (int(i*SQUARES+SQUARES/2), height-int(w*SQUARES+SQUARES/2)), RAD)
    pygame.display.update()



#initializing board
body = make_body()

#used pygame.org\docs to help me with pygame functions
#initializing pygame
pygame.init()

#width and height of window
width = COL * SQUARES
height = (ROW+1) * SQUARES

size = (width, height)

#Initializing a window to display
window = pygame.display.set_mode(size)
draw_body(body)
pygame.display.update()

connect4_font = pygame.font.SysFont("Arial", 75)
id = pygame.font.SysFont("Arial", 15)
#game starts
while play:

    #show name in game
    id_text = id.render("Created By Christos Mappouras", 1, GREEN)
    window.blit(id_text, (40,10))

    #checked pygames docs to make sure how to implement it
    #https://www.pygame.org/docs/ref/event.html#pygame.event.Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(window, BLACK, (0,0, width, SQUARES))
            x_position = event.pos[0]
            if time == 0:
                pygame.draw.circle(window, GREEN, (x_position, int(SQUARES/2)), RAD)
            else:
                pygame.draw.circle(window, PURPLE, (x_position, int(SQUARES/2)), RAD)
        pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(window, BLACK, (0,0, width, SQUARES))
            #MOUSEBUTTONDOWN attributes:   pos, button
            print(event.pos)

            #Player 1
            if time == 0:
                #print("Player 1:")
                #print("\n")
                x_position = event.pos[0]
                droptocol = int(math.floor(x_position/SQUARES))


                if valid_spot(body, droptocol):
                    nextrow = get_row(body, droptocol)
                    drop(body, nextrow, droptocol, 1)
                    round+=1

                    if win(body, 1):
                        text = connect4_font.render("Player 1 wins!", 1, GREEN)
                        print("\nPlayer 1 wins!")
                        window.blit(text, (40,10))
                        play = False

                    elif tie(body):
                        text2 = connect4_font.render("ITS A TIE", 1, GREEN)
                        window.blit(text2, (40,10))
                        play = False

            #Player 2
            elif time == 1:
                #print("Player 2:")
                #print("\n")
                x_position = event.pos[0]
                droptocol = int(math.floor(x_position/SQUARES))

                if valid_spot(body, droptocol):
                    nextrow = get_row(body, droptocol)
                    drop(body, nextrow, droptocol, 2)
                    round+=1

                    if win(body, 2):
                        text = connect4_font.render("Player 2 wins!", 1, PURPLE)
                        print("\nPlayer 2 wins!")
                        window.blit(text, (40,10))
                        play = False

                    elif tie(body):
                        text2 = connect4_font.render("ITS A TIE", 1, GREEN)
                        window.blit(text2, (40,10))
                        play = False

            connect4_body(body)
            draw_body(body)
            print("\n")

            #var time used to switch rounds between player 1 and 2
            time = (time + 1) % 2

            if play == False:
                pygame.time.wait(1000)
