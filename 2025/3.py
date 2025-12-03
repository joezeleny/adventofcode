"""
Day 3 of Advent of Code 2025
"""

with open("3.example", "r") as f:
    example_data = f.read().splitlines()

with open("3.data", "r") as f:
    data = f.read().splitlines()

def solve_part_one(lines: list[str]) -> int:
    total = 0
    for line in lines:
        digits = [int(i) for i in line]
        options = []
        for idx, digit in enumerate(digits):
            second_battery = max(digits[idx+1:]) if idx + 1 < len(digits) else ''
            options.append(int(f'{digit}{second_battery}'))
        total += max(options)
    return total

def next_max(digits: list, remaining: int) -> str:
    if remaining > len(digits):
        remaining = len(digits)
    if remaining == 0:
        return ''
    options = digits[:len(digits)-(remaining-1)] # need to leave enough to finish the 12 slots
    next_battery = max(options)
    next_idx = digits.index(next_battery)
    return f'{max(options)}{next_max(digits[next_idx+1:], remaining - 1)}'

def solve_part_two(lines: list[str]) -> int:
    total = 0
    for line in lines:
        digits = [int(i) for i in line]
        options = []
        for idx, digit in enumerate(digits):
            next_battery = next_max(digits[idx+1:], 11) if idx + 1 < len(digits) else ''
            options.append(int(f'{digit}{next_battery}'))
        total += max(options)
    return total


assert solve_part_one(example_data) == 357
print(solve_part_one(data)) # 17229

assert solve_part_two(example_data) == 3121910778619
print(solve_part_two(data)) # 170520923035051
