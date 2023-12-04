import re
from collections import namedtuple
from typing import List, Tuple

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14
REGEX = r"(\d+).(green|blue|red)"
MaxCubes = namedtuple("MaxCubes", ["red", "blue", "green", "power"])


def get_game_id(line: str) -> Tuple[int, str]:
    game_and_contents = line.split(":")
    game_id = game_and_contents[0].split()[1]
    return int(game_id), game_and_contents[1]


def get_cube_values(line: str):
    pattern = re.compile(REGEX)
    found = re.finditer(pattern, line)
    for re_match in found:
        valid_game = _valid_game(re_match.group(2), int(re_match.group(1)))
        if not valid_game:
            return False
    return True


def _valid_game(cube_color: str, no_cubes: int):
    match cube_color:
        case "red":
            if int(no_cubes) > RED_CUBES:
                return False
        case "green":
            if int(no_cubes) > GREEN_CUBES:
                return False
        case "blue":
            if int(no_cubes) > BLUE_CUBES:
                return False
    return True


def max_cubes(line: str):
    pattern = re.compile(REGEX)
    max_red = 0
    max_blue = 0
    max_green = 0

    match_iter = re.finditer(pattern, line)
    for re_match in match_iter:
        no_cube = int(re_match.group(1))
        cube_color = re_match.group(2)
        match cube_color:
            case "red":
                if no_cube > max_red:
                    max_red = no_cube
            case "green":
                if no_cube > max_green:
                    max_green = no_cube
            case "blue":
                if no_cube > max_blue:
                    max_blue = no_cube

    power = max_red * max_blue * max_green

    return MaxCubes(max_red, max_blue, max_green, power)


def find_added_power(lines: List[str]):
    power_sum = []

    for line in lines:
        cubes = max_cubes(line)
        power_sum.append(cubes.power)
    return sum(power_sum)


def find_valid_games(lines: List[str]):
    valid_games = []

    for line in lines:
        game_id, game_contents = get_game_id(line)
        valid_game = get_cube_values(game_contents)
        if valid_game:
            valid_games.append(game_id)

    return sum(valid_games)


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as fp:
        lines = fp.readlines()
    print(find_valid_games(lines))
    print(find_added_power(lines))
