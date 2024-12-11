"""
Day 9 of Advent of Code 2024
"""

with open("10.example", "r") as f:
    example_data = f.read().splitlines()

with open("10.data", "r") as f:
    data = f.read().splitlines()


def get_grid_and_trail_heads(lines: list[str]) -> tuple[list[list[int]], list[tuple[int, int]]]:
    grid: list[list[int]] = []
    trail_heads: list[tuple[int, int]] = []
    for index, line in enumerate(lines):
        grid.append([int(c) for c in line])
        for ch_index, ch in enumerate(line):
            if ch == '0':
                trail_heads.append((index, ch_index))
    return grid, trail_heads


def solve_part_one(lines: list[str]) -> int:
    grid, trail_heads = get_grid_and_trail_heads(lines)
    height = len(grid)
    width = len(grid[0])
    score = 0

    def check_x_y(x: int, y: int, level: int) -> set[tuple[int,int]]:
        if (x >= height or x < 0) or (y >= width or y < 0):
            return set()
        if grid[x][y] != level:
            return set()
        if level == 9:
            return set([(x,y)])
        level += 1
        return (
            check_x_y(x+1, y, level)
            | check_x_y(x, y+1, level)
            | check_x_y(x-1, y, level)
            | check_x_y(x, y-1, level)
        )

    for tx, ty in trail_heads:
        result = check_x_y(tx, ty, 0)
        score += len(result)

    return score


def solve_part_two(lines: list[str]) -> int:
    grid, trail_heads = get_grid_and_trail_heads(lines)
    height = len(grid)
    width = len(grid[0])
    score = 0

    def check_x_y(x: int, y: int, level: int) -> int:
        if (x >= height or x < 0) or (y >= width or y < 0):
            return 0
        if grid[x][y] != level:
            return 0
        if level == 9:
            return 1
        level += 1
        return sum([
            check_x_y(x+1, y, level),
            check_x_y(x, y+1, level),
            check_x_y(x-1, y, level),
            check_x_y(x, y-1, level),
        ])

    for tx, ty in trail_heads:
        result = check_x_y(tx, ty, 0)
        score += result

    return score


assert solve_part_one(example_data) == 36
print(solve_part_one(data)) # 472

assert solve_part_two(example_data) == 81
print(solve_part_two(data)) # 969
