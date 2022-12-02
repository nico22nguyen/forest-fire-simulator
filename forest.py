import random
from graphics import *
from tree import Tree

COL_SPACE = 45
ROW_SPACE = 50
TREE_DIM = 42
INITIAL_X = 20
INITIAL_Y = 20

class Forest:
  def __init__(self, cols, rows, win):
    self.cols = cols
    self.pixel_width = cols * COL_SPACE + (INITIAL_X - TREE_DIM / 2)
    self.rows = rows
    self.pixel_height = rows * ROW_SPACE + (INITIAL_Y - TREE_DIM / 2)
    self.win = win
    self.is_burning = False
    self.create_forest()
    self.draw_forest()
      
  def create_forest(self):
    self.tree_grid = [] #empty list
    x = INITIAL_X
    y = INITIAL_Y
    for row in range(self.rows):
        self.tree_grid.append([])
        for _ in range(self.cols):
            tree = Tree(x, y, self.win)
            self.tree_grid[row].append(tree)
            x += COL_SPACE
        y += ROW_SPACE
        x = INITIAL_X
                             
  def draw_forest(self):
    for row in self.tree_grid:
      for tree in row:
        tree.draw_self()

  def burn_tick(self, probability):
    to_burn = []
    for row in range(self.rows):
      for col in range(self.cols):
        tree = self.tree_grid[row][col]

        # burnt trees and unlit trees dont spread fire
        if tree.burn_severity == 3 or tree.burn_severity == 0:
          continue

        to_burn.append(tree)

        neighbors = []
        if col > 0:
          neighbors.append(self.tree_grid[row][col])
        if col < self.cols - 1:
          neighbors.append(self.tree_grid[row][col + 1])
        if row > 0:
          neighbors.append(self.tree_grid[row - 1][col])
        if row < self.rows - 1:
          neighbors.append(self.tree_grid[row + 1][col])

        for neighbor in neighbors:
          will_burn = random.random() < probability
          if will_burn:
            to_burn.append(neighbor)

    all_burnt = len(to_burn) == 0
    for tree in to_burn:
      tree.burn()
      
    return all_burnt

  def burn(self, probability):
    self.is_burning = True
    time = 0
    all_burnt = False

    while not all_burnt:
      all_burnt = self.burn_tick(probability)
      time += 1

    self.is_burning = False

    summary_box, summary_text = self.render_summary(self.win, time)
    self.win.getMouse()
    summary_text.undraw()
    summary_box.undraw()

  def render_summary(self, win, num_steps):
    COLOR = 'bisque'
    TEXT_COLOR = 'red'
    HEIGHT = 50
    OFFSET = 20
    FONT_SIZE = 20
    text_content = f'The fire subsided after {num_steps} steps. Click anywhere to close.'

    box = Rectangle(Point(OFFSET, (self.pixel_height - HEIGHT) / 2), Point(self.pixel_width - OFFSET, (self.pixel_height + HEIGHT) / 2))
    box.setFill(COLOR)

    text = Text(Point(self.pixel_width / 2, self.pixel_height / 2), text_content)
    text.setTextColor(TEXT_COLOR)
    text.setSize(FONT_SIZE)
    
    box.draw(win)
    text.draw(win)

    return box, text

  def reset(self):
    for row in self.tree_grid:
      for tree in row:
        tree.reset()

  def get_tree_from_click(self, click):
    x_start = INITIAL_X - TREE_DIM / 2
    y_start = INITIAL_Y - TREE_DIM / 2
    total_height = self.pixel_height - y_start
    total_width = self.pixel_width - x_start

    # out of bounds
    if click.getX() > self.pixel_width or click.getY() > self.pixel_height or total_height < 0 or total_width < 0:
      return None

    row = int((click.getY() - y_start) / (total_height) * self.rows)
    col = int((click.getX() - x_start) / (total_width) * self.cols)

    return self.tree_grid[row][col]