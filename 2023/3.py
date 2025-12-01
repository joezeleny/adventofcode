"""
Day 3 Part 1

Got this one wrong a bunch of times - forgot about the newlines in the file.
Fixed by replacing readlines() with read().splitlines
"""

data = []
with open('3.data', 'r') as f:
    data = f.read().splitlines()

test_data = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]
test_result = 4361

def solve_puzzle(lines: list[str]) -> int:
    total = 0
    prev_line = '.' * len(lines[0])
    digits = set()
    all_chars = set()
    for line_index, line in enumerate(lines):
        next_line = lines[line_index + 1] if (line_index + 1) < len(lines) else '.' * len(line)
        values: list[tuple[int, str]] = []
        part = ''
        st: int | None = None
        for ch_index, ch in enumerate(line):
            all_chars.add(ch)
            if ch.isdigit():
                digits.add(ch)
                if st is None:
                    st = ch_index
                part += ch
            elif part and st is not None:
                values.append((st, part))
                part = ''
                st = None
        for start, value in values:
            if not value or not value.isnumeric():
                continue
            end = start + len(value)
            adj_start = max(0, start - 1)
            adj_end = min(len(line), end+1)
            check = line[adj_start] + line[end] + prev_line[adj_start: adj_end] + next_line[adj_start: adj_end]
            for ch in check:
                if ch.isnumeric() or ch == '.':
                    continue
                else:
                    total += int(value)
                    break
        prev_line = line
    return total

assert solve_puzzle(test_data) == test_result

print(solve_puzzle(data))

"""
python 3.py
556057
"""
