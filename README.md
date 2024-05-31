# Battleship Game

## Introduction
Welcome to the Battleship Game! This is a simple and intuitive text-based implementation of the classic Battleship game written using Python code. The objective is to sink all the hidden ships on the grid by making accurate guesses. You have a limited number of turns to achieve your mission!

## Features
- Grid-based gameplay: The game is played on a 5x5 grid where ships are randomly placed.
- Random placement of the ships: The ships are randomly placed on the grid at the start of each game to ensure a unique gaming experience.
- Player input: The game prompts the user to enter coordinates for their guesses, with player input being validated to ensure valid moves on the grid.
- Feedback System: The game provides the user with feedback on each turn, highlighting whether there was a direct hit or a miss.
Turn Limit: Users have a maximum of 10 turns to sink all the ships, adding a level of strategy and challenge to the gameplay.

## How to play
1. Setup: The game begins by creating a 5x5 grid and randomly placing 3 ships on the grid.
2. Turns: The player has 10 turns to guess the locations of the ships on the grid and for each turn:
    - Enter the X coordinate (0-4)
    - Enter the Y coordinate (0-4)
    - Receive feedback on whether the players guess was a hit or miss
3. Winning: If you sink all the ships within the allocated 10 turns you win the game! The game will display a congratulatory message to the player!
4. Losing: If the player does not sink all the ships within the allocated 10 turns, the game will end and you lose. The game will then display a final grid showing the locations of the remaining ships.