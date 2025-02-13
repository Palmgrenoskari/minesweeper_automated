from pyautogui import alert, locateOnScreen, center, moveTo, click
from time import sleep

def start_game():
  alert("Starting game...", timeout=2000)
  
  starting_point_xy = center(locateOnScreen("./images/gameplay/game_entrypoint.png", confidence=0.95))
  moveTo(starting_point_xy.x, starting_point_xy.y, duration=0.5)
  click()
  sleep(0.2)

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
