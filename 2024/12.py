"""
Day 12 of Advent of Code 2024
"""
from collections import defaultdict

with open("12.example", "r") as f:
    example_data = f.read().splitlines()

with open("12.data", "r") as f:
    data = f.read().splitlines()

def get_neighbors(
    plant: tuple[int, int],
    plants: set[tuple[int, int]],
    visited: set[tuple[int, int]]
) -> tuple[set[tuple[int, int, int]], set[tuple[int, int]]]:
    coords = [
        (plant[0], plant[1] - 1),
        (plant[0], plant[1] + 1),
        (plant[0] - 1, plant[1]),
        (plant[0] + 1, plant[1])
    ]
    neighbors: set[tuple[int, int, int]] = set()
    if plant in visited:
        return neighbors, visited
    visited.add(plant)
    sides = 0
    for coord in coords:
        if coord in plants:
            sides += 1
            coord_neighbors, v = get_neighbors(coord, plants, visited)
            neighbors |= (coord_neighbors)
            visited |= v
    neighbors.add((plant[0], plant[1], 4-sides))
    return neighbors, visited

def solve_part_one(lines: list[str]) -> int:
    total = 0
    mapping: dict[str, set[tuple[int, int]]] = defaultdict(set)
    for ri, row in enumerate(lines):
        for ci, column in enumerate(row):
            mapping[column].add((ri,ci))
    visited: set[tuple[int, int]] = set()
    for plant_type, plants in mapping.items():
        for plant in plants:
            neighbors: set[tuple[int, int, int]] = set()
            if plant in visited:
                continue
            neighbors, v = get_neighbors(plant, plants, visited)
            visited |= v
            if neighbors:
                area = len(neighbors)
                perimeter = sum([x[2] for x in neighbors])
                total += area * perimeter
    return total


assert solve_part_one(example_data) == 1930
print(solve_part_one(data)) # 1518548

"""
def solve_part_two(lines: list[str]) -> int:
    return 0

assert solve_part_two(example_data) ==
print(solve_part_two(data)) #
"""
