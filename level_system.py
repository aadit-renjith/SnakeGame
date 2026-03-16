import random
from settings import WIDTH, HEIGHT, BLOCK

def random_pos():

    return [
        random.randrange(0, WIDTH, BLOCK),
        random.randrange(0, HEIGHT, BLOCK)
    ]


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


def get_speed(level):

    speeds = {
        "Easy": 4,
        "Medium": 5.5,
        "Hard": 7
    }

    return speeds[level]