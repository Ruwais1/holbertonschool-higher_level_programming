#!/usr/bin/python3
"""N Queens puzzle solver using backtracking algorithm."""
import sys


def print_usage_and_exit():
    """Prints usage message and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def print_number_error_and_exit():
    """Prints number error message and exits with status 1."""
    print("N must be a number")
    sys.exit(1)


def print_value_error_and_exit():
    """Prints value error message and exits with status 1."""
    print("N must be at least 4")
    sys.exit(1)


def is_safe(placed_queens, row, col):
    """
    Checks if a queen can be safely placed at (row, col).
    
    Args:
        placed_queens (list): List of coordinates [r, c] for placed queens.
        row (int): The row to check.
        col (int): The column to check.
        
    Returns:
        bool: True if safe, False otherwise.
    """
    for r, c in placed_queens:
        # Check same column or same diagonal
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(n, row, placed_queens):
    """
    Recursively finds all solutions for the N queens problem.
    
    Args:
        n (int): The size of the board / number of queens.
        row (int): The current row being evaluated.
        placed_queens (list): The list of placed queens coordinates.
    """
    if row == n:
        # All queens are placed successfully, print the solution
        print(placed_queens)
        return

    for col in range(n):
        if is_safe(placed_queens, row, col):
            # Try placing queen at (row, col)
            placed_queens.append([row, col])
            
            # Move to the next row
            solve_nqueens(n, row + 1, placed_queens)
            
            # Backtrack: remove the queen and try the next column
            placed_queens.pop()


def main():
    """Main execution function handling arguments and validation."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()

    if n < 4:
        print_value_error_and_exit()

    solve_nqueens(n, 0, [])


if __name__ == "__main__":
    main()
