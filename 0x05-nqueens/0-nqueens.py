#!/usr/bin/python3
"""
Module for 0x0C. N Queens.
ALX
Specializations - Interview Preparation ― Algorithms
"""

from sys import argv, exit

def solve_n_queens(n):
    """
    Solves the N-Queens problem and returns all possible solutions.
    """
    def is_safe(board, row, col):
        """
        Checks if a queen can be placed at a given position.
        """
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row, board):
        """
        Recursively places queens on the board.
        """
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                place_queens(n, row + 1, board)

    result = []
    place_queens(n, 0, [-1] * n)
    return result

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    solutions = solve_n_queens(n)
    for solution in solutions:
        print([list((i, j)) for i, j in enumerate(solution)])
