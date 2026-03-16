import pygame
from settings import *
from draw_utils import *
from ai_engine import ai_move
from level_system import random_pos, generate_walls, get_speed


def game(mode, level):

    snake = [[300,200]]
    direction = (BLOCK,0)

    food = random_pos()
    walls = generate_walls(level)

    score = 0
    speed = get_speed(level)

    paused = False

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    paused = not paused

                if mode == "player":

                    if event.key == pygame.K_LEFT and direction!=(BLOCK,0):
                        direction=(-BLOCK,0)

                    elif event.key == pygame.K_RIGHT and direction!=(-BLOCK,0):
                        direction=(BLOCK,0)

                    elif event.key == pygame.K_UP and direction!=(0,BLOCK):
                        direction=(0,-BLOCK)

                    elif event.key == pygame.K_DOWN and direction!=(0,-BLOCK):
                        direction=(0,BLOCK)

        if paused:
            continue

        head = snake[-1]

        if mode == "ai":
            direction = ai_move(head,food,snake,walls)

        new_head = [head[0]+direction[0], head[1]+direction[1]]

        if (
            new_head[0]<0 or new_head[0]>=WIDTH or
            new_head[1]<0 or new_head[1]>=HEIGHT or
            new_head in snake or
            new_head in walls
        ):
            return score

        snake.append(new_head)

        if new_head == food:

            food = random_pos()
            score += 1
            speed += 0.5

        else:
            snake.pop(0)

        screen.fill(BLACK)

        draw_grid()
        draw_food(food)
        draw_snake(snake)
        draw_walls(walls)
        draw_score(score, level)

        pygame.display.update()

        clock.tick(speed)