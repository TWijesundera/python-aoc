from typing import List

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


def sum_calibrations(lines: List):
    calibrations = []
    for line in lines:
        calibration = get_calibration_num(line)
        calibrations.append(int(calibration))
    return sum(calibrations)


if __name__ == "__main__":
    with open("input.txt", "r+", encoding="utf-8") as fp:
        lines = fp.readlines()
        print(sum_calibrations(lines))
