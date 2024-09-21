# TIC_TAC_TOE

We have a Player class, which serves as a blueprint for both human and computer players. Each player has a letter—either ‘X’ or ‘O’—to represent their moves.

The RandomComputerPlayer class is a delightful little creation. It’s like a mischievous sprite that randomly selects an available square on the board for its move. 🎲

And then there’s the HumanPlayer. Ah, the noble human! This player interacts with the game through the console, inputting their desired move. But beware, for it checks if the chosen square is valid. If not, it gently nudges the player to try again. 🤓

# Game Board (Tictactoe class):

The Tictactoe class initializes an empty 3x3 board (represented by a list of 9 elements).

It keeps track of the current winner (if any).

Methods like print_board, print_board_nums, available_moves, empty_squares, num_empty_squares, and make_move handle various aspects of the game.

# Winning Logic (winner method):

The winner method checks if a player has won by examining rows, columns, and diagonals.

It uses the modulo operator to identify diagonals.

# Game Flow (play function):

The play function alternates between the human player and the computer player.

It prints the board and the moves made.

If there’s a winner, it announces the result; otherwise, it declares a tie.

Now, let’s play a virtual round! You’re “x,” and I’ll be the random computer player (“o”). Here’s the initial board

|0|1|2|
|3|4|5|
|6|7|8|
