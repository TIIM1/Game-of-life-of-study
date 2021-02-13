from random import randint
from copy import deepcopy

world_size = 16
populations = 256

world = [[] for _ in range(world_size)]
for i in range(world_size):
    for j in range(world_size):
        world[i].append(randint(0, 1))

new_world = deepcopy(world)


for _ in range(populations):
    for x in range(world_size):
        for y in range(world_size):
            alives_in_area = 0
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if i != 0 or j != 0:
                        if (
                            world[(y - 1 + j + world_size) % world_size][
                                (x - 1 + i + world_size) % world_size
                            ]
                            == 1
                        ):
                            alives_in_area += 1
            if alives_in_area == 3 or alives_in_area == 2:
                new_world[x][y] = 1
            else:
                new_world[x][y] = 0
    for i in range(world_size):
        for i in range(world_size):
            if new_world[i][j] == 1:
                print(f"\N{MEDIUM BLACK CIRCLE}", end="")
            else:
                print(f"\N{MEDIUM WHITE CIRCLE}", end="")
        print("")
    print("")
