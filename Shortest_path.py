# in this project we program the A* algorithm, an algorithm that finds the shortest path between 2 points
# given terrain geometry

import pygame
import math
from queue import PriorityQueue


# this is will be our windowm
WIDTH = 600
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Finding the shortest path")

# to make things more apparent we will define some colors

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Point:
    def __init__(self, row, column, width, totalRows):
        self.row = row
        self.column = column
        self.x = row * width
        self.y = column * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.totalRows = totalRows

    def get_position(self): # returns the spot position if we need
        return self.row, self.column

    def viewed(self): # did we check this spot
        return self.color == RED # if it was checked then it turns RED

    def consider(self): # if the algorithm considers the point to be part on the shortest path
        return self.color == GREEN

    def barrier(self): # if the point can't be trespassed
        return self.color == BLACK

    def start_point(self): # our starting point is orange colored
        return self.color == ORANGE

    def end_point(self): # our end point is turquoise
        return self.color == TURQUOISE

    # now we give the points their color

    def beginning(self): # when we go back to the beginning everything is WHITE
        self.color = WHITE

    def draw_viewed(self):
        self.color = RED

    def draw_consider(self):
        self.color = GREEN

    def draw_barrier(self):
        self.color = BLACK

    def draw_start_point(self):
        self.color = ORANGE

    def draw_end_point(self):
        self.color = TURQUOISE

    def draw_path(self):
        self.color = PURPLE

    def draw_window(self, window):
        pygame.draw.rect(window, self.color,(self.x, self.y, self.width, self.width))

    def update_neighbours(self,grid):
        self.neighbours = []
        if self.row < self.totalRows - 1 and not grid[self.row + 1][self.column].barrier(): # down
            self.neighbours.append(grid[self.row + 1][self.column])

        if self.row > 0 and not grid[self.row - 1][self.column].barrier(): # up
            self.neighbours.append(grid[self.row - 1][self.column])

        if self.column < self.totalRows - 1 and not grid[self.row][self.column + 1].barrier(): # rightt
            self.neighbours.append(grid[self.row][self.column + 1])

        if self.column > 0 and not grid[self.row][self.column - 1].barrier(): # left
            self.neighbours.append(grid[self.row][self.column - 1 ])

    def __lt__(self, other):
        return False

def H(point_1, point_2): # heuristic function which will be defined as
    x1, y1 = point_1
    x2, y2 = point_2
    return abs(x1 - x2) + abs(y1 - y2) # Manhattan distance


def reconstruct_path(origins, current, draw):
    while current in origins:
        current = origins[current]
        current.draw_path()
        draw()


def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    origins = {}
    G_score = {point: float("inf") for row in grid for point in row}
    G_score[start] = 0
    F_score = {point: float("inf") for row in grid for point in row}
    F_score[start] = H(start.get_position(), end.get_position())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)
        if current == end:
            reconstruct_path(origins,end,draw)
            end.draw_end_point()
            start.draw_start_point()
            return True
        for neighbour in current.neighbours:
            prov_G_score = G_score[current] + 1

            if prov_G_score < G_score[neighbour]:
                origins[neighbour] = current
                G_score[neighbour] = prov_G_score
                F_score[neighbour] = prov_G_score + H(neighbour.get_position(), end.get_position())
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((F_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.draw_consider()
        draw()
        if current != start:
            current.draw_viewed()
    return False



def grid_structure(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            point = Point(i, j, gap, rows)
            grid[i].append(point)
    return grid

def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (0,i * gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(window, GREY, (j * gap, 0), (j * gap, width))

def draw(window, grid, rows, width):
    window.fill(WHITE)

    for row in grid:
        for point in row:
            point.draw_window(window)

    draw_grid(window, rows, width)
    pygame.display.update()

def get_clickedPosition(position, rows, width):
    gap = width // rows
    y, x = position

    row = y // gap
    column = x // gap
    return row, column


def main(window, width):
    ROWS = 50
    grid = grid_structure(ROWS, width)

    start = None
    end = None

    run = True

    while run:
        draw(window,grid,ROWS,width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]: # LMB
                position = pygame.mouse.get_pos()
                row, column = get_clickedPosition(position,ROWS,width)
                point = grid[row][column]
                if not start and point != end:
                    start = point
                    start.draw_start_point()
                elif not end and point != start:
                    end = point
                    end.draw_end_point()
                elif point != start and point != end:
                    point.draw_barrier()

            elif pygame.mouse.get_pressed()[2]: # RMB
                position = pygame.mouse.get_pos()
                row, column = get_clickedPosition(position, ROWS, width)
                point = grid[row][column]
                point.beginning()
                if point == start:
                    start = None
                elif point == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for point in row:
                            point.update_neighbours(grid)
                    algorithm(lambda: draw(window,grid,ROWS,width), grid, start, end)

                # restart the algorithm with the same barrier points
                if event.key == pygame.K_r:
                    for row in grid:
                        for point in row:
                            if point.color == RED:
                                point.color = WHITE
                            elif point.color == GREEN:
                                point.color = WHITE
                            elif point.color == PURPLE:
                                point.color = WHITE
                # clear and restart
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = grid_structure(ROWS, width)








    pygame.quit()

main(WINDOW, WIDTH)


