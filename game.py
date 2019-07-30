from time import sleep
from os import system

height = 14
width = 14

DEAD = 0
ALIVE = 1

start_area = [[DEAD for x in range(width)] for y in range(height)]

start_area[5][5] = ALIVE
start_area[5][6] = ALIVE
start_area[5][7] = ALIVE

start_area[8][5] = ALIVE
start_area[8][6] = ALIVE
start_area[8][7] = ALIVE


start_area[6][5] = ALIVE
start_area[6][7] = ALIVE


start_area[7][5] = ALIVE
start_area[7][7] = ALIVE


def print_area(area):
    for i, h in enumerate(area):
        for j in range(len(h)):
            value = area[i][j]
            if value == ALIVE:
                print(f"\x1b[0;30;43m{value}\x1b[0m", end=" ")
            else:
                print(value, end=" ")
        print()


def _count_alived_neighborhood(area, x, y):
    neighborhood = [
        area[x + 1][y],
        area[x - 1][y],
        area[x][y - 1],
        area[x][y + 1],
        area[x + 1][y + 1],
        area[x - 1][y - 1],
        area[x + 1][y - 1],
        area[x - 1][y + 1],
    ]

    return neighborhood.count(ALIVE)


def _should_be_resurrected(area, x, y):
    return _count_alived_neighborhood(area, x, y) == 3


def _should_be_killed(area, x, y):
    return _count_alived_neighborhood(area, x, y) not in [2, 3]


def calculate_next_field_state(area, x, y):
    try:
        current_state = area[x][y]
        if current_state == DEAD and _should_be_resurrected(area, x, y):
            return ALIVE
        elif current_state == ALIVE and _should_be_killed(area, x, y):
            return DEAD
        else:
            return current_state
    except IndexError as x:
        return None


def process_next_generation(area):
    new_area = [[DEAD for x in range(width)] for y in range(height)]
    print_area(area)

    for i, h in enumerate(area):
        for j in range(len(h)):
            new_state = calculate_next_field_state(area, i, j)
            if new_state:
                new_area[i][j] = new_state
    print()
    return new_area


while True:
    system("clear")
    start_area = process_next_generation(start_area)
    sleep(1)
