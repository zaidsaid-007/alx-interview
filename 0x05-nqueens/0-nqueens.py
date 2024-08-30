#!/usr/bin/python3
"""
Module for 0x0C. N Queens.
ALX
Specializations - Interview Preparation ― Algorithms
"""
from sys import argv, exit

def solveNQueens(n):
    """Solves the N-Queens problem and returns all possible solutions."""
    res = []
    queens = [-1] * n  # Initialize the list to store queen positions

    def dfs(row):
        """Performs a depth-first search to place queens row by row."""
        if row == n:  # All queens have been placed successfully
            res.append(queens[:])
            return
        for col in range(n):
            queens[row] = col
            if is_valid(row):
                dfs(row + 1)

    def is_valid(row):
        """Checks if the current placement of queens is valid."""
        for prev_row in range(row):
            # Check column and diagonal conflicts
            if (queens[prev_row] == queens[row] or
                    abs(queens[prev_row] - queens[row]) == row - prev_row):
                return False
        return True

    def format_solutions(res):
        """Formats the list of solutions into the required output format."""
        return [["." * i + "Q" + "." * (n - i - 1) for i in queens] for queens in res]

    dfs(0)
    return format_solutions(res)


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

    solutions = solveNQueens(n)
    for solution in solutions:
        for row in solution:
            print(row)
        print()