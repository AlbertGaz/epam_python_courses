"""Homework 7.3."""
from typing import List, Optional, Set


def check_diagonals(board: List[List]) -> Optional[bool]:
    """Check if there is winner in diagonal."""
    if len({board[i][i] for i in range(3)}) == 1 and board[1][1] != "-":
        return board[1][1]
    if len({board[2 - i][i] for i in range(3)}) == 1 and board[1][1] != "-":
        return board[1][1]
    return None


def check_rows_columns(board: List[List]) -> (Set, bool):
    """Check if there is winner in rows and columns."""
    res = set()
    finished = True
    matrix = board + list(zip(*board))
    for row in matrix:
        if len(set(row)) == 1 and row[0] != "-":
            res.add(row[0])
        if "-" in row:
            finished = False
    return res, finished


def tic_tac_toe_checker(board: List[List]) -> str:
    """Find if there is game has winner or it is draw or unfinished."""
    if check_diagonals(board):
        return f"{board[1][1]} wins!"
    res, finished = check_rows_columns(board)
    if len(res) == 1:
        return f"{str(*res)} wins!"
    if len(res) == 2 or finished:
        return "draw!"
    return "unfinished!"
