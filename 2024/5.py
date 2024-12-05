"""
Day 5 of Advent of Code 2024
"""
from collections import defaultdict
from functools import cmp_to_key

with open("5.example", "r") as f:
    example_data = f.read().splitlines()

with open("5.data", "r") as f:
    data = f.read().splitlines()


def split_rules_updates(lines: list[str]) -> tuple[list[str], list[str]]:
    sep = lines.index('')
    rules = lines[:sep]
    updates = lines[sep+1:]
    return rules, updates


def get_rule_mapping(rules: list[str]) -> dict[str, list[str]]:
    rule_mapping = defaultdict(list)
    for rule in rules:
        first, second = rule.split('|')
        rule_mapping[first].append(second)
    return rule_mapping


def check_update_order(pages: list[str], rule_mapping: dict[str, list]) -> bool:
    reversed = pages[:]
    reversed.reverse()
    for index, page in enumerate(reversed):
        if any([p in rule_mapping[page] for p in reversed[index:]]):
            return False
    return True


def solve_part_one(lines: list[str]) -> int:
    total = 0
    rules, updates = split_rules_updates(lines)
    rule_mapping = get_rule_mapping(rules)

    for update in updates:
        pages = update.split(',')
        if check_update_order(pages, rule_mapping):
            total += int(pages[len(pages) // 2])
    return total


def solve_part_two(lines: list[str]) -> int:
    total = 0
    rules, updates = split_rules_updates(lines)
    rule_mapping = get_rule_mapping(rules)
    invalid_updates: list[str] = []
    for update in updates:
        pages = update.split(',')
        valid = check_update_order(pages, rule_mapping)
        if not valid:
            invalid_updates.append(update)

    for update in invalid_updates:
        def sort_comp(a: str, b: str) -> int:
            if b in rule_mapping[a]:
                return -1
            elif a in rule_mapping[b]:
                return 1
            return 0
        pages = update.split(',')
        pages = sorted(pages, key=cmp_to_key(sort_comp))
        if check_update_order(pages, rule_mapping): # Just double checking
            total += int(pages[len(pages) // 2])
    return total


assert solve_part_one(example_data) == 143
print(solve_part_one(data)) # 5374

assert solve_part_two(example_data) == 123
print(solve_part_two(data)) # 4260
