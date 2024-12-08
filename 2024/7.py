"""
Day 7 of Advent of Code 2024
"""
with open("7.example", "r") as f:
    example_data = f.read().splitlines()

with open("7.data", "r") as f:
    data = f.read().splitlines()

def check_equation(values: list[str], index: int, possible_totals: list[int]) -> bool:
    if index >= len(values):
        return False
    value = int(values[index])
    new_totals = []
    for total in possible_totals:
        can_multiply = total % value == 0
        if can_multiply:
            multiply_result = total // value
            if multiply_result == 1 and index == (len(values) - 1):
                return True
            new_totals.append(total // value)
        if (add_result := total - value) >= 0:
            if add_result == 0 and index == (len(values) - 1):
                return True
            new_totals.append(add_result)
    if new_totals:
        return check_equation(values, index + 1, new_totals)

    return False

def solve_part_one(lines: list[str]) -> int:
    total = 0
    for line in lines:
        test_value, numbers = line.split(':')
        values = numbers.strip().split(' ')
        values.reverse()
        if check_equation(values, 0, [int(test_value)]):
            total += int(test_value)

    return total


def check_equation_two(values: list[str], index: int, total: int, current_value: int) -> bool:
    if index >= len(values) or current_value > total:
        return False
    value = int(values[index])
    multiply_result = current_value * value
    success = False
    if multiply_result == total and index == (len(values) - 1):
        success = True
    elif check_equation_two(values, index + 1, total, multiply_result):
        success = True
    add_result = current_value + value
    if add_result == total and index == (len(values) - 1):
        success = True
    elif check_equation_two(values, index + 1, total, add_result):
        success = True
    combine_result = int(f'{current_value}{value}')
    if combine_result == total and index == (len(values) - 1):
        success = True
    elif check_equation_two(values, index + 1, total, combine_result):
        success = True
    return success


def solve_part_two(lines: list[str]) -> int:
    total = 0
    for line in lines:
        test_value, numbers = line.split(':')
        values = numbers.strip().split(' ')
        if check_equation_two(values, 1, int(test_value), int(values[0])):
            total += int(test_value)

    return total

assert solve_part_one(example_data) == 3749
print(solve_part_one(data)) # 3312271365652

assert solve_part_two(example_data) == 11387
print(solve_part_two(data)) # 509463489296712
