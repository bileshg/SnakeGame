# Snake Game

This is a simple Snake game implemented in Python using the Pygame library. The game features a snake that moves around the screen, eating food to grow longer. The game ends if the snake runs into itself or the edges of the screen.

## Requirements

- Python 3.x
- Pygame
- Tkinter (for message boxes)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/bileshg/SnakeGame.git
    cd SnakeGame
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To start the game, run the following command:
```sh
python src/main.py
```

## Controls

- **Arrow Keys / WASD**: Control the direction of the snake
- **ESC**: Pause the game and show a quit confirmation dialog

## Game Features

- **Grid Drawing**: The game grid is drawn on the screen.
- **Random Food Placement**: Food appears at random locations on the grid.
- **Score Display**: The current score is displayed at the top of the screen.
- **Game Over Handling**: The game shows a message box when the player wins or loses, asking if they want to play again.

## Project Structure

- `engine.py`: Contains the main game logic and functions.
- `src/main.py`: Entry point of the game.
- `src/utils/config.py`: Configuration file for game settings.
- `src/game/direction.py`: Direction enumeration for snake movement.
- `src/game/snake.py`: Snake class definition.
- `src/game/food.py`: Food class definition.
