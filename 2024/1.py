"""
Day 1 of Advent of Code 2024
"""

with open("1.example", "r") as f:
    example_data = f.read().splitlines()

with open("1.data", "r") as f:
    data = f.read().splitlines()

def parse_lists(lines: list[str]) -> tuple[list[int], list[int]]:
    left = []
    right = []
    for line in lines:
        li, *_, ri = line.split(' ')
        left.append(int(li))
        right.append(int(ri))
    return left, right

def solve_part_one(lines: list[str]) -> int:
    total = 0
    left, right = parse_lists(lines)
    left = sorted(left)
    right = sorted(right)

    for i in range(len(left)):
        distance = abs(left[i] - right[i])
        total += distance
    return total

assert solve_part_one(example_data) == 11

print(solve_part_one(data))

def solve_part_two(lines: list[str]) -> int:
    score = 0
    left, right = parse_lists(lines)
    for item in left:
        score += item * right.count(item)
    return score

assert solve_part_two(example_data) == 31

print(solve_part_two(data))
