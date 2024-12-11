"""
Day 9 of Advent of Code 2024
"""

with open("9.example", "r") as f:
    example_data = f.read().splitlines()

with open("9.data", "r") as f:
    data = f.read().splitlines()

def solve_part_one(lines: list[str]) -> int:
    files = list(lines[0])
    expanded = []
    id = 0
    for index, file in enumerate(files):
        if index % 2 == 0:
            expanded += [f'{id}'] * int(file)
            id += 1
        else:
            expanded += ['.'] * int(file)

    try:
        for index in range(len(expanded)):
            if expanded[index] != '.':
                continue
            while (replacement := expanded.pop()) == '.':
                continue
            expanded[index] = replacement
    except IndexError:
        pass

    checksum = 0
    for index, item in enumerate(expanded):
        checksum += (index * int(item))

    return checksum


def solve_part_two(lines: list[str]) -> int:
    files = list(lines[0])
    expanded: list[dict[str, int]] = []
    id = 0
    for index, file in enumerate(files):
        if index % 2 == 0:
            expanded.append({'id': id, 'size': int(file), 'moved': False})
            id += 1
        else:
            expanded.append({'id': -1, 'size': int(file), 'moved': True})

    for index in range(len(expanded)-1, 0, -1):
        if expanded[index]['moved']:
            continue
        space_required = expanded[index]['size']
        move_to = None
        for idx in range(0, index):
            if expanded[idx]['id'] == -1:
                if expanded[idx]['size'] >= space_required:
                    move_to = idx
                    break
        if move_to:
            space_available = expanded[move_to]['size']
            expanded[move_to] = expanded[index]
            expanded[move_to]['moved'] = True
            expanded[index] = {'id': -1, 'size': space_required, 'moved': True}
            if (remaining := space_available - space_required) != 0:
                expanded.insert(move_to + 1, {'id': -1, 'size': remaining, 'moved': True})


    checksum = 0
    system: list[str] = []
    for item in expanded:
        string = str(item['id']) if item['id'] != -1 else '.'
        system += [string] * item['size']

    for index, item_id in enumerate(system):
        if item_id != '.':
            checksum += index * int(item_id)

    return checksum


assert solve_part_one(example_data) == 1928
print(solve_part_one(data)) # 6262891638328

assert solve_part_two(example_data) == 2858
print(solve_part_two(data)) # 6287317016845
