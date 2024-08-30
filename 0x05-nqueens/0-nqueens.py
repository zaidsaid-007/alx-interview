#!/usr/bin/python3
"""
Module for 0x0C. N Queens.
ALX
Specializations - Interview Preparation ― Algorithms
"""
from sys import argv, exit

def solveNQueens(n):
    """Solves the N-Queens problem and returns all solutions."""
    res = []
    queens = [-1] * n  # Initialize the queens' positions

    def dfs(row):
        """Performs a DFS to place queens row by row."""
        if row == n:  # All queens have been placed
            res.append(queens[:])
            return
        for col in range(n):
            queens[row] = col
            if is_valid(row):  # Check if placing the queen here is valid
                dfs(row + 1)

    def is_valid(row):
        """Checks if the current queen placement is valid."""
        for i in range(row):
            if queens[i] == queens[row] or abs(queens[i] - queens[row]) == row - i:
                return False
        return True

    def format_solutions(res):
        """Formats the result into a list of lists of coordinates."""
        actual_boards = []
        for queens in res:
            board = [[row, col] for row, col in enumerate(queens)]
            actual_boards.append(board)
        return actual_boards

    dfs(0)
    return format_solutions(res)

if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = solveNQueens(n)
    for solution in solutions:
        print(solution)
