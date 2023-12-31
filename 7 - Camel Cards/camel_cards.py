import re

from collections import Counter
from enum import Enum
from functools import cmp_to_key, partial
from typing import List, Dict


class Ranking(Enum):
    FIVE = 7
    FOUR = 6
    FULL = 5
    THREE = 4
    TWO = 3
    ONE = 2
    HIGH = 1


class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.count = Counter(self.hand)
        self.hand_type = self._find_ranking(self.count)
        self.joker_hand = self._rank_with_jokers(self.count, hand)

    def _find_ranking(self, counter):
        match counter.most_common():
            case [first]:
                return Ranking.FIVE
            case [first, _] if first[1] == 4:
                return Ranking.FOUR
            case [first, second] if first[1] == 3 and second[1] == 2:
                return Ranking.FULL
            case [first, _, _] if first[1] == 3:
                return Ranking.THREE
            case [first, second, _] if first[1] == second[1]:
                return Ranking.TWO
            case [first, _, _, _] if first[1] == 2:
                return Ranking.ONE
            case _:
                return Ranking.HIGH

    def _rank_with_jokers(self, counter: Counter, original_hand: str):
        if counter["J"] and len(counter) > 1:
            for elem, _ in counter.most_common():
                if elem != "J":
                    most_common = elem
                    break
            replaced_string = re.sub(r"J", most_common[0], original_hand)
            counter = Counter(replaced_string)

        return self._find_ranking(counter)

    def __str__(self):
        self.hand


def get_card_values(joker: bool) -> Dict[str, str]:
    card_values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    if joker:
        card_values["J"] = 1
    else:
        card_values["J"] = 11
    return card_values


def compare_hands(
    hand: "Hand",
    other: "Hand",
):
    card_values = get_card_values(False)
    if hand.hand_type == other.hand_type:
        for x, y in zip(hand.hand, other.hand):
            if x != y:
                return -1 if card_values[x] < card_values[y] else 1
    else:
        return -1 if hand.hand_type.value < other.hand_type.value else 1


def compare_joker(hand: "Hand", other: "Hand"):
    card_values = get_card_values(True)
    if hand.joker_hand == other.joker_hand:
        for x, y in zip(hand.hand, other.hand):
            if x != y:
                return -1 if card_values[x] < card_values[y] else 1
    else:
        return -1 if hand.joker_hand.value < other.joker_hand.value else 1


def sort_cards(lines, compare_func):
    return sorted(
        [Hand(line.split()[0], line.split()[1]) for line in lines],
        key=cmp_to_key(compare_func),
    )


def total_winnings(lines: List[str]):
    sorted_keys = sort_cards(lines, compare_hands)
    # print(
    #     [
    #         (i, hand.hand, hand.hand_type)
    #         for (i, hand) in enumerate(sorted_keys, start=1)
    #     ]
    # )
    total = sum([i * int(hand.bid) for (i, hand) in enumerate(sorted_keys, start=1)])
    return total


def total_winnings_joker(lines: List[str]):
    sorted_joker_hands = sort_cards(lines, compare_joker)
    # print(
    #     [
    #         (i, hand.hand, hand.joker_hand)
    #         for (i, hand) in enumerate(sorted_joker_hands, start=1)
    #     ]
    # )
    total = sum(
        [i * int(hand.bid) for (i, hand) in enumerate(sorted_joker_hands, start=1)]
    )
    return total


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as fp:
        input = fp.readlines()
    print(f"total: {total_winnings(input)}")
    print(f"Joker: {total_winnings_joker(input)}")
