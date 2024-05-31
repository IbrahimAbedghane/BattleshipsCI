import random

# Define Constants
GRID_SIZE = 5
SHIP_COUNT = 3
MAX_TURNS = 10

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
        except ValueError:
            print("Invalid input. Enter numbers only. Try again.")

def main():
    # Create the game grid and place ships
    grid = create_grid(GRID_SIZE)
    ships = place_ships(grid, SHIP_COUNT)
    
    print("Welcome to Battleships!")
    print("You have 10 turns to sink all ships.")
    
    turns = 0
    while turns < MAX_TURNS and ships:
        print_grid(grid)
        guess_x, guess_y = get_player_input()
        hit, message = make_guess(grid, ships, guess_x, guess_y)
        print(message)
        if hit:
            print(f"Ship sunk! {len(ships)} remaining.")
        turns += 1
    
    if not ships:
        print("Congratulations! You sank all the ships.")
    else:
        print("Game over. You've used all your turns.")
    
    print("Final grid:")
    print_grid(grid)

if __name__ == "__main__":
    main()


