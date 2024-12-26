import sys
import pygame
import random

import tkinter as tk
from tkinter import messagebox

from src.utils.config import conf
from src.game.direction import Direction
from src.game.snake import Snake
from src.game.food import Food


def message_box(subject: str, content: str) -> bool:
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    response = messagebox.askyesno(subject, content)
    root.destroy()
    return response


def draw_grid(screen: pygame.Surface):
    screen.fill(conf.window.background.color)

    x = 0
    for _ in range(conf.game.cols):
        pygame.draw.line(screen, conf.window.grid.color, (x, 0), (x, conf.window.height))
        x += conf.block.width

    y = 0
    for _ in range(conf.game.rows):
        pygame.draw.line(screen, conf.window.grid.color, (0, y), (conf.window.width, y))
        y += conf.block.height


def random_empty_block(snake: Snake) -> tuple[int, int]:
    while True:
        x = random.randint(0, conf.game.cols - 1) * conf.block.width
        y = random.randint(0, conf.game.rows - 1) * conf.block.height

        if not any(block.x == x and block.y == y for block in snake.body):
            return x, y


def create_food(snake: Snake) -> Food:
    return Food(*random_empty_block(snake))


def end_game():
    pygame.quit()
    sys.exit()


def handle_events(snake: Snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game()
        if event.type == pygame.KEYDOWN:
            handle_keydown(event, snake)


def handle_keydown(event, snake: Snake):
    if event.key in [pygame.K_DOWN, pygame.K_s]:
        snake.set_direction(Direction.DOWN)
    elif event.key in [pygame.K_UP, pygame.K_w]:
        snake.set_direction(Direction.UP)
    elif event.key in [pygame.K_RIGHT, pygame.K_d]:
        snake.set_direction(Direction.RIGHT)
    elif event.key in [pygame.K_LEFT, pygame.K_a]:
        snake.set_direction(Direction.LEFT)
    elif event.key == pygame.K_ESCAPE:
        if response := message_box(
                'Quit!', 'Do you want to quit?'
        ):
            end_game()


def update_score(screen: pygame.Surface, font: pygame.font.Font, score_panel: pygame.Rect, snake: Snake):
    score = font.render(f"{len(snake.body) - 1}", True, conf.font.color)
    screen.blit(score, score_panel)


def game_loop(screen: pygame.Surface, font: pygame.font.Font, clock: pygame.time.Clock):
    score = font.render("0", True, conf.font.color)
    score_panel = score.get_rect(center=(conf.window.width / 2, conf.window.height / 20))

    snake = Snake()
    food = create_food(snake)

    draw_grid(screen)

    while True:
        clock.tick(conf.game.tick)

        if len(snake.body) == conf.game.cols * conf.game.rows:
            if response := message_box(
                    'Wow! You Won!', 'Do you want to play again?'
            ):
                snake.reset()
                food = create_food(snake)
            else:
                end_game()

        handle_events(snake)

        if snake.is_dead():
            if response := message_box(
                    'You Lost!', 'Do you want to play again?'
            ):
                snake.reset()
                food = create_food(snake)
            else:
                end_game()
        snake.move()

        draw_grid(screen)

        snake.draw(screen)
        food.draw(screen)

        update_score(screen, font, score_panel, snake)

        if snake.head.x == food.x and snake.head.y == food.y:
            snake.grow()
            food = create_food(snake)

        pygame.display.update()
