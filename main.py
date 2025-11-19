"""
main.py

The main execution file for the Minesweeper console game.
It initializes the game, handles the main game loop, processes user input,
and manages game state transitions (win, loss, save, quit).
"""
from board import Board
import game_logic
import file_manager
import game_state
import time

def user_input(board_size):
    """
    Handles user input during the game loop.
    
    It prompts the user to enter an action ('r' for reveal, 'f' for flag) 
    followed by row and column coordinates, or 'q' to quit.
    It validates the number of arguments, the action command, and the 
    coordinates against the board size.
        
    Returns:
        tuple: (action: str, row: int, col: int) if valid, 
               otherwise (None, None, None).
               
    """
    try:
        user_input = input("Enter action ('r'/'f' row col) or 'q' to save/quit: ").split()
        
        if len(user_input) == 1 and user_input[0].lower() == 'q':
            return 'q', None, None

        if len(user_input) != 3:
            print("Invalid input. Please enter 3 values (action row col) or 'q'.")
            return None, None, None

        cmd = user_input[0].lower()
        row = int(user_input[1])
        col = int(user_input[2])

        if cmd!='r' and cmd!='f' and cmd!='q':
            print("Invalid action. Type 'r', 'f', or 'q'.")
            return None, None, None

        if not ((row < board_size and row>=0) and (col>=0 and col < board_size)):
            print(f"Invalid position.")
            return None, None, None
            
        return cmd, row, col

    except ValueError:
        print("Invalid input. Row and column must be integers.")
        return None, None, None

def run_game():
    """
    Initializes and manages the main Minesweeper game loop.
    
    This function handles:
    1. Board initialization and loading a saved game (if available).
    2. Displaying the best time to beat.
    3. Tracking the elapsed time using 'time.time()'.
    4. Processing user moves (reveal or flag) until the game is won, lost, or quit.
    5. Saving the time/game state upon ending the game.
    
    """
    board = Board(size=9, num_mines=10)
    g_over = False
    g_won = False
    previous_elapsed_time = 0

    loaded_grid, loaded_player_grid, loaded_time = game_state.load_game()
    if loaded_grid:
        print("Loading the saved game....")
        board.grid = loaded_grid
        board.player_grid = loaded_player_grid
        previous_elapsed_time = loaded_time

    best_time = file_manager.load_time()
    if best_time:
        print(f"The best time to beat is: {best_time:.2f} seconds.")

    start_time = time.time()
    cmd = None

    while not g_over and not g_won:
        board.print_board()
        if previous_elapsed_time > 0:
            print(f"(Time elapsed so far: {previous_elapsed_time:.2f}s)")
            
        cmd, row, col = user_input(board.size)
        
        if cmd is None:
            continue

        if cmd == 'q':
            g_over = True
            continue

        if cmd == 'r':
            if not game_logic.reveal(board, row, col):
                g_over = True
                print("You hit a bloody mine. GOODBYEEE !!!.")        
        elif cmd == 'f':
            game_logic.flag(board, row, col)            
        
        if not g_over:
            g_won = game_logic.check_win(board)

    end_time = time.time()
    time_taken = (end_time - start_time) + previous_elapsed_time

    if cmd == 'q':
        game_state.save_game(board, time_taken)
        print(f"Game saved with {time_taken:.2f} seconds elapsed. Bye!")
    else:
        game_state.delete_save()
        
        board.reveal()
        board.print_board()

        if g_won:
            print(f"YOU WIN!!! You took {time_taken:.2f} seconds to complete.")
            file_manager.save_time(time_taken)    

if __name__ == "__main__":
    print("Welcome to Minesweeper!")
    run_game()
