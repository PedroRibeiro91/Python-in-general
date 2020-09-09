import numpy as np
import pygame
import sys
import math

# connect 4
# our game will have 6 x 7 = 42 squares of 100 pixels each
ROWS = 6
COLUMNS = 7


# create the game grid
def create_grid():
    game_grid = np.zeros((ROWS,COLUMNS)) # initially everything is 0
    return game_grid


def drop_chip(game, row, column, chip):
    game[row, column] = chip


def validlocation(game, column): # can a player drop a chip in the selected column? yes if the that column isnt full
    return game[ROWS-1][column] == 0 # pretty simple lets test for the top row whichever column the player picks and checks
    # if its free


def get_next_open_row(game, column):
    for row in range(ROWS):
        if game[row][column] == 0:
            return row

# here is the problem the entry (0,0) is at the top left of our game matrix
# we want to set it at the lower left
# numpy has a method called flip that will do that for us


def reverse_game(game): # this will reverse the direction in which the matrix gets filled. Instead of top to bottom
    # it will go botto to top
    print(np.flip(game, 0))


def win_test(game, piece): # here we test if someone won
    # check for horizontal win
    for column in range(COLUMNS-3): # we cant connect 4 if we only have 3 open spaces
        # until column 4. If from column 4 we dont have a horizontal win the we cant have an horizontal win
        # for that row
        for row in range(ROWS):
            if game[row, column] == piece and game[row, column + 1] == piece and game[row, column + 2] == piece\
            and game[row, column+3] == piece:
                return True

    # check for vertical win
    for column in range(COLUMNS):
        # until column 4. If from column 4 we dont have a horizontal win the we cant have an horizontal win
        # for that row
        for row in range(ROWS-3): # we cant connect 4 if we only have 3 open spaces
            if game[row, column] == piece and game[row+1, column] == piece and game[row+2, column] == piece \
                    and game[row+3, column] == piece:
                return True

    # check for diagonal win with a "crescent slope"
    for column in range(COLUMNS-3): # from these positions we can have a connect 4 diagonal
        for row in range(ROWS-3):
            if game[row, column] == piece and game[row + 1, column + 1] == piece and game[row + 2, column + 2] == piece \
                    and game[row + 3, column + 3] == piece:
                return True
    # check for diagonal win with a "decrescent slope"
    for column in range(3, COLUMNS):  # from these positions we can have a connect 4 diagonal
        for row in range(3, ROWS):
            if game[row, column] == piece and game[row - 1, column + 1] == piece and game[row - 2, column + 2] == piece \
                    and game[row - 3, column + 3] == piece:
                return True


SQUARESIZE = 100
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW =(255, 255, 0)
RADIUS = int(SQUARESIZE/2 - 5) # is just because and will corresponds to the width of the game lines


def draw_game(board):
    for col in range(COLUMNS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE,\
                             (col * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(col * SQUARESIZE + SQUARESIZE/2),\
                                               int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), RADIUS)
    for col in range(COLUMNS):
        for r in range(ROWS):
            if board[r][col] == 1:
                pygame.draw.circle(screen, YELLOW, (int(col * SQUARESIZE + SQUARESIZE / 2), \
                                                   screen_height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][col] == 2:
                pygame.draw.circle(screen, RED, (int(col * SQUARESIZE + SQUARESIZE / 2), \
                                                    screen_height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()

game = create_grid()
reverse_game(game)
pygame.init()
screen_width = COLUMNS * SQUARESIZE
screen_height = (ROWS+1) * SQUARESIZE # we will need an extra row for the player to
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
draw_game(game)
pygame.display.update()


# game loop
game_over = False
turn = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            position_x = event.pos[0]  # stores the position of the click
            pygame.draw.rect(screen, BLACK, (0,0, screen_width, SQUARESIZE))
            if turn == 0:
                pygame.draw.circle(screen, YELLOW, (position_x, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, RED, (position_x, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            position_x = event.pos[0]  # stores the position of the click
            column = int(math.floor(position_x / SQUARESIZE))  # turn that click into an action
            # Ask player 1 play
            # this is our click tracker
            if turn == 0:
                # we need to let pygame know that where we click is where we want to drop the chip
                # that will correspond to an (x, y) position in our 700 x 700 pixel screen
                if validlocation(game, column):
                    row = get_next_open_row(game, column)
                    drop_chip(game, row, column, 1)
                    if win_test(game, 1):
                        print("Player 1 wins!!!")
                        game_over = True
            # Aks player 2 play
            else:
                if validlocation(game, column):
                    row = get_next_open_row(game, column)
                    drop_chip(game, row, column, 2)
                    if win_test(game, 1):
                        print("Player 2 wins!!!")
                        game_over = True
            draw_game(game)
            reverse_game(game) # updates the game
            turn += 1 # passed the turn to the next player
            turn = turn % 2  # here we have our alternation between player 1 and player 2 turn
            if game_over:
                pygame.time.wait(3000) # 3000 milliseconds equal 3 seconds
            # one of the players win the game and the game closes 3 seconds after

