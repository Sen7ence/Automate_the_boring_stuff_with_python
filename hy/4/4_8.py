# Conway's Game of Life
import random
import time
import copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = []  # create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')  # add a living cell
        else:
            column.append(' ')  # add a dead cell
    nextCells.append(column)  # add the column to nextCells

while True:
    print('\n\n\n\n\n')  # Separate each step with newlines
    currentCells = copy.deepcopy(nextCells)  # set currentCells to nextCells
    # print currentCells to the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')  # print the # or space
        print()  # print a newline after each row

    # Calculate the next step's cells based on currentCells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x-1) % WIDTH  # wrap around the edges of the screen
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            # Count the number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1  # top left neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1  # top neighbor is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1  # top right neighbor is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1  # left neighbor is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1  # right neighbor is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1  # bottom left neighbor is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1  # bottom neighbor is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1  # bottom right neighbor is alive

            # Set nextCells based on the number of neighbors:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # living cell with 2 or 3 neighbors stays alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # dead cell with 3 neighbors becomes alive
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '  # all other cells die or stay dead

    time.sleep(1)  # pause for a second before repeating the loop
