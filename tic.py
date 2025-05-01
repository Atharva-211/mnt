def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def simple_bot_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return i, j

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" "]*3 for _ in range(3)]
    print("Tic Tac Toe! You are X. Computer is O.")

    while True:
        print_board(board)
        
        # Player move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != " ":
            print("Cell taken! Try again.")
            continue
        board[row][col] = "X"
        if check_winner(board, "X"):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Computer move
        r, c = simple_bot_move(board)
        board[r][c] = "O"
        print(f"Computer moves to ({r}, {c})")
        if check_winner(board, "O"):
            print_board(board)
            print("Computer wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

play_game()
