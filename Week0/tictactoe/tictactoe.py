"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    cant_x = 0
    cant_o = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                cant_x += 1
            elif board[i][j] == O:
                cant_o += 1

    if cant_x == cant_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_movements = []

    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                possible_movements.append((i,j))

    return possible_movements


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)

    if action:
        if action[0] < 0 or action[1] < 0 or action[0] > 2 or action[1] > 2:
            raise Exception("Movement not valid.")

        if player(board) == X:
            new_board[action[0]][action[1]] = X
        else:
            new_board[action[0]][action[1]] = O

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != EMPTY):
        return board[0][0]
    elif (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != EMPTY):
        return board[0][2]
    elif (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[1][0] != EMPTY):
        return board[0][0]
    elif (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[1][1] != EMPTY):
        return board[0][1]
    elif (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[1][2] != EMPTY):
        return board[0][2]
    elif (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][1] != EMPTY):
        return board[0][0]
    elif (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][1] != EMPTY):
        return board[1][0]
    elif (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][1] != EMPTY):
        return board[2][0]
    elif (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != EMPTY):
        return board[0][0]
    elif (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != EMPTY):
        return board[0][0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not actions(board):
      return True
    else:
      return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        value, action = max_value(board)
    else:
        value, action = min_value(board)

    return action


def max_value(board):
    if terminal(board):
        return utility(board), None
    v = -100000
    new_move = None

    for action in actions(board):
        aux_val, new_action = min_value(result(board, action))
        if aux_val > v:
            v = aux_val
            new_move = action

    return v, new_move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = 1000000
    new_move = None

    for action in actions(board):
        aux_val, new_action = max_value(result(board, action))
        if aux_val < v:
            v = aux_val
            new_move = action


    return v, new_move
