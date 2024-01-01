import unittest

from haunted_wasteland import Networks, Instructions


class TestHauntedWasteland(unittest.TestCase):
    test_instructions = "LLR"
    test_network = ["AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"]

    def test_network_populated(self):
        sol = {"AAA": ("BBB", "BBB"), "BBB": ("AAA", "ZZZ"), "ZZZ": ("ZZZ", "ZZZ")}
        network = Networks(self.test_network, Instructions(self.test_instructions))
        self.assertDictEqual(network.networks, sol)

    def test_number_steps(self):
        sol = 6
        start_node = "AAA"
        end_node = "ZZZ"
        network = Networks(self.test_network, Instructions(self.test_instructions))
        res = network.calculate_steps(start_node, end_node)
        self.assertEqual(res, sol)


if __name__ == "__main__":
    unittest.main()
