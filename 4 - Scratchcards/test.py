import unittest
import scratchcards


class TestScratchCards(unittest.TestCase):
    def test_find_no_matches(self):
        input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        res, _ = scratchcards.get_intersection(input)
        self.assertEqual(res, 4)

    def test_calculate_card_value(self):
        input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        matches, _ = scratchcards.get_intersection(input)
        res = scratchcards.card_value(matches)
        self.assertEqual(res, 8)

    def test_total_card_sum(self):
        input = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
        res = scratchcards.get_total_card_sum(input)
        self.assertEqual(res, 13)

    def test_instances(self):
        input = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
        sol = 30
        res = scratchcards.get_instances(input)
        self.assertEqual(res, sol)


if __name__ == "__main__":
    unittest.main()
