"""
game_logic.py

Contains the core non-board-specific logic for the Minesweeper game,
which includes functions for revealing cells, placing/removing flags, 
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
        
    board.player_grid[row][col] = board.actual_grid[row][col]

    if board.actual_grid[row][col] == '*':
        return False  

    elif board.actual_grid[row][col] == '0':
        for nr, nc in board._neighbours(row, col):      #recursion
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
        board.player_grid[row][col] = 'F'

    elif board.player_grid[row][col] == 'F':
        board.player_grid[row][col] = 'H'
    else:
        print("Cannot flag that cell.")

def check_win(board):
    """
    Checks if the player has won the game.
    
    The win condition is met when every single non-mine cell on the board
    has been revealed. 
    If any cell that is NOT a mine is still hidden ('H'), 
    the game is not won.
        
    Returns True if the player has won, False otherwise.
    """
    for r in range(9):
        for c in range(9):
            mine = (board.actual_grid[r][c] == '*')
            hidden = (board.player_grid[r][c] == 'H')            
            
            if ((not mine) and hidden):
                return False                
    return True

