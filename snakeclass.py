import pygame
from squareclass import Square

class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, position):
        self.color = color
        self.head = Square(position)
        self.body.append(self.head)
        self.dir_x = 0 # default direction, at each update the snake will move 0 units on x, 1 unit on y
        self.dir_y = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    if self.dir_x !=1: # the snake can only go left if its not going right
                        self.dir_x = -1
                        self.dir_y = 0
                    self.turns[self.head.position[:]] = [self.dir_x, self.dir_y]
                elif keys[pygame.K_RIGHT]:
                    if self.dir_x != -1: # the snake can only go right if its not going left
                        self.dir_x = 1
                        self.dir_y = 0
                    self.turns[self.head.position[:]] = [self.dir_x, self.dir_y]
                elif keys[pygame.K_UP]:
                    if self.dir_y != 1: # the snake can only go up if its not going down
                        self.dir_x = 0
                        self.dir_y = -1
                    self.turns[self.head.position[:]] = [self.dir_x, self.dir_y]
                elif keys[pygame.K_DOWN]:
                    if self.dir_y != -1: # the snake can only go down if its not going up
                        self.dir_x = 0
                        self.dir_y = 1
                    self.turns[self.head.position[:]] = [self.dir_x, self.dir_y]

        for i, c in enumerate(self.body):
            p = c.position[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else: # here we check if we go outside the map
                if c.dir_x == -1 and c.position[0] <= 0: # if we are moving to the left
                    c.position = (c.rows-1, c.position[1]) # we will show up on the same row from the right side
                elif c.dir_x == 1 and c.position[0] >= c.rows - 1: # if we are moving the right
                    c.position = (0, c.position[1]) # we will show up on the same row from the left side
                elif c.dir_y == 1 and c.position[1] >= c.rows-1: # if we are moving down
                    c.position = (c.position[0], 0) # we will show up on the top
                elif c.dir_y == -1 and c.position[1] <= 0: # if we are moving up
                    c.position = (c.position[0], c.rows-1) # we will show up on the bottom
                else: # everything is normal
                    c.move(c.dir_x, c.dir_y)



    def reset(self, position):
        self.head = Square(position)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dir_x = 0
        self.dir_y = 1

    def addSquare(self): # we call this method when our snake hits the snake and
        tail = self.body[-1] # the tail is the last element on the snakes body
        tx, ty = tail.dir_x, tail.dir_y # this is the direction the tail is going
        if tx == 1 and ty == 0: # if the tail is going to the right
            self.body.append(Square((tail.position[0]-1, tail.position[1]))) # the snack goes to the position to the left
        elif tx == -1 and ty == 0: # if the tail is going to the left
            self.body.append(Square((tail.position[0] + 1, tail.position[1]))) # the snack goes to the position to the right
        elif tx == 0 and ty == 1: # if the tail is moving down
            self.body.append(Square((tail.position[0], tail.position[1] - 1))) # the snack goes to the top of the tail
        elif tx == 0 and ty == -1: # if the tail is moving up
            self.body.append(Square((tail.position[0], tail.position[1] + 1))) # the snack goes to the bottom of the tail
        self.body[-1].dir_x = tx # now the new tail is moving on the tx direction
        self.body[-1].dir_y = ty # now the new tail is moving on the tx direction


    def drawEyes(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface, False)
