"""
Part 1
"""
test_1 = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet',
]
test_result_1 = 142

def solve_day_1_part_1():
    lines = []
    with open('1.data', 'r') as f:
        lines = f.readlines()
    print(get_total(lines))

def get_total(lines: list[str]) -> int:
    total = 0
    for line in lines:
        first = None
        last = None
        for i in line:
            try:
                int(i)
            except ValueError:
                continue
            if not first:
                first = i
            last = i
        combined = int(f'{first}{last}')
        total += combined
    return total

assert get_total(test_1) == test_result_1

solve_day_1_part_1()

"""
Part 2
"""
test_2 = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]
test_result_2 = 281

def solve_day_1_part_2():
    lines = []
    with open('1.data', 'r') as f:
        lines = f.readlines()
    print(get_total_revised(lines))

int_words = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def get_total_revised(lines: list[str]) -> int:
    total = 0
    for line in lines:
        first_int = None
        last_int = None
        first_words = {}
        last_words = {}
        for i, ch in enumerate(line):
            try:
                int(ch)
            except ValueError:
                pass
            else:
                if not first_int:
                    first_int = i, ch
                last_int = i, ch
        for word in int_words.keys():
            if (i := line.find(word)) != -1:
                first_words[word] = i
            if (i := line.rfind(word)) != -1:
                last_words[word] = i
        first_words = dict(sorted(first_words.items(), key=lambda item: item[1]))
        first_word = next(iter(first_words.items()), None)
        last_words = dict(sorted(last_words.items(), key=lambda item: item[1], reverse=True))
        last_word = next(iter(last_words.items()), None)

        if first_word and first_int:
            first = first_int[1] if first_int[0] < first_word[1] else int_words[first_word[0]]
        elif first_word:
            first = int_words[first_word[0]]
        elif first_int:
            first = first_int[1]

        if last_word and last_int:
            last = last_int[1] if last_int[0] > last_word[1] else int_words[last_word[0]]
        elif last_word:
            last = int_words[last_word[0]]
        elif last_int:
            last = last_int[1]

        combined = int(f'{first}{last}')
        total += combined
    return total

assert get_total_revised(test_2) == test_result_2

solve_day_1_part_2()

"""
python 1.py
54990
54473
"""
