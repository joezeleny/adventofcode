"""
Day 6 of Advent of Code 2024
"""
from copy import deepcopy
from enum import Enum
from itertools import cycle

with open("6.example", "r") as f:
    example_data = f.read().splitlines()

with open("6.data", "r") as f:
    data = f.read().splitlines()

class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)


class LoopError(Exception):
    pass


def get_grid_and_position(lines: list[str]) -> tuple[list[list[str]], tuple[int, int]]:
    grid: list[list[str]] = []
    position: tuple[int, int] = (0, 0)
    for index, line in enumerate(lines):
        grid.append(list(line))
        try:
            position = (index, line.index('^'))
        except ValueError:
            pass
    return grid, position


def get_unique_positions(grid: list[list[str]], position: tuple[int, int], log=False) -> set[tuple[int, int]]:
    direction = cycle(list(Direction))
    facing = next(direction)
    unique_positions = set([position])
    obstacles: dict[tuple[int, int], int] = {}
    while True:
        try:
            x, y = (position[0] + facing.value[0], position[1] + facing.value[1])
            if x < 0 or y < 0:
                # Guard left the map (up or left)
                raise IndexError()
            while grid[x][y] == '#':
                if (x,y) in obstacles and obstacles[(x,y)] == len(unique_positions):
                    # Guard already saw this obstacle and hasn't visited a new location since the last time, he's stuck
                    raise LoopError()
                obstacles[(x,y)] = len(unique_positions)
                facing = next(direction)
                x, y = (position[0] + facing.value[0], position[1] + facing.value[1])
                if x < 0 or y < 0:
                    # Guard left the map (up or left)
                    raise IndexError()
            position = (x, y)
            unique_positions.add(position)
        except IndexError:
            # Guard left the map (down or right)
            break
    return unique_positions


def solve_part_one(lines: list[str]) -> int:
    grid, position = get_grid_and_position(lines)
    unique_positions = get_unique_positions(grid, position)
    return len(unique_positions)


def solve_part_two(lines: list[str]) -> int:
    obstacles = 0
    grid, position = get_grid_and_position(lines)
    unique_positions = get_unique_positions(grid, position)
    unique_positions.remove(position)
    for x, y in unique_positions:
        new_grid = deepcopy(grid)
        new_grid[x][y] = '#'
        try:
            get_unique_positions(new_grid, position,log=True)
        except LoopError:
            obstacles += 1
    return obstacles


assert solve_part_one(example_data) == 41
print(solve_part_one(data)) # 5101

assert solve_part_two(example_data) == 6
print(solve_part_two(data)) # 1951
