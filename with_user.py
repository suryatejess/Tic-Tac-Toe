def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_valid_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column, separated by space): ").split())
            if board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. That cell is already occupied.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers between 0 and 2.")

def play_tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        player = players[current_player]
        print(f"Player {player}'s turn")
        row, col = get_valid_move(board)
        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    play_tic_tac_toe()
