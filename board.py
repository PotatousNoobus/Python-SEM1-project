"""
board.py

Contains the Board class, which manages the core game grid,
mine placement, number calculation, and board display for Minesweeper.
"""
import random

class Board:
    """
    Represents the Minesweeper game board. It holds two 9x9 grids: 
    the secret grid with mines and numbers (`self.grid`), and 
    the player's visible grid (`self.player_grid`).
    """
    def __init__(self, size=9, num_mines=10):
        """
        Initializes a new Board object. 
        It sets the board dimensions and number of mines, then calls 
        the helper methods to set up the grids, place the mines, and calculate the numbers.
        """
        self.size = size
        self.num_mines = num_mines
        self.actual_grid = []
        self.player_grid = []
        
        self._init_grids()        
        self._place_mines()
        self._calc_num()

    def _init_grids(self):
        """
        Initializes the two 9x9 grid structures manually.
        - self.grid: Filled with '0's initially, later holds mines ('*') and numbers.
        - self.player_grid: Filled with 'H' (Hidden), which is what the player sees.
        """
        
        self.actual_grid = [['0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0']]

        self.player_grid = [['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H']]
    
    def _place_mines(self): 
        """
        Randomly distributes 10 mines ('*') across the 9x9 grid.
        It uses a while loop to ensure the correct number of mines are placed 
        without overlap.
        """
        curr_mines = 0

        while (curr_mines < 10):
            row = random.randint(0, 8)
            col = random.randint(0, 8)            
            
            if self.actual_grid[row][col] != '*':
                self.actual_grid[row][col] = '*'
                curr_mines+=1

    def is_valid(self, row, col):
        """
        Checks if the given (row, col) coordinates are inside the 9x9 board.
        Returns True if the position is on the board, False otherwise.
        """
        if ((row>=0 and row<9) and (col>=0 and col<9)):
            return True
        else:
            return False

    def _neighbours(self, row, col):
        """
        Calculates and returns a list of valid coordinates for all 8 adjacent cells.
        This helps in checking for mines or recursively revealing clear areas.
        """
        all_neighbours = [] #list of lists of all the neighbours of the cell
        for nr in [0,1,-1]:
            for nc in [0,1,-1]: #to check all 8 possible combinations
                if nr==0 and nc==0:
                    continue  
                else:                
                    nrow = row + nr
                    ncol = col + nc            
                    if self.is_valid(nrow, ncol):
                        all_neighbours.append([nrow,ncol])
        return all_neighbours
    
    def _calc_num(self):
        """
        Fills the non-mine cells in self.grid with the count of adjacent mines.
        It iterates through the board and uses _neighbours() to count the '*'s.
        """
        for r in range(self.size):
            for c in range(self.size):
                if self.actual_grid[r][c] == '*':
                    continue
                
                mine_count = 0
                for nr, nc in self._neighbours(r,c): #neighbours = [(nr,nc)]
                    if self.actual_grid[nr][nc] == '*':
                        mine_count+=1 
                
                self.actual_grid[r][c] = str(mine_count)

    def print_board(self):
        """
        Displays the current state of the game board (self.player_grid) to the user.
        It includes the column and row indices for easier input.
        """
        #print("   " + " ".join([str(i) for i in range(self.size)]))

        print("   ", end="")
        for i in range(9):
            print(f"{str(i)} ", end="")

        print()

        #print("  " + "-" * (self.size * 2))

        print("  ", end="")
        for i in range(18):
            print("-", end="")
        print()
        
        for rindex, r in enumerate(self.player_grid):
            print(f"{rindex} |" + " ".join(r))
        print()

    def reveal(self):
        """
        Forces the player's grid (self.player_grid) to show the full internal grid (self.grid).
        This function is typically called when the game ends (win or loss) to show all mines and numbers.
        """
        for r in range(9):
            for c in range(9):
                self.player_grid[r][c] = self.actual_grid[r][c]
