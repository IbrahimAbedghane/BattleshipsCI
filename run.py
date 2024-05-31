import random

# Define Constants
GRID_SIZE = 5

# Function to create the game grid
def create_grid(size):
    return [['~' for _ in range(size)] for _ in range(size)]
