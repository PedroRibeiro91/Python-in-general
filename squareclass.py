import pygame

class Square(object):
    w = 500
    rows = 20

    def __init__(self, start, dir_x=1, dir_y=0, color=(0,0,0)):
        self.position = start
        self.dir_x = 1
        self.dir_y = 0
        self.color = color

    def move(self, dir_x, dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.position = (self.position[0] + self.dir_x, self.position[1] + dir_y)

    def draw(self, surface, eyes = False):
        distance = self.w // self.rows
        i = self.position[0]
        j = self.position[1]
        pygame.draw.rect(surface, self.color, (i*distance+1, j*distance+1, distance-2,distance-2))
        # the eyes of the snake
        if eyes:
            center = distance//2
            radius = 3
            circleMid = (i * distance + center-radius, j*distance + 8)
            circleMid2 = (i * distance + distance - radius * 2, j*distance + 8)
            pygame.draw.circle(surface, (255,255,255), circleMid, radius)
            pygame.draw.circle(surface, (255, 255, 255), circleMid2, radius)
