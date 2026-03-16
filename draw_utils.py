import pygame
from settings import *

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


def draw_food(food):

    pygame.draw.rect(screen,RED,(*food,BLOCK,BLOCK))


def draw_score(score, level):

    text = font.render(f"Score: {score}",True,WHITE)
    lvl = font.render(f"Level: {level}",True,WHITE)

    screen.blit(text,(10,10))
    screen.blit(lvl,(480,10))