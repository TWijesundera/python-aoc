import unittest
from trebuchet import sum_calibrations, get_calibration


class TrebuchetTest(unittest.TestCase):
    def skiptest_calibration_correct(self):
        ex_input = "pqr3stu8vwx"
        calibration = get_calibration(ex_input)
        self.assertEqual(calibration, "38")

    def skiptest_part1(self):
        example_input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        input_sum = 142
        self.assertEqual(sum_calibrations(example_input), input_sum)

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
