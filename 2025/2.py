"""
Day 2 of Advent of Code 2025
"""
import re

with open("2.example", "r") as f:
    example_data = f.read().splitlines()

with open("2.data", "r") as f:
    data = f.read().splitlines()

def solve_part_one(lines: list[str]) -> int:
    line = lines[0] # only 1 line in this puzzle
    id_ranges = line.split(',')
    count = 0
    for id_range in id_ranges:
        start, end = id_range.split('-')
        check_ids = range(int(start), int(end)+1)
        for id in check_ids:
            str_id = str(id)
            if not len(str_id) % 2 == 0:
                continue
            mid = len(str_id) // 2
            if str_id[:mid] == str_id[mid:]:
                count += id
    return count

def solve_part_two(lines: list[str]) -> int:
    line = lines[0] # only 1 line in this puzzle
    id_ranges = line.split(',')
    count = 0
    pattern = re.compile(r'\b(\d+)\1+\b')
    for id_range in id_ranges:
        start, end = id_range.split('-')
        check_ids = range(int(start), int(end)+1)
        for id in check_ids:
            str_id = str(id)
            if pattern.match(str_id): # regex feels like cheating
                count += id

    return count

assert solve_part_one(example_data) == 1227775554
print(solve_part_one(data)) # 38437576669

assert solve_part_two(example_data) == 4174379265
print(solve_part_two(data)) # 49046150754
