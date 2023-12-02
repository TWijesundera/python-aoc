import unittest
from unittest import skip

import trebuchet
import trebuchet_retry


class TrebuchetTest(unittest.TestCase):
    def test_calibration_correct(self):
        ex_input = "pqr3stu8vwx"
        calibration = trebuchet_retry.get_calibration_num(ex_input)
        self.assertEqual(calibration, "38")
    
    @skip
    def test_overlapping_calibration(self):
        ex_input = "2eightwone"
        self.assertEqual("21", "21")

    
    def test_part1(self):
        example_input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        input_sum = 142
        self.assertEqual(trebuchet_retry.sum_calibrations(example_input), input_sum)

    @skip
    def test_part2(self):
        example_input = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
            "nineightoneight"
        ]
        answer = 379
        self.assertEqual(answer, sum_calibrations(example_input))


if __name__ == "__main__":
    unittest.main()
