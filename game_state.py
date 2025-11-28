"""
game_state.py

Handles the saving, loading, and deletion of the ongoing game state
using the built-in 'json' module to serialize the board and elapsed time
into a human-readable text file.
"""
import json
import os

SAVE_FILENAME = "minesweeper_save.json" 

def save_game(board, elapsed_time):
    """
    Saves the current game state (board grids and elapsed time) to a JSON file.
    
    """
    state = {
        'grid': board.actual_grid,
        'player_grid': board.player_grid,
        'elapsed_time': elapsed_time
    }
    
    try:
        with open(SAVE_FILENAME, 'w') as file:
            json.dump(state, file, indent=4) 
        print("Game saved.")
    except (IOError, TypeError) as e:
        print(f"Error saving game: {e}")

def load_game():
    """
    Loads the saved game state from the JSON file.
    
    Returns:
        tuple: (grid, player_grid, elapsed_time) if successful, 
               otherwise (None, None, None).
    """
    if not os.path.exists(SAVE_FILENAME):
        return None, None, None
        
    try:

        with open(SAVE_FILENAME, 'r') as file:
            state = json.load(file)
            
            if 'grid' in state and 'player_grid' in state and 'elapsed_time' in state:
                return state['grid'], state['player_grid'], state['elapsed_time']
            else:
                return None, None, None
    except (IOError, json.JSONDecodeError, EOFError) as e:
        print(f"Error loading saved game: {e}")
        return None, None, None

def delete_save():
    """
    Deletes the saved game file if it exists.
    """
    if os.path.exists(SAVE_FILENAME):
        try:
            os.remove(SAVE_FILENAME)
            print("Save file deleted.") 
        except IOError as e:
            print(f"Error deleting save file: {e}")

