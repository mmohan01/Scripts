"Standard Library"
import unittest

from tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    """Test class for Tic-tac-toe game."""
    def setUp(self):
        """Initializes Tic-tac-toe game."""
        self.tic_tac_toe = TicTacToe()

    def test_player_x_starts(self):
        """Test which player starts in the game."""
        self.assertTrue(self.tic_tac_toe.current_player == "X")

    def test_move_valid(self):
        """Test player input."""
        valid_input = "1 1"
        self.assertTrue(self.tic_tac_toe.is_valid("move", valid_input))
        valid_input = "1 2"
        self.assertTrue(self.tic_tac_toe.is_valid("move", valid_input))
        valid_input = "1 3"
        self.assertTrue(self.tic_tac_toe.is_valid("move", valid_input))
        valid_input = "2 1"
        self.assertTrue(self.tic_tac_toe.is_valid("move", valid_input))
        valid_input = "2 2"
        self.assertTrue(self.tic_tac_toe.is_valid("move", valid_input))
        valid_input = "2 3"
        self.assertTrue(self.tic_tac_toe.is_valid("move", valid_input))
        valid_input = "3 1"
        self.assertTrue(self.tic_tac_toe.is_valid("move", valid_input))
        valid_input = "3 2"
        self.assertTrue(self.tic_tac_toe.is_valid("move", valid_input))
        valid_input = "3 3"
        self.assertTrue(self.tic_tac_toe.is_valid("move", valid_input))

    def test_move_invalid_wrong_type(self):
        """Test player input."""
        no_type = None
        self.assertFalse(self.tic_tac_toe.is_valid("move", no_type, False))
        boolean_type = True
        self.assertFalse(self.tic_tac_toe.is_valid("move", boolean_type,
                                                   False))
        float_type = 1.1
        self.assertFalse(self.tic_tac_toe.is_valid("move", float_type, False))

    def test_move_invalid_wrong_argument_type(self):
        """Test player input."""
        float_arguments = "1.1 1.1"
        self.assertFalse(
            self.tic_tac_toe.is_valid("move", float_arguments, False))
        alphanumeric_arguments = "a a"
        self.assertFalse(
            self.tic_tac_toe.is_valid("move", alphanumeric_arguments, False))
        alphanumeric_arguments = "ab ab"
        self.assertFalse(
            self.tic_tac_toe.is_valid("move", alphanumeric_arguments, False))
        boolean_arguments = "True False"
        self.assertFalse(
            self.tic_tac_toe.is_valid("move", boolean_arguments, False))
        mixed_arguments = "1 1.1"
        self.assertFalse(
            self.tic_tac_toe.is_valid("move", mixed_arguments, False))
        mixed_arguments = "1.1 1"
        self.assertFalse(
            self.tic_tac_toe.is_valid("move", mixed_arguments, False))

    def test_move_invalid_wrong_argument_amount(self):
        """Test player input."""
        wrong_argument_amount = ""
        self.assertFalse(
            self.tic_tac_toe.is_valid("move", wrong_argument_amount, False))
        wrong_argument_amount = "1"
        self.assertFalse(
            self.tic_tac_toe.is_valid("move", wrong_argument_amount, False))
        wrong_argument_amount = "1 1 1"
        self.assertFalse(
            self.tic_tac_toe.is_valid("move", wrong_argument_amount, False))

    def test_move_invalid_no_space(self):
        """Test player input."""
        no_space = "11"
        self.assertFalse(self.tic_tac_toe.is_valid("move", no_space, False))

    def test_move_invalid_out_of_bounds(self):
        """Test player input."""
        row_too_small = "0 1"
        self.assertFalse(
            self.tic_tac_toe.is_valid("move", row_too_small, False))
        row_too_large = "4 1"
        self.assertFalse(
            self.tic_tac_toe.is_valid("move", row_too_large, False))
        column_too_small = "1 0"
        self.assertFalse(
            self.tic_tac_toe.is_valid("move", column_too_small, False))
        column_too_large = "1 4"
        self.assertFalse(
            self.tic_tac_toe.is_valid("move", column_too_large, False))
        row_minus = "-1 1"
        self.assertFalse(self.tic_tac_toe.is_valid("move", row_minus, False))
        column_minus = "1 -1"
        self.assertFalse(self.tic_tac_toe.is_valid("move", column_minus,
                                                   False))

    def test_replay_valid(self):
        """Test player input."""
        valid_input = "Y"
        self.assertTrue(self.tic_tac_toe.is_valid("replay", valid_input))
        valid_input = "y"
        self.assertTrue(self.tic_tac_toe.is_valid("replay", valid_input))
        valid_input = "N"
        self.assertTrue(self.tic_tac_toe.is_valid("replay", valid_input))
        valid_input = "n"
        self.assertTrue(self.tic_tac_toe.is_valid("replay", valid_input))

    def test_replay_not_valid(self):
        """Test player input."""
        invalid_input = None
        self.assertFalse(
            self.tic_tac_toe.is_valid("replay", invalid_input, False))
        invalid_input = True
        self.assertFalse(
            self.tic_tac_toe.is_valid("replay", invalid_input, False))
        invalid_input = "1.1"
        self.assertFalse(
            self.tic_tac_toe.is_valid("replay", invalid_input, False))
        invalid_input = "1"
        self.assertFalse(
            self.tic_tac_toe.is_valid("replay", invalid_input, False))
        invalid_input = "-1"
        self.assertFalse(
            self.tic_tac_toe.is_valid("replay", invalid_input, False))
        invalid_input = ""
        self.assertFalse(
            self.tic_tac_toe.is_valid("replay", invalid_input, False))
        invalid_input = " "
        self.assertFalse(
            self.tic_tac_toe.is_valid("replay", invalid_input, False))
        invalid_input = "a"
        self.assertFalse(
            self.tic_tac_toe.is_valid("replay", invalid_input, False))
        invalid_input = "ab"
        self.assertFalse(
            self.tic_tac_toe.is_valid("replay", invalid_input, False))

    def test_ai_valid(self):
        """Test player input."""
        valid_input = "Y"
        self.assertTrue(self.tic_tac_toe.is_valid("ai", valid_input))
        valid_input = "y"
        self.assertTrue(self.tic_tac_toe.is_valid("ai", valid_input))
        valid_input = "N"
        self.assertTrue(self.tic_tac_toe.is_valid("ai", valid_input))
        valid_input = "n"
        self.assertTrue(self.tic_tac_toe.is_valid("ai", valid_input))

    def test_ai_not_valid(self):
        """Test player input."""
        invalid_input = None
        self.assertFalse(self.tic_tac_toe.is_valid("ai", invalid_input, False))
        invalid_input = True
        self.assertFalse(self.tic_tac_toe.is_valid("ai", invalid_input, False))
        invalid_input = "1.1"
        self.assertFalse(self.tic_tac_toe.is_valid("ai", invalid_input, False))
        invalid_input = "1"
        self.assertFalse(self.tic_tac_toe.is_valid("ai", invalid_input, False))
        invalid_input = "-1"
        self.assertFalse(self.tic_tac_toe.is_valid("ai", invalid_input, False))
        invalid_input = ""
        self.assertFalse(self.tic_tac_toe.is_valid("ai", invalid_input, False))
        invalid_input = " "
        self.assertFalse(self.tic_tac_toe.is_valid("ai", invalid_input, False))
        invalid_input = "a"
        self.assertFalse(self.tic_tac_toe.is_valid("ai", invalid_input, False))
        invalid_input = "ab"
        self.assertFalse(self.tic_tac_toe.is_valid("ai", invalid_input, False))

    def test_ai_generated_move_valid(self):
        """Test move generated by ai."""
        for _ in range(10):
            move = self.tic_tac_toe.compute_ai_move()
            self.assertTrue(len(move) == 3)
            self.assertTrue(self.tic_tac_toe.is_valid("move", move))

    def test_in_play_true(self):
        """Test whether the current game is still in progress."""
        self.tic_tac_toe.moves = [None] * 9
        self.assertTrue(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            "X", None, None, None, None, None, None, None, None
        ]
        self.assertTrue(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            "O", None, None, None, None, None, None, None, None
        ]
        self.assertTrue(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = ["X", "O", "X", "X", "X", "O", "O", "X", None]
        self.assertTrue(self.tic_tac_toe.in_play())

    def test_in_play_false(self):
        """Test whether the current game is finished."""
        self.tic_tac_toe.moves = ["X", "X", "X", "X", "X", "X", "X", "X", "X"]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = ["X", "O", "X", "X", "X", "O", "O", "X", "O"]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            "X", "X", "X", None, None, None, None, None, None
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            None, None, None, "X", "X", "X", None, None, None
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            None, None, None, None, None, None, "X", "X", "X"
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            "X", None, None, "X", None, None, "X", None, None
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            None, "X", None, None, "X", None, None, "X", None
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            None, None, "X", None, None, "X", None, None, "X"
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            "X", None, None, None, "X", None, None, None, "X"
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            None, None, "X", None, "X", None, "X", None, None
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            "O", "O", "O", None, None, None, None, None, None
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            None, None, None, "O", "O", "O", None, None, None
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            None, None, None, None, None, None, "O", "O", "O"
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            "O", None, None, "O", None, None, "O", None, None
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            None, "O", None, None, "O", None, None, "O", None
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            None, None, "O", None, None, "O", None, None, "O"
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            "O", None, None, None, "O", None, None, None, "O"
        ]
        self.assertFalse(self.tic_tac_toe.in_play())
        self.tic_tac_toe.moves = [
            None, None, "O", None, "O", None, "O", None, None
        ]
        self.assertFalse(self.tic_tac_toe.in_play())


if __name__ == '__main__':
    unittest.main()
