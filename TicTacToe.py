def display_board(board):
    """
    Prints the board
    :param board: This is the game board list
    :return: Nothing
    """
    print("\n" * 5)
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("-" * 11)
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-" * 11)
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("\n" * 5)


# game_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]
# display_board(game_board)


def player_choose(marker):
    """
    Players can choose their marker.
    :param marker: This is the marker input by the player
    :return: Assign using player1, player2 = player_choose(marker)
    """
    if marker.upper() == "X":
        return "X", "O"
    else:
        return "O", "X"

# player1, player2 = player_choose("O")
# print(player1, player2)


def place_marker(board, position, player):
    """
    Places the marker at a position in the board.
    :param board: This is the game board list
    :param position: This is the index position in the board list
    :param player: This is the marker - Eg. X
    :return: Nothing
    """
    board[position] = player


# game_board = [" " for i in range(10)]
# place_marker(game_board, 3, "X")
# print(game_board)


def space_check(board, position):
    """
    Checks if a space is empty or not.
    :param board: This is the game board list
    :param position: This is the index position it checks for
    :return: True if empty.
    """
    return board[position] in [str(i) for i in range(10)]


# game_board = ["#", "X", " ", "X", "O", "X", "O", "X", "O", "X"]
# print(space_check(game_board, 2))


def board_full(board):
    """
    Checks whether the board is full or not.
    :param board: This is the game board list
    :return: True if board is full
    """
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# game_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]
# print(board_full(game_board))


def check_win(board, player):
    """
    Checks whether or not someone has won.
    :param board: This is the game board list
    :param player: This is the players marker we are checking for
    :return: True if someone has one
    """
    return ((board[1] == player and board[2] == player and board[3] == player) or  # Top row
            (board[4] == player and board[5] == player and board[6] == player) or  # Middle row
            (board[7] == player and board[8] == player and board[9] == player) or  # Bottom row
            (board[1] == player and board[4] == player and board[7] == player) or  # Left column
            (board[2] == player and board[5] == player and board[8] == player) or  # Middle column
            (board[3] == player and board[6] == player and board[9] == player) or  # Last column
            (board[1] == player and board[5] == player and board[9] == player) or  # left to right slanting
            (board[3] == player and board[5] == player and board[7] == player)     # right to left slanting
            )


# game_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]
# display_board(game_board)
# print(check_win(game_board, "O"))


def replay(answer):
    return answer[0].lower() == "y"


# Actual Game Logic!!
game_on = True

while True:
    game_board = [str(i) for i in range(10)] # Game board list, numbers from 0 to 9. 0 to be ignored.
    print("\n" * 100)
    print("Welcome to TicTacToe!\n")
    print("Player 1 goes first.")
    user_marker = input("Choose X or O:\n")
    player1, player2 = player_choose(user_marker) # Assigns player1 and player2 their markers based on player1's choice.
    print(f"Player 2 is {player2}\n")
    turn = "Player 1"

    while game_on:
        display_board(game_board)
        if turn == "Player 1":
            while True:
                try:
                    position = int(input("Where do you want to place your marker? [Choose between 1 - 9]:\n"))
                    while not space_check(game_board, position):
                        position = int(input("Where do you want to place your marker? [Choose between 1 - 9]:\n"))
                    break
                except Exception as e:
                    print("\nPlease enter a valid number!\n")
            place_marker(game_board, position, player1)
            display_board(game_board)
            if check_win(game_board, player1):
                print(f"{turn} has won the game!")
                game_on = False
            else:
                if board_full(game_board):
                    print("The game is a draw...")
                    game_on = False
                else:
                    turn = "Player 2"
        elif turn == "Player 2":
            while True:
                try:
                    position = int(input("Where do you want to place your marker? [Choose between 1 - 9]:\n"))
                    while not space_check(game_board, position):
                        position = int(input("Where do you want to place your marker? [Choose between 1 - 9]:\n"))
                    break
                except Exception as e:
                    print("\nPlease enter a valid number!\n")
            place_marker(game_board, position, player2)
            display_board(game_board)
            if check_win(game_board, player2):
                print(f"{turn} has won the game!")
                game_on = False
            else:
                if board_full(game_board):
                    print("The game is a draw...")
                    game_on = False
                else:
                    turn = "Player 1"

    choice = input("Do you want to play again? [Y/n]:\n")
    if replay(choice):
        game_on = True
    else:
        break
