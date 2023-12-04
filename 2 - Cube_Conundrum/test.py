import unittest
import cube_conundrum


class TestCubeConundrum(unittest.TestCase):
    def test_get_game_id(self):
        input = (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
        )
        res = cube_conundrum.get_game_id(input)
        self.assertEqual(res[0], 4)

    def test_invalid_game(self):
        input = (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
        )
        valid_game = cube_conundrum.get_cube_values(input)
        self.assertEqual(valid_game, False)

    def test_valid_game(self):
        input = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
        valid_game = cube_conundrum.get_cube_values(input)
        self.assertEqual(valid_game, True)

    def test_example_solution(self):
        input = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]
        game_sum = cube_conundrum.find_valid_games(input)
        self.assertEqual(game_sum, 8)

    def test_find_fewest_to_play(self):
        input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        res = cube_conundrum.max_cubes(input)
        solution = cube_conundrum.MaxCubes(4, 6, 2, 48)
        self.assertEqual(res, solution)

    def test_find_added_power(self):
        input = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]
        solution = 2286
        res = cube_conundrum.find_added_power(input)
        self.assertEqual(res, solution)


if __name__ == "__main__":
    unittest.main()
