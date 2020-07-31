# Our goal in this project is to create a sudoku solver

# sudoku rules

# in a game of sudoku the goal to complete is a matrix of size 9x9 with numbers from 1 to 9
# without repeating the same number in the column and row they are put and same square
# so in the next lines we will define the rules

# A sudoku game can be solved using the backtracking algorithm

# and it will work as follows:
# (1) pick a free cell (in our case free cells have a 0)
# (2) try a number from 1 to 9 on that cell
# (3) check if it fits, if it does go to (4) else go to (5)
# (4) back to the step 1
# (5) backtrack step back to step (2)

# lets look at our sudoku

sudoku_card = [
    [1, 0, 2, 0, 0, 0, 0, 0, 9],
    [0, 3, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 7, 0],
    [6, 0, 0, 0, 0, 8, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 6, 0, 0],
    [0, 5, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 3, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 1, 0, 4, 0, 0, 9, 0, 0]
]


def print_sudoku(card): # a sudoku in the form of list of lists must be fed to this function
    # all of length 9
    for i in range(len(card)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -")

        for j in range(len(card[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(card[i][j])
            else:
                print(str(card[i][j])+ " ",end="")

# print_sudoku(sudoku_card)

# check for repetitions of the number in the card

def valid_number(sudoku, number, position):

    # check row for if the number exists
    for i in range(len(sudoku[0])):
        if sudoku[position[0]][i] == number and position[1] != i: # exclude the cell we just filled
            return False

    # check column for if the number exists
    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == number and position[0] != i: # exclude the cell we just filled
            return False

    # check 3x3 square for if the number exists
    square_x = position[1] // 3
    square_y = position[0] // 3

    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            if sudoku[i][j] == number and (i, j) != position:
                return False

    return True


# we have to know what cells need to be filled so lets find those

def find_free(sudoku): # this function will find the free cells in our sudoku card
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j) # the position in our sudoku card that needs a number
    return None # every cell has a value diferent from zero


# we have all we need to play the game now so lets do it

def solver(sudoku):

    # print_sudoku(sudoku) # this would print each step the solver takes, remove the # at your own risk
    free = find_free(sudoku)
    if not free:
        return True
    else:
        row, column = free

    for i in range(1,10):
        if valid_number(sudoku, i, (row, column)):
            sudoku[row][column] = i
            if solver(sudoku):
                return True

            sudoku[row][column] = 0

    return False
    print("This sudoku card has no solution")

print_sudoku(sudoku_card)
solver(sudoku_card)
print()
print("This is your solution")
print_sudoku(sudoku_card)