import pygame
import random
from collections import deque

pygame.init()

WIDTH = 600
HEIGHT = 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Snake")

clock = pygame.time.Clock()

BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
GRAY = (120,120,120)

font = pygame.font.SysFont("arial",25)
big_font = pygame.font.SysFont("arial",40)

# ------------------------------
# Utility
# ------------------------------

def random_pos():
    return [
        random.randrange(0, WIDTH, BLOCK),
        random.randrange(0, HEIGHT, BLOCK)
    ]

# ------------------------------
# AI Pathfinding (BFS)
# ------------------------------

def ai_move(head, food, snake, walls):

    queue = deque()
    visited = set()

    queue.append((head, []))

    moves = [
        (BLOCK,0),
        (-BLOCK,0),
        (0,BLOCK),
        (0,-BLOCK)
    ]

    while queue:

        pos, path = queue.popleft()

        if pos == food:
            return path[0] if path else (0,0)

        for move in moves:

            new = [pos[0]+move[0], pos[1]+move[1]]

            if (
                0 <= new[0] < WIDTH and
                0 <= new[1] < HEIGHT and
                tuple(new) not in visited and
                new not in snake and
                new not in walls
            ):
                visited.add(tuple(new))
                queue.append((new, path+[move]))

    return random.choice(moves)

# ------------------------------
# Draw functions
# ------------------------------

def draw_grid():

    for x in range(0, WIDTH, BLOCK):
        pygame.draw.line(screen,(40,40,40),(x,0),(x,HEIGHT))

    for y in range(0, HEIGHT, BLOCK):
        pygame.draw.line(screen,(40,40,40),(0,y),(WIDTH,y))


def draw_snake(snake):

    for i,seg in enumerate(snake):

        color = GREEN if i != len(snake)-1 else (0,200,0)

        pygame.draw.rect(screen,color,(*seg,BLOCK,BLOCK))


def draw_walls(walls):

    for w in walls:
        pygame.draw.rect(screen,GRAY,(*w,BLOCK,BLOCK))


def draw_score(score, level):

    text = font.render(f"Score: {score}",True,WHITE)
    lvl = font.render(f"Level: {level}",True,WHITE)

    screen.blit(text,(10,10))
    screen.blit(lvl,(480,10))

# ------------------------------
# Level system
# ------------------------------

def generate_walls(level):

    walls = []

    if level == "Easy":
        count = 4

    elif level == "Medium":
        count = 6

    else:
        count = 10

    for _ in range(count):
        walls.append(random_pos())

    return walls

# ------------------------------
# Game
# ------------------------------

def game(mode, level):

    snake = [[300,200]]

    direction = (BLOCK,0)

    food = random_pos()

    walls = generate_walls(level)

    score = 0

    speed = {
        "Easy":4,
        "Medium":5.5,
        "Hard":7
    }[level]

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

        pygame.draw.rect(screen,RED,(*food,BLOCK,BLOCK))

        draw_snake(snake)

        draw_walls(walls)

        draw_score(score,level)

        pygame.display.update()

        clock.tick(speed)

# ------------------------------
# Menu
# ------------------------------

def menu():

    options = [
        "Player Mode",
        "AI Mode",
        "Quit"
    ]

    level_options = [
        "Easy",
        "Medium",
        "Hard"
    ]

    selecting_level = False

    index = 0

    while True:

        screen.fill(BLACK)

        title = big_font.render("SNAKE GAME",True,WHITE)
        screen.blit(title,(200,50))

        if not selecting_level:

            for i,opt in enumerate(options):

                color = GREEN if i==index else WHITE

                txt = font.render(opt,True,color)

                screen.blit(txt,(240,150+i*40))

        else:

            for i,opt in enumerate(level_options):

                color = GREEN if i==index else WHITE

                txt = font.render(opt,True,color)

                screen.blit(txt,(240,150+i*40))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    index = (index-1)%3

                elif event.key == pygame.K_DOWN:
                    index = (index+1)%3

                elif event.key == pygame.K_RETURN:

                    if not selecting_level:

                        if options[index]=="Quit":
                            pygame.quit()
                            quit()

                        mode = "player" if index==0 else "ai"

                        selecting_level = True
                        index = 0

                    else:

                        level = level_options[index]

                        score = game(mode,level)

                        selecting_level = False
                        index = 0

menu()