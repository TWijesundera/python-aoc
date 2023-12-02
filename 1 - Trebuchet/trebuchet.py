import regex as re

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


def get_calibration(line):
    or_pattern = "|".join(WORDS_TO_NUM.keys())
    pattern = re.compile(f"\\d|{or_pattern}")
    matches = re.findall(pattern, line, overlapped=True)
    return f"{WORDS_TO_NUM.get(matches[0], matches[0])}{WORDS_TO_NUM.get(matches[-1], matches[-1])}"


def sum_calibrations(lines):
    calibration_values = []
    for line in lines:
        calibration = get_calibration(line)
        calibration_values.append(int(calibration))
    return sum(calibration_values)


if __name__ == "__main__":
    with open("input.txt", "r+", encoding="utf-8") as fp:
        lines = fp.readlines()
    print(sum_calibrations(lines))
