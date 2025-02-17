from pyautogui import alert, locateOnScreen, center, moveTo, click, locateAllOnScreen
from time import sleep

from utils.utils import easy_board

def start_game():
  alert("Starting game...", timeout=2000)
  
  starting_point_xy = center(locateOnScreen("./images/gameplay/game_entrypoint.png", confidence=0.95))
  moveTo(starting_point_xy.x, starting_point_xy.y, duration=0.5)
  click()
  sleep(0.2)
  
def scan_value(value, image, board):
  """
  Scans the board for single value and updates those cells accordingly
  """
  boxes = list(locateAllOnScreen(f"./images/gameplay/{image}.png", confidence=0.98))
  # Remove duplicates, locateAllOnScreen tends to find the same box multiple times with ~1-3 pixels differences
  unique_boxes = remove_duplicates(boxes)
  # Find all center coordinates of ones
  unique_centers = [center(x) for x in unique_boxes]

  # Update board states for cells containing these centers
  for center_point in unique_centers:
    for cell_coords, cell_data in board.items():
      # Skip if satisfied or mine, those cells are already completed
      if cell_data['state'] == "satisfied" or cell_data['state'] == "mine":
        continue
      
      cell_area = cell_data['area']
      # Check if center point falls within this cell's area
      if (cell_area.left <= center_point.x <= cell_area.left + cell_area.width and
        cell_area.top <= center_point.y <= cell_area.top + cell_area.height):
        board[cell_coords]['state'] = value

def remove_duplicates(boxes):
  """
  Removes duplicate boxes from the list
  """
  unique_boxes = []
  used_indices = set()

  for i in range(len(boxes)):
    if i in used_indices:
      continue
        
    current_box = boxes[i]
    used_indices.add(i)
    
    # Compare with remaining boxes
    for j in range(i + 1, len(boxes)):
      if j in used_indices:
        continue
            
      next_box = boxes[j]
      # If boxes are within 5 pixels in both x and y coordinates
      if (abs(current_box.left - next_box.left) <= 5 and abs(current_box.top - next_box.top) <= 5):
        used_indices.add(j)
    
    unique_boxes.append(current_box)
  
  return unique_boxes

def scan_board(board):
  """
  Checks the whole board and updates cell states accordingly
  """
  # Scan for numbers 1-6
  scan_value("1", "num_1", board)
  scan_value("2", "num_2", board)
  scan_value("3", "num_3", board)
  scan_value("4", "num_4", board)
  scan_value("5", "num_5", board)
  scan_value("6", "num_6", board)
  
  # Scan for not opened and mine
  scan_value("not_opened", "not_opened", board)
  scan_value("mine", "mine", board)

            
def analyze_board(board):
  """
  Goes through each number in the grid, checks the neighbors and flags
  guaranteed mines as mine and satisfied numbers as satisfied.
  """
  # List of states we want to check
  allowed_states = ["1", "2", "3", "4", "5", "6"]
  
  for _, cell_data in board.items():
    # Skip if cell is not a number
    if cell_data["state"] not in allowed_states:
      continue
    
    # Convert state to integer for comparison
    target_mines = int(cell_data["state"])
    
    # Count mines and unopened cells among neighbors
    neighbor_mines = 0
    unopened_neighbors = []
    
    for neighbor_coords in cell_data["neighbors"]:
      neighbor_state = board[neighbor_coords]["state"]
      if neighbor_state == "mine":
        neighbor_mines += 1
      elif neighbor_state == "not_opened":
        unopened_neighbors.append(neighbor_coords)
    
    # Case 1: Number matches exactly with surrounding mines
    if neighbor_mines == target_mines:
      cell_data["state"] = "satisfied"
        
    # Case 2: Number matches with (mines + unopened)
    # This means all unopened must be mines
    if neighbor_mines + len(unopened_neighbors) == target_mines:
      for neighbor_coords in unopened_neighbors:
        board[neighbor_coords]["state"] = "mine"
  
def flag_mines_and_open_safe_cells(board):
  """
  Goes through each cell in the grid and opens numbers that are marked as completed.
  There is this super nice QoL feature in minesweeper.online that you can click the number to reveal all the cells around it.
  Only works if has enough mines around it.
  """
  # In two separate loops because we want to put all the mines first before opening any cells
  # Since once a cell is clicked, it will be marked as clicked = True and won't be clicekd again
  print("Flagging mines and opening safe cells...")
  for _, cell_data in board.items():
    if cell_data['state'] == "mine" and not cell_data['clicked']:
      x, y = cell_data['center']
      moveTo(x, y, duration=0.3)
      sleep(0.1)
      click(button="right")
      cell_data['clicked'] = True
      
  for _, cell_data in board.items():
    if cell_data['state'] == "satisfied" and not cell_data['clicked']:
      x, y = cell_data['center']  
      moveTo(x, y, duration=0.3)
      sleep(0.1)
      click()
      cell_data['clicked'] = True

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
  scan_board(easy_board)
  for _ in range(10):
    scan_board(easy_board)
    analyze_board(easy_board)
    flag_mines_and_open_safe_cells(easy_board)
