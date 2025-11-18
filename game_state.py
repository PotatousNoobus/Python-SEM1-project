import pickle
import os

SAVE_FILENAME = "minesweeper_save.dat"

def save_game(board, elapsed_time):
    state = {
        'grid': board.grid,
        'player_grid': board.player_grid,
        'elapsed_time': elapsed_time
    }
    
    try:
        with open(SAVE_FILENAME, 'wb') as file:
            pickle.dump(state, file)
        print("Game saved.")
    except (IOError, pickle.PicklingError) as e:
        print(f"Error saving game: {e}")

def load_game():
    if not os.path.exists(SAVE_FILENAME):
        return None, None, None
        
    try:
        with open(SAVE_FILENAME, 'rb') as file:
            state = pickle.load(file)
            
            if 'grid' in state and 'player_grid' in state and 'elapsed_time' in state:
                return state['grid'], state['player_grid'], state['elapsed_time']
            else:
                return None, None, None
    except (IOError, pickle.UnpicklingError, EOFError) as e:
        print(f"Error loading saved game: {e}")
        return None, None, None

def delete_save():
    if os.path.exists(SAVE_FILENAME):
        try:
            os.remove(SAVE_FILENAME)
        except IOError as e:

            print(f"Error deleting save file: {e}")
