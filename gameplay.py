from pyautogui import alert, locateOnScreen, center, moveTo, click
from time import sleep

from utils.utils import easy_grid

def start_game():
  alert("Starting game...", timeout=2000)
  
  starting_point_xy = center(locateOnScreen("./images/gameplay/game_entrypoint.png", confidence=0.95))
  moveTo(starting_point_xy.x, starting_point_xy.y, duration=0.5)
  click()
  sleep(0.2)

def scan_board():
  """
  Goes through each cell in the grid and updates all number's surroundings.
  Marks cells that are guaranteed mines.
  """
  pass
def flag_mines():
  """
  Goes through each cell in the grid and flags cells that are marked as mines.
  """
  pass
  
def open_safe_cells():
  """
  Goes through each cell in the grid and opens numbers that are marked as completed.
  There is this super nice QoL feature in minesweeper.online that you can click the number to reveal all the cells around it.
  Only works if has enough mines around it.
  """
  pass
  
def play():
  """
  Plays the game
  
  Implement some sort of loop that goes through the board in 2 modes iteratively:
  
  1) Look for guaranteed mines
  2) Open all safe squares
  
  ------------------------------------------------------------------
  
  Above might work for easy difficulty, but to eventually move to medium, hard or even evil difficulty,
  it is required to implement algorithms for the more complex patterns that involve chains of logic shared between multiple numbers.
  """
  start_game()
  scan_board()
  flag_mines()
  open_safe_cells()

