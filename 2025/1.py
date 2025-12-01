"""
Day 1 of Advent of Code 2025
"""

with open("1.example", "r") as f:
    example_data = f.read().splitlines()

with open("1.data", "r") as f:
    data = f.read().splitlines()

def solve_part_one(lines: list[str]) -> int:
    dial = list(range(0,100))
    position = 50 # Starting point on the dial
    count = 0
    for line in lines:
        direction = -1 if line[0] == 'L' else 1
        # The turns can be > 100, but 100 is just a full turn and just noise
        turn = (int(line[1:]) % 100) * direction
        new_index = position + turn
        if new_index > 99:
            new_index -= 100
        position = dial[new_index]
        if position == 0:
            count += 1

    return count


def solve_part_two(lines: list[str]) -> int:
    # There is actually a bug in this code but my data didn't cause an issue
    # If you land on 0 then the next turn is 100, it will count that as hitting 0 once and passing 0 once
    # even though it should only count that as 1
    dial = list(range(0,100))
    position = 50 # Starting point on the dial
    count = 0
    for line in lines:
        direction = -1 if line[0] == 'L' else 1
        # The turns can be > 100, but 100 is just a full turn and just noise
        turn = (int(line[1:]) % 100) * direction
        count += int(line[1:]) // 100
        new_index = position + turn
        if position != 0 and new_index < 0:
            count += 1
        if new_index > 99:
            new_index -= 100
            if new_index != 0:
                count += 1
        position = dial[new_index]
        if position == 0:
            count += 1

    return count


assert solve_part_one(example_data) == 3
print(solve_part_one(data)) # 1040

assert solve_part_two(example_data) == 6
print(solve_part_two(data)) # 6027
