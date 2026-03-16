import pygame

WIDTH = 600
HEIGHT = 400
BLOCK = 20

BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
GRAY = (120,120,120)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Snake")

clock = pygame.time.Clock()

font = pygame.font.SysFont("arial",25)
big_font = pygame.font.SysFont("arial",40)