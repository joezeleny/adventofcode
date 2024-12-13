"""
Day 11 of Advent of Code 2024
"""
from collections import defaultdict

with open("11.example", "r") as f:
    example_data = f.read().splitlines()

with open("11.data", "r") as f:
    data = f.read().splitlines()


def update_stone(stone: str) -> list[str]:
    if stone == '0':
        return ['1']
    if len(stone) % 2 == 0:
        mid = len(stone) // 2
        return [stone[:mid], str(int(stone[mid:]))]
    return [str(int(stone) * 2024)]


def blink(stones: list[str]) -> list[str]:
    result = []
    for stone in stones:
        new_stones = update_stone(stone)
        result += new_stones
    return result

def blink_x_times(stones: list[str], iterations: int) -> int:
    for i in range(iterations):
        stones = blink(stones)
    return len(stones)

def solve_part_one(lines: list[str]) -> int:
    stones = lines[0].split(' ')
    total = 0
    for stone in stones:
        total += blink_x_times([stone], 25)
    return total

def solve_part_two(lines: list[str]) -> int:
    stones = lines[0].split(' ')
    stone_counts: dict[str, int] = defaultdict(int)
    for stone in stones:
        stone_counts[stone] += 1

    for i in range(75):
        new_counts: dict[str, int] = defaultdict(int)
        for stone, count in stone_counts.items():
            new_stones = update_stone(stone)
            for stone in new_stones:
                new_counts[stone] += count
        stone_counts = new_counts

    return sum(stone_counts.values())

assert solve_part_one(example_data) == 55312
print(solve_part_one(data)) # 200446
print(solve_part_two(data)) # 238317474993392
