"Standard Library"
import math
import random


class TicTacToe:
    """Class to store information about the state of Tic-tac-toe game"""
    PLAYER_X = "X"
    PLAYER_O = "O"
    MIN_ROW = 1
    MAX_ROW = 3
    MIN_COLUMN = MIN_ROW
    MAX_COLUMN = MAX_ROW

    def __init__(self):
        """Initializes the state of the board and players in the Tac-tac-toe game."""
        self.current_player = self.PLAYER_X
        self.moves = [None] * 9
        self.board = "- - -\n- - -\n- - -"
        self.current_index = -1
        self.winner = None
        self.play_computer = False
        return

    def start_game(self):
        """Runs the Tic-tac-toe game."""
        while True:
            # While the game is in progress.
            while self.in_play():
                # Get the current move from the legal player.
                current_move = None
                while not self.is_valid("move", current_move):
                    if ((self.play_computer)
                            and (self.current_player == self.PLAYER_O)):
                        current_move = self.compute_ai_move()
                    else:
                        current_move = input(
                            f"Player {self.current_player}, please enter your move: "
                        )

                # Update the board with the current move and display the updated board.
                self.set_move()
                if ((self.play_computer)
                        and (self.current_player == self.PLAYER_O)):
                    row = math.floor(self.current_index / self.MAX_COLUMN) + 1
                    column = (self.current_index % self.MAX_COLUMN) + 1
                    # If playing against the AI, output the move the
                    # AI has made before displaying the updated board.
                    print(f"Player {self.PLAYER_O} has entered a move"
                          f"in row {row} and column {column}")
                print(self.board)
                self.current_player = self.PLAYER_O if (
                    self.current_player == self.PLAYER_X) else self.PLAYER_X

            # Display the winner of the previous game.
            if not self.winner:
                print("The game is a draw!")
            else:
                print(f"The winner is Player {self.winner}")

            # Prompt user to replay. If not, exit.
            replay = None
            while not self.is_valid("replay", replay):
                replay = input("Play again [Y/N]? ")
            if (replay == "N" or replay == "n"):
                break

            # Prompt user to play against the AI.
            computer = None
            while not self.is_valid("ai", computer):
                computer = input("Play against AI [Y/N]? ")
            if (computer == "Y" or computer == "y"):
                self.play_computer = True
                print("Playing against the AI. You are player X")

            # Reset the board state before restarting the game.
            self.reset()
        return

    def compute_ai_move(self):
        """Randomly generates a valid move on the board for the AI.

        Returns:
            str: string representation of current AI move ("row column").
        """
        row = random.randint(1, 3)
        column = random.randint(1, 3)
        move = str(row) + " " + str(column)
        return move

    def in_play(self):
        """Works out whether the game in its current state
        is finished, or if there are still moves to be made.

        Returns:
            bool: True if the game is unfinished.
                  False if there is a winner or all moves have been made.
        """
        # Set of possible winning moves.
        winning_states = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                          [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        # If any of the winning states have been achieved in the
        # current board, store the winning player and return False.
        for state in winning_states:
            if ((self.moves[state[0]])
                    and (self.moves[state[0]] == self.moves[state[1]] ==
                         self.moves[state[2]])):
                self.winner = self.moves[state[0]]
                return False

        # If all moves have already been made, return False.
        if all(value is not None for value in self.moves):
            return False

        # Game is still unfinished, return True.
        return True

    def is_valid(self, input_type, input_value, debug=True):
        """Checks whether a user input is a valid value.

        Args:
            input_type (str): String representing the type of input to check the validity of.
            input_value (str): The value of the input to validate.
            debug (bool): Whether or not to display output statement on invalid inputs.

        Returns:
            bool: True if input_value is valid. False if it isn't.
        """
        if ((input_value) and isinstance(input_value, str)):
            if input_type == "move":
                # Check that the right amount of values have been specified.
                if len(input_value.split()) != 2:
                    if debug:
                        print("The input must be a row value followed "
                              "by a space followed by a column value")
                else:
                    row = input_value.split()[0]
                    column = input_value.split()[1]

                    # Check that inputs are integers
                    if not row.isdigit():
                        if debug:
                            print("The row must be an integer value")
                    elif not column.isdigit():
                        if debug:
                            print("The column must be an integer value")
                    # Check that the input values are within the correct row/column range.
                    elif ((int(row) < self.MIN_ROW)
                          or (int(row) > self.MAX_ROW)):
                        if debug:
                            print(
                                f"The row must be a value between {self.MIN_ROW} and {self.MAX_ROW}"
                            )
                    elif ((int(column) < self.MIN_COLUMN)
                          or (int(column) > self.MAX_COLUMN)):
                        if debug:
                            print(f"The column must be a value between "
                                  f"{self.MIN_COLUMN} and {self.MAX_COLUMN}")
                    else:
                        # Check whether the move has already been made.
                        self.set_current_index(int(row), int(column))
                        if self.moves[self.current_index] is not None:
                            # Don't display warning if the AI is the current player.
                            if not ((self.play_computer) and
                                    (self.current_player == self.PLAYER_O)):
                                if debug:
                                    print("The move has already been made")
                        # Move is valid.
                        else:
                            return True
            elif (input_type == "replay") or (input_type == "ai"):
                # Check that the input is a valid yes or no value.
                if ((input_value != "Y") and (input_value != "y")
                        and (input_value != "N") and (input_value != "n")):
                    if debug:
                        print("Value must be \'Y\' or \'N\'")
                # Input is valid yes or no value..
                else:
                    return True
        # Input is not valid.
        return False

    def set_current_index(self, row, column):
        """Calculates the index in the list of moves that represents the row and column specified as
        an input, and sets the class attibute self.current_index to the calculated value.

        Args:
            row (int): row value of the soecified move (1-indexed).
            column (int): column value of the soecified move (1-indexed).
        """
        self.current_index = (row - 1) * self.MAX_COLUMN + (column - 1)
        return

    def set_move(self):
        """Updates the current board with the specified move"""
        self.moves[self.current_index] = self.current_player
        board_index = 2 * self.current_index
        self.board = self.board[:
                                board_index] + self.current_player + self.board[
                                    (board_index + 1):]
        return

    def reset(self):
        """Resets the state of the board and players, in order to replay the game."""
        self.current_player = self.PLAYER_X
        self.moves = [None] * 9
        self.board = "- - -\n- - -\n- - -"
        self.current_index = -1
        self.winner = None
        return
