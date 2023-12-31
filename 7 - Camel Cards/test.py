import unittest

from camel_cards import (
    Hand,
    Ranking,
    total_winnings,
    sort_cards,
    compare_hands,
    compare_joker,
    total_winnings_joker,
)


class TestCamelCards(unittest.TestCase):
    def test_five(self):
        input = "TTTTT"
        bid = "765"
        hand = Hand(input, bid)
        self.assertIs(hand.hand_type, Ranking.FIVE)

    def test_four(self):
        input = "99A99"
        bid = "72"
        hand = Hand(input, bid)
        self.assertIs(hand.hand_type, Ranking.FOUR)

    def test_full(self):
        input = "3T3T3"
        bid = "802"
        hand = Hand(input, bid)
        self.assertIs(hand.hand_type, Ranking.FULL)

    def test_three(self):
        input = "T55J5"
        bid = "765"
        hand = Hand(input, bid)
        self.assertIs(hand.hand_type, Ranking.THREE)

    def test_two(self):
        input = "T5T56"
        bid = "216"
        hand = Hand(input, bid)
        self.assertIs(hand.hand_type, Ranking.TWO)

    def test_one(self):
        input = "32T3K"
        bid = "765"
        hand = Hand(input, bid)
        self.assertIs(hand.hand_type, Ranking.ONE)

    def test_high(self):
        input = "23456"
        bid = "1"
        hand = Hand(input, bid)
        self.assertIs(hand.hand_type, Ranking.HIGH)

    def test_sorting(self):
        sol = ["32T3K", "KTJJT", "KK677", "T55J5", "QQQJA"]
        input = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]
        res = sort_cards(input, compare_hands)
        self.assertEqual([x.hand for x in res], sol)

    def test_total_winnings(self):
        input = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]
        sol = 6440
        res = total_winnings(input)
        self.assertEqual(res, sol)

    def test_joker_one(self):
        input = "J267K"
        bid = "30"
        hand = Hand(input, bid)
        self.assertIs(hand.joker_hand, Ranking.ONE)

    def test_joker_ranking(self):
        input = "KTJJT"
        bid = "220"
        hand = Hand(input, bid)
        self.assertIs(hand.joker_hand, Ranking.FOUR)

    def test_joker_sorting(self):
        sol = ["32T3K", "KK677", "T55J5", "QQQJA", "KTJJT"]
        input = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]
        res = sort_cards(input, compare_joker)
        self.assertListEqual([x.hand for x in res], sol)

    def test_joker_winnings(self):
        input = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]
        sol = 5905
        res = total_winnings_joker(input)
        self.assertEqual(res, sol)


if __name__ == "__main__":
    unittest.main()
