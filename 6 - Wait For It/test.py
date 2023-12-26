import unittest
import wait_for_it


class TestWaitForIt(unittest.TestCase):
    def test_zipped_races(self):
        input = ["Time:      7  15   30", "Distance:  9  40  200"]
        res = list(wait_for_it.get_zipped_races(input))
        sol = [(7, 9), (15, 40), (30, 200)]
        self.assertEqual(res, sol)

    def test_find_possible_wins(self):
        input = [(7, 9), (15, 40), (30, 200)]
        res = wait_for_it.beat_record(input)
        sol = 288
        self.assertEqual(res, sol)

    def test_get_single_race(self):
        input = ["Time:      7  15   30", "Distance:  9  40  200"]
        res = wait_for_it.get_single_race(input)
        sol = [(71530, 940200)]
        self.assertListEqual(res, sol)


if __name__ == "__main__":
    unittest.main()
