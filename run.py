import random

# Define Constants
GRID_SIZE = 5
SHIP_COUNT = 3

# Function to create the game grid
def create_grid(size):
    return [['~' for _ in range(size)] for _ in range(size)]

# Function to print the game grid
def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

# Function to randomly place ships on the grid
def place_ships(grid, count):
    ships = []
    while len(ships) < count:
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if grid[x][y] == '~':
            grid[x][y] = 'S'
            ships.append((x, y))
    return ships


