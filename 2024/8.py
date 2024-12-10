"""
Day 8 of Advent of Code 2024
"""
from collections import defaultdict

with open("8.example", "r") as f:
    example_data = f.read().splitlines()

with open("8.data", "r") as f:
    data = f.read().splitlines()


def get_grid_and_mapping(lines: list[str]) -> tuple[list[list[str]], dict[str, list[tuple[int, int]]]]:
    grid: list[list[str]] = []
    mapping: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for index, line in enumerate(lines):
        grid.append(list(line))
        for ch_index, ch in enumerate(line):
            if ch == '.':
                continue
            mapping[ch].append((index, ch_index))
    return grid, mapping


def solve_part_one(lines: list[str]) -> int:
    grid, mapping = get_grid_and_mapping(lines)
    grid_height = len(grid)
    grid_width = len(grid[0])
    anti_nodes = set()
    for ch, coords in mapping.items():
        for x1, y1 in coords:
            for x2, y2 in coords:
                if (x1, y1) == (x2, y2):
                    continue
                dx = (x2 - x1)
                dy = (y2 - y1)

                ax1 = x1 - dx
                ay1 = y1 - dy

                ax2 = x2 + dx
                ay2 = y2 + dy

                if 0 <= ax1 < grid_height and 0 <= ay1 < grid_width:
                    anti_nodes.add((ax1, ay1))
                if 0 <= ax2 < grid_height and 0 <= ay2 < grid_width:
                    anti_nodes.add((ax2, ay2))

    return len(anti_nodes)


def solve_part_two(lines: list[str]) -> int:
    grid, mapping = get_grid_and_mapping(lines)
    grid_height = len(grid)
    grid_width = len(grid[0])
    anti_nodes = set()

    for ch, coords in mapping.items():
        for x1, y1 in coords:
            for x2, y2 in coords:
                if (x1, y1) == (x2, y2):
                    continue

                anti_nodes.add((x1, y1))
                dx = (x2 - x1)
                dy = (y2 - y1)

                ax1 = x1 - dx
                ay1 = y1 - dy
                while 0 <= ax1 < grid_height and 0 <= ay1 < grid_width:
                    anti_nodes.add((ax1, ay1))
                    ax1 -= dx
                    ay1 -= dy

                ax2 = x2 + dx
                ay2 = y2 + dy
                while 0 <= ax2 < grid_height and 0 <= ay2 < grid_width:
                    anti_nodes.add((ax2, ay2))
                    ax2 += dx
                    ay2 += dy

    return len(anti_nodes)

assert solve_part_one(example_data) == 14
print(solve_part_one(data)) # 371

assert solve_part_two(example_data) == 34
print(solve_part_two(data)) # 1229
