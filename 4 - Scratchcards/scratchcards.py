import re
import string
from collections import defaultdict
from typing import List, Dict, Tuple


def get_intersection(line: str) -> Tuple[int, str]:
    card_num, winning_nums, nums = re.split(r"[:|]", line)
    win_set = set(winning_nums.strip().split())
    nums_set = set(nums.strip().split())
    intersect = win_set.intersection(nums_set)
    return len(intersect), card_num


def card_value(no_matches: int) -> int:
    return 2 ** (no_matches - 1)


def get_total_card_sum(lines: List[str]) -> int:
    total_sum = []
    for line in lines:
        no_matches, _ = get_intersection(line)
        if no_matches > 0:
            total_sum.append(card_value(no_matches))
    return sum(total_sum)


def get_instances(lines):
    key_template = string.Template("Card $num")
    #card_instances: Dict[str, int] = defaultdict(int)
    card_instances = {card_no: 1 for card_no in range(1, len(lines) + 1)}
    for line in lines:
        matches, card = get_intersection(line)
        number_match = int(re.search(r"\d+", card).group(0))

        for num in range(number_match + 1, number_match + matches + 1):
            card_instances[num] += card_instances[number_match]
    print(card_instances)
    return sum(card_instances.values())


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as fp:
        lines = fp.readlines()
        print(get_total_card_sum(lines))
        print(get_instances(lines))
