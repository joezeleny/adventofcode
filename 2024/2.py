"""
Day 2 of Advent of Code 2024
"""
from typing import Any

with open("2.example", "r") as f:
    example_data = f.read().splitlines()

with open("2.data", "r") as f:
    data = f.read().splitlines()


class InvalidReport(Exception):
    def __init__(self, index: int, *args: Any) -> None:
        self.index = index


def check_report(items: list[str]) -> None:
    for index, item in enumerate(items):
        if index == 0:
            if int(item) == int(items[index + 1]):
                # First two numbers are equal, this report is already invalid
                raise InvalidReport(index)
            # incr being true means the numbers are increasing left to right
            incr = int(item) < int(items[index + 1])
            continue

        diff = int(item) - int(items[index - 1])
        if incr and not (1 <= diff <= 3):
            # If increasing, the diff should be between 1 and 3, if not the report is invalid
            raise InvalidReport(index-1)
        elif not incr and not (-3 <= diff <= -1):
            # If decreasing, the diff should be between -1 and -3, if not the report is invalid
            raise InvalidReport(index-1)

def solve_part_one(lines: list[str]) -> int:
    result = 0

    for line in lines:
        items = line.split(' ')
        try:
            check_report(items)
        except InvalidReport:
            # Skip to the next report once one is deemed invalid
            continue
        else:
            # This report didn't raise an exception, it must be valid
            result += 1

    return result

assert solve_part_one(example_data) == 2
print(solve_part_one(data))


def solve_part_two(lines: list[str]) -> int:
    result = 0
    for line in lines:
        items = line.split(' ')
        try:
            try:
                check_report(items)
            except InvalidReport as first:
                # First lets try removing the first item, as it may just be an incr/decr issue
                # This is the part I missed the first time and went
                # to the brute force method below to find this issue
                new_items = items[:]
                new_items.pop(0)
                try:
                    check_report(new_items)
                except InvalidReport:
                    # Let's try removing one of the values that caused the issue
                    new_items = items[:]
                    new_items.pop(first.index)
                    try:
                        check_report(new_items)
                    except InvalidReport:
                        # Let's try one more time removing the other value
                        new_items = items[:]
                        new_items.pop(first.index + 1)
                        check_report(new_items)
        except InvalidReport:
            # Skip to the next report once one is deemed invalid
            continue
        else:
            # This report didn't raise an exception, it must be valid
            result += 1

    return result

assert solve_part_two(example_data) == 4
print(solve_part_two(data))


def solve_part_two_brute_force(lines: list[str]) -> int:
    result = 0

    for line in lines:
        items = line.split(' ')
        try:
            try:
                check_report(items)
            except InvalidReport:
                for i in range(len(items)):
                    new_items = items[:]
                    new_items.pop(i)
                    try:
                        check_report(new_items)
                    except InvalidReport:
                        if i == len(items) - 1:
                            raise
                    else:
                        break
        except InvalidReport:
            # Skip to the next report once one is deemed invalid
            continue
        else:
            # This report didn't raise an exception, it must be valid
            result += 1

    return result

assert solve_part_two_brute_force(example_data) == 4
print(solve_part_two_brute_force(data))
