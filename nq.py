def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1: return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1: return False
        if col + (row - i) < n and board[i][col + (row - i)] == 1: return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_solution(board)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n)
            board[row][col] = 0

def n_queens(n):
    board = [[0] * n for _ in range(n)]
    solve_n_queens(board, 0, n)

n_queens(4)  # Change the value to solve for different N