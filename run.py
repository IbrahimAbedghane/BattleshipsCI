import random

# Define Constants
GRID_SIZE = 5

# Function to create the game grid
def create_grid(size):
    return [['~' for _ in range(size)] for _ in range(size)]

# Function to print the game grid
def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

