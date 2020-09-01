import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from snakeclass import *



def drawGrid(w, rows, surface): # draws the world
    space = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x += space
        y += space
        # at each step of the loop a vertical line is drawn
        pygame.draw.line(surface, (0,0,0), (x,0), (x,w))
        # at each step of the loop a horizontal line is drawn
        pygame.draw.line(surface, (0, 0, 0), (0, y), (w, y))

def redraWindow(surface): # window updater
    global rows, width, ekans, snack
    surface.fill((152,251,152))
    ekans.drawEyes(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, snake):# creates snack in a position different from that of the snake
    positions = snake.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        # make sure a snack doesnt appear on top of the snake
        if len(list(filter(lambda z:z.position == (x,y), positions))) > 0:
            continue
        else:
            break
    return (x, y)

def messageBox(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():
    global rows, width, ekans, snack
    width = 500
    rows = 20
    window = pygame.display.set_mode((width, width))
    flag = True
    clock = pygame.time.Clock()
    ekans = Snake((0, 0, 0), (10, 10))
    snack = Square((random.randrange(rows), random.randrange(rows)), color=(128, 0, 128))
    while flag:
        pygame.time.delay(50) # this makes the snake not moving too fast
        clock.tick(10) # this makes the snake not moving too slow
        ekans.move()
        if ekans.body[0].position == snack.position: # if the position of the head of the snake is the same as the snack
            ekans.addSquare() # add it to the snakes body
            snack = Square(randomSnack(rows, ekans), color=(128,0,128)) # create a new snack
        # lets make sure than when we eat ourselves we die
        for i in range(len(ekans.body)):
            # if any part of our snakes body is in the list of the next body parts
            if ekans.body[i].position in list(map(lambda z:z.position,ekans.body[i+1:])):
                print("Your score was: ", len(ekans.body))
                messageBox("You lost!!!", "Try again anytime!")
                ekans.reset((10,10))
                break


        redraWindow(window)

main()