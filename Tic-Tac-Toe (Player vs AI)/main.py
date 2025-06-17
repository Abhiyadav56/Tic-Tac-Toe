import random

# Set up the game board (like laying out 9 tiles in a 3x3 grid)
board = [' '] * 9

def show_board():
    """Draws the game board in a 3x3 format."""
    print()
    for row in range(3):
        i = row * 3
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if row < 2:
            print("---|---|---")
    print()

def get_free_spots():
    """Returns all indexes where a move can still be made."""
    return [i for i, cell in enumerate(board) if cell == ' ']

def has_winner(brd, symbol):
    """Checks all winning combinations for the given symbol."""
    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # Vertical
        [0, 4, 8], [2, 4, 6]               # Diagonal
    ]
    return any(all(brd[i] == symbol for i in line) for line in winning_lines)

def is_draw():
    """Checks if the game ended in a draw (no more moves)."""
    return ' ' not in board

def player_turn():
    """Takes input from the player and places their move."""
    while True:
        try:
            move = int(input("Your move (1-9): ")) - 1
            if move in range(9) and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("That spot's already taken or invalid. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def bot_easy_mode():
    """Bot plays like randomly throwing rock, paper, or scissors."""
    return random.choice(get_free_spots())

def bot_hard_mode():
    """Bot plays smart – like choosing rock when it knows you'll pick scissors."""
    # Try to win
    for move in get_free_spots():
        copy = board[:]
        copy[move] = 'O'
        if has_winner(copy, 'O'):
            return move
    # Try to block player win
    for move in get_free_spots():
        copy = board[:]
        copy[move] = 'X'
        if has_winner(copy, 'X'):
            return move
    # Take center if it's free
    if 4 in get_free_spots():
        return 4
    # Corners first (classic strategy)
    corners = [i for i in [0, 2, 6, 8] if i in get_free_spots()]
    if corners:
        return random.choice(corners)
    # Else just pick something
    return random.choice(get_free_spots())

def bot_turn(difficulty):
    """Handles the bot’s move based on difficulty."""
    print("Bot is thinking...")
    move = bot_easy_mode() if difficulty == 'easy' else bot_hard_mode()
    board[move] = 'O'

def play_game():
    """Runs the full Tic-Tac-Toe game loop."""
    print("Welcome to Tic-Tac-Toe 🤖 vs 🧠")
    difficulty = input("Choose difficulty (easy / hard): ").strip().lower()
    while difficulty not in ['easy', 'hard']:
        difficulty = input("Please type 'easy' or 'hard': ").strip().lower()

    show_board()

    while True:
        # Your turn
        player_turn()
        show_board()
        if has_winner(board, 'X'):
            print("🎉 You won! Smart move.")
            break
        if is_draw():
            print("It's a draw! Well played.")
            break

        # Bot's turn
        bot_turn(difficulty)
        show_board()
        if has_winner(board, 'O'):
            print("Bot wins! It got lucky... or did it?")
            break
        if is_draw():
            print("It's a draw! Nobody cracked the code.")
            break

if __name__ == "__main__":
    play_game()