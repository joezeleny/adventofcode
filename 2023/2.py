"""
Day 2 Part 1
"""
class ImpossibleGameException(Exception):
    pass

data = []
with open('2.data', 'r') as f:
    data = f.readlines()

test_data = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
]

test_result = 8

def solve_puzzle(lines: list[str]) -> int:
    MAX = {
        'green': 13,
        'red': 12,
        'blue': 14,
    }
    total = 0
    for game in lines:
        id, sets = game.split(':')
        int_id = int(id[5:])
        try:
            for round in sets.split(';'):
                for cubes in round.split(','):
                    count, color = cubes.strip().split(' ')
                    if int(count) > MAX[color]:
                        raise ImpossibleGameException('Impossible Game!')
        except ImpossibleGameException:
            pass
        else:
            total += int_id
    return total

assert solve_puzzle(test_data) == test_result

print(solve_puzzle(data))


"""
Part 2
"""

test_result_2 = 2286

def solve_puzzle_2(lines: list[str]) -> int:
    import functools
    total = 0
    for game in lines:
        min_cubes = {
            'green': 0,
            'red': 0,
            'blue': 0,
        }
        id, sets = game.split(':')
        for round in sets.split(';'):
            for cubes in round.split(','):
                count, color = cubes.strip().split(' ')
                min_cubes[color] = int(count) if int(count) > min_cubes[color] else min_cubes[color]
        power = functools.reduce(lambda a, b: a*b, min_cubes.values())
        total += power
    return total

assert solve_puzzle_2(test_data) == test_result_2

print(solve_puzzle_2(data))

"""
python 2.py
2285
77021
"""
