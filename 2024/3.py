"""
Day 3 of Advent of Code 2024
"""
import re

with open("3.example", "r") as f:
    example_data = f.read().splitlines()

with open("3.example2", "r") as f:
    example_data_two = f.read().splitlines()

with open("3.data", "r") as f:
    data = f.read().splitlines()

def solve_part_one(lines: list[str]) -> int:
    total = 0
    pattern = re.compile(r"(mul\((\d{1,3})\,(\d{1,3})\))")
    for line in lines:
        # find all will return a tuple for each operation of ('mul(x,y)', 'x', 'y')
        operations = pattern.findall(line)
        for _, x, y in operations:
            total += int(x) * int(y)
    return total

assert solve_part_one(example_data) == 161
print(solve_part_one(data)) # 182780583

def solve_part_two(lines: list[str]) -> int:
    line = "".join(lines) # This tripped me up at first, I was processing each line separately, not as 1 input
    clean_pattern = re.compile(r"(don\'t\(\))(.*?do\(\)|.*)")
    cleaned_line = clean_pattern.sub('', line)
    total = solve_part_one([cleaned_line])
    return total

assert solve_part_two(example_data_two) == 48
print(solve_part_two(data)) # 90772405
