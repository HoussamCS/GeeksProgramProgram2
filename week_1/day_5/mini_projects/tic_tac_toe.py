def display_board(board):
    print("\nTIC TAC TOE")
    print("*" * 17)
    for row in board:
        print("*", end=" ")
        print(" | ".join(row), end=" *\n")
        print("*" + "---|"*2 + "---*")
    print("*" * 17)


def player_input(player, board):
    while True:
        try:
            row = int(input(f"Player {player}'s turn.\nEnter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if row not in range(3) or col not in range(3):
                print("Row and column must be between 1 and 3.")
            elif board[row][col] != ' ':
                print("This cell is already occupied. Choose another one.")
            else:
                return row, col
        except ValueError:
            print("Please enter valid integers for row and column.")


def check_win(board, player):
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


def check_tie(board):
    return all(cell != ' ' for row in board for cell in row)


def play():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        display_board(board)
        row, col = player_input(current_player, board)
        board[row][col] = current_player
        
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play()
