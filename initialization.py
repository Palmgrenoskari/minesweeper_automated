from pyautogui import *
from time import sleep

#TODO: Detect windowed browser, change to fullscreen
#TODO: Detect other themes and convert to dark theme
#TODO: Other than brave-browser?

def open_browser():
  press("win")
  sleep(0.5)
  write("brave", interval=0.1)
  sleep(0.1)
  press("enter")
  sleep(1)

def open_minesweeper():
  write("minesweeper.online", interval=0.1)
  sleep(0.1)
  press("enter")
  sleep(1)

def dark_theme():
  try:
    # Find the theme icon, only possible if light mode
    theme_xy = center(locateOnScreen("./images/initialization/theme_light.png", confidence=0.9))
    moveTo(theme_xy.x, theme_xy.y, duration=0.5)
    click()
    sleep(0.2)
    # Find the dark theme option and click it
    dark_xy = center(locateOnScreen("./images/initialization/dark_theme_option.png", confidence=0.9))
    moveTo(dark_xy.x, dark_xy.y, duration=0.5)
    click()
    sleep(0.2)
  except:
    # Pass if already dark theme.
    pass

def start_ngg():
  # ngg = no guessing game
  try:
    start_xy = center(locateOnScreen("./images/initialization/no_guessing_mode.png", confidence=0.90))
    moveTo(start_xy.x, start_xy.y, duration=0.5)
    click()
    sleep(0.2)
  except:
    # Pass for now.
    pass
  
  try:
    # Find unselected easy mode option, if not found, means already easy mode.
    easy_xy = center(locateOnScreen("./images/initialization/easy_mode.png", confidence=0.95))
    moveTo(easy_xy.x, easy_xy.y, duration=0.5)
    click()
    sleep(0.2)
  except:
    # Pass, already on easy mode.
    pass

def adjust_zoom():
  
  try:
    # Relatively low confidence, since the current value can be anything
    zoom_xy = center(locateOnScreen("./images/initialization/zoom_dropdown.png", confidence=0.75))
    moveTo(zoom_xy.x, zoom_xy.y, duration=0.5)
    click()
    sleep(0.2)
    
    # Move mouse to a value to make sure nothing around the 34 is highlighted
    moveTo(zoom_xy.x, zoom_xy.y + 50, duration=0.2)
    sleep(0.2)

    # Find the 34 option and click it
    zoom_34_xy = center(locateOnScreen("./images/initialization/zoom_34.png", confidence=0.95))
    moveTo(zoom_34_xy.x, zoom_34_xy.y, duration=0.5)
    click()
    sleep(0.2)

  except:
    # Pass for now.
    pass

def initialize():
  """
  Opens browser
  Navigates to minesweeper.online site
  Sets dark theme if not already set
  Starts no guessing game, selects easy mode
  Adjusts zoom to 34
  """
  
  open_browser()
  open_minesweeper()
  dark_theme()
  start_ngg()
  adjust_zoom()
