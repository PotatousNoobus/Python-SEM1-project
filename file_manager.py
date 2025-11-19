"""
file_manager.py

Handles saving and loading the best completion time for the Minesweeper game.
This module uses a simple text file (defined by FILENAME) to store the fastest 
time achieved by the player.
"""
import os

# The name of the file where the best time is stored.
FILENAME = "minesweeper_save_time.txt"

def load_time():
    """
    Tries to read the current best time from the specified file.
    
    Returns:
        float: The saved best time, or None if the file does not exist, 
               or if the file content is invalid (not a number).
    """
    if not os.path.exists(FILENAME):
        return None
        
    try:
        with open(FILENAME, 'r') as file:
            return float(file.read())
    except ValueError:
        # This catches errors if the file content isn't a valid number
        return None

def save_time(time_taken):
    """
    Compares the newly achieved 'time_taken' with the current saved best time.
    
    If the new time is faster, it overwrites the file with the new best time 
    and prints a congratulatory message.
    
    """
    current_best = load_time()
    
    if current_best is None or time_taken < current_best:
        try:
            with open(FILENAME, 'w') as file:
                file.write(str(time_taken))
            print(f"New best: {time_taken:.2f} seconds!")
        except IOError:
            # This catches errors if the program can't write to the file
            print("Best time couldnt be saved")

