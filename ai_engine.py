from collections import deque
import random
from settings import WIDTH, HEIGHT, BLOCK

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