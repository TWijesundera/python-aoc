import re
from typing import List, Match

WORDS_TO_NUM = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_calibration_num(line: str):
    first_num = 0
    last_num = 0

    for char in line:
        if char.isdigit():
            first_num = char
            break

    for char in reversed(line):
        if char.isdigit():
            last_num = char
            break

    return f"{first_num}{last_num}"


def get_calibration_with_word(line: str):
    found_words = []

    for word in WORDS_TO_NUM.keys():
        for match in re.finditer(word, line):
            found_words.append(match)

    match_digits = list(re.finditer(r"\d", line))

    if match_digits:
        found_words.extend(match_digits)

    min_match = min(found_words, key=lambda x: x.start())
    max_match = max(found_words, key=lambda x: x.end())

    return "".join(
        [
            f"{WORDS_TO_NUM.get(min_group := min_match.group(), min_group)}",
            f"{WORDS_TO_NUM.get(max_group := max_match.group(), max_group)}",
        ]
    )


def sum_calibrations(lines: List):
    calibrations = []
    for line in lines:
        calibration = get_calibration_with_word(line)
        print(line)
        print(calibration)
        calibrations.append(int(calibration))
    return sum(calibrations)


if __name__ == "__main__":
    with open("input.txt", "r+", encoding="utf-8") as fp:
        lines = fp.readlines()
        print(sum_calibrations(lines))
