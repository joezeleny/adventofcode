"""
Day 4 of Advent of Code 2024
"""

with open("4.example", "r") as f:
    example_data = f.read().splitlines()

with open("4.data", "r") as f:
    data = f.read().splitlines()

def solve_part_one(lines: list[str]) -> int:
    total = 0
    input_length = len(lines[0])
    line_data = " ".join(lines)
    CHARS = ['M', 'A', 'S']
    INDEXES = [1, input_length, input_length+1, input_length + 2]
    NEXT_CHAR_INDEXES = INDEXES + [index * -1 for index in INDEXES]

    def check_char(char: int, ch_index: int, step: int) -> int:
        if char == 3:
            return 1
        try:
            check_index = ch_index + step
            if check_index < 0:
                return 0
            if line_data[check_index] == CHARS[char]:
                return check_char(char + 1, check_index, step)
            else:
                return 0
        except IndexError:
            return 0

    def check_words(x_index: int) -> int:
        words = 0
        for step in NEXT_CHAR_INDEXES:
            words += check_char(0, x_index, step)
        return words

    for ch_index, ch in enumerate(line_data):
        if ch == 'X':
            total += check_words(ch_index)

    return total

assert solve_part_one(example_data) == 18
print(solve_part_one(data)) # 2567


def solve_part_two(lines: list[str]) -> int:
    total = 0
    input_length = len(lines[0])
    line_data = " ".join(lines)

    def check_words(a_index: int) -> int:
        top_left = (-1 * (input_length + 2)) + a_index
        top_right = (-1 * input_length) + a_index
        bottom_left = (input_length) + a_index
        bottom_right = (input_length + 2) + a_index
        if any([index < 0 for index in [top_left, top_right, bottom_left, bottom_right]]):
            return 0
        for a ,b in [(top_left, bottom_right), (top_right, bottom_left)]:
            try:
                if not (
                    line_data[a] in ['M', 'S']
                    and line_data[b] in ['M', 'S']
                    and line_data[a] != line_data[b]
                ):
                    return 0
            except IndexError:
                return 0

        return 1

    for ch_index, ch in enumerate(line_data):
        if ch == 'A':
            total += check_words(ch_index)

    return total

assert solve_part_two(example_data) == 9
print(solve_part_two(data)) # 2029
