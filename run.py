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

# Function to handle player's guess
def make_guess(grid, ships, guess_x, guess_y):
    if (guess_x, guess_y) in ships:
        grid[guess_x][guess_y] = 'H'
        ships.remove((guess_x, guess_y))
        return True, "Hit!"
    else:
        grid[guess_x][guess_y] = 'M'
        return False, "Miss!"

# Function to get valid player input
def get_player_input():
    while True:
        try:
            x = int(input("Enter X coordinate (0-4): "))
            y = int(input("Enter Y coordinate (0-4): "))
            if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                return x, y
            else:
                print("Coordinates out of bounds. Try again.")


