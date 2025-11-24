A simple, easy Minesweeper game that runs in the terminal.  
Features include saving/loading games and tracking your best completion time.

--------------------------

 **Features:**

- **Classic Minesweeper gameplay** on a 9×9 grid with 10 mines 
- **Text-based interface** – play directly in your terminal   
- **Recursive reveal of empty cells** (0-neighbour cells auto-expand)   
- **Flagging system** - used to mark suspected mines   
- **Save & resume games** via a binary save file   
- **Best time tracking** stored locally in a text file

----

  **Directory Structure:**

-> board.py         # Board class: mine placement, neighbour counts, printing, reveal-all  
-> game_logic.py    # Core game logic: reveal, flag, win-check  
-> file_manager.py  # Handles best-time loading & saving (time.txt)  
-> game_state.py    # Save/load/delete game state (savegame.dat)  
-> main.py          # Game entry point & main loop   
-> savegame.dat     # Saved game data  
-> time.txt         # Stores best completion time  

----------

**Game Instructions:**

+ Board is 9×9 with 10 hidden mines  
+ Cells start hidden  
+ Your commands:  
     r row col → reveal a cell  
     f row col → flag/unflag a suspected mine  

+ q → save and quit  
+ Revealing a mine = game over.  
+ Reveal all non-mine cells = you win.  
+ Empty cells auto-expand when revealed.  
+ Game auto-saves on quit and auto-loads on next launch.  

----------

**Setup Instructions:**

1. Make sure you have Python 3 installed.
2. Put all project files in the same folder.
3. Open terminal in that folder.
4. Run the game:
     
      python main.py
     


***ENJOY***  
what is this diddy blud doin on my calculator


ENJOY !!!

