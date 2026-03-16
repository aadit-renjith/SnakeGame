import asyncio
import pygame
from settings import *
from game_engine import game

async def menu():

    options = ["Player Mode", "AI Mode", "Quit"]
    level_options = ["Easy","Medium","Hard"]

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
        await asyncio.sleep(0)

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

                        await game(mode,level)

                        selecting_level = False
                        index = 0