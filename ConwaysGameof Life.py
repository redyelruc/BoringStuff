#  Conway's Game of Life
import random
import time
import copy

WIDTH = 60
HEIGHT = 20

#  Create a list of list for the cells:
next_cells = []
for x in range(WIDTH):
    column = []  # Creates a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#")  # adds a living cell
        else:
            column.append(" ")  # adds a dead cell
    next_cells.append(column)  # next_cells is a list of column lists
while True:  # main program loop
    print("\n\n\n\n\n")  # Separate each step with a new line
    current_cells = copy.deepcopy(next_cells)

    # Print current cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end="")  # Print the # or the space
        print()  # Prints a new line at the end of the row
    # Calculate the next steps cell based on current neighbours
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if current_cells[leftCoord][aboveCoord] == "#":
                numNeighbors += 1  # Top-left neighbor is alive.
            if current_cells[x][aboveCoord] == "#":
                numNeighbors += 1  # Top neighbor is alive.
            if current_cells[rightCoord][aboveCoord] == "#":
                numNeighbors += 1  # Top-right neighbor is alive.
            if current_cells[leftCoord][y] == "#":
                numNeighbors += 1  # Left neighbor is alive.
            if current_cells[rightCoord][y] == "#":
                numNeighbors += 1  # Right neighbor is alive.
            if current_cells[leftCoord][belowCoord] == "#":
                numNeighbors += 1  # Bottom-left neighbor is alive.
            if current_cells[x][belowCoord] == "#":
                numNeighbors += 1  # Bottom neighbor is alive.
            if current_cells[rightCoord][belowCoord] == "#":
                numNeighbors += 1  # Bottom-right neighbor is alive.
            # Set cell based on Conway's Game of Life rules:
            if current_cells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                next_cells[x][y] = "#"
            elif current_cells[x][y] == " " and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                next_cells[x][y] = "#"
            else:  # Everything else dies or stays dead:
                next_cells[x][y] = " "
    time.sleep(1)  # Add a 1-second pause to reduce flickering.
