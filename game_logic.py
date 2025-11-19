"""
game_logic.py

Contains the core non-board-specific logic for the Minesweeper game,
including functions for revealing cells, placing/removing flags, 
and checking the win condition.
"""

def reveal(board, row, col):
    """
    Attempts to reveal a cell at the given (row, col) coordinates.
    
    If the cell is already revealed or flagged, it does nothing and returns True.
    If the cell contains a mine ('*'), the player loses and it returns False.
    If the cell contains a '0' (no adjacent mines), it recursively calls itself 
    to automatically reveal all valid, hidden neighbours.
    Otherwise, it reveals the number and returns True.
        
    Returns:
        bool: False if a mine was hit (game over), True otherwise.
    """
    if not board.is_valid(row, col) or board.player_grid[row][col] != 'H':
        return True
        
    board.player_grid[row][col] = board.grid[row][col]

    if board.grid[row][col] == '*':
        return False  

    elif board.grid[row][col] == '0':
        # Recursively reveal neighbours if the cell is clear ('0')
        for nr, nc in board._neighbours(row, col):
            reveal(board, nr, nc)

    return True 

def flag(board, row, col):
    """
    Toggles the flag ('F') status on a cell if it is currently hidden ('H').
    
    If the cell is hidden, it becomes flagged. If it is flagged, it becomes hidden.
    If the cell is already revealed (a number or mine), it cannot be flagged.
    
    """
    if not board.is_valid(row, col):
        print("Invalid position.")
        return

    if board.player_grid[row][col] == 'H':
        # Change Hidden to Flagged
        board.player_grid[row][col] = 'F'
    elif board.player_grid[row][col] == 'F':
        # Change Flagged back to Hidden
        board.player_grid[row][col] = 'H'
    else:
        print("Cannot flag that cell.")

def check_win(board):
    """
    Checks if the player has won the game.
    
    The win condition is met when every single non-mine cell on the board
    has been revealed. If any cell that is NOT a mine is still hidden ('H'), 
    the game is not won.
        
    Returns:
        bool: True if the player has won, False otherwise.
    """
    for r in range(9):
        for c in range(9):
            mine = (board.grid[r][c] == '*')
            hidden = (board.player_grid[r][c] == 'H')            
            
            # If a cell is NOT a mine AND it is still hidden, the player hasn't won.
            if ((not mine) and hidden):
                return False                
    return True
