import random
from graphics import *
from draw import *
from forest import Forest

def main():
  win = GraphWin("Forest Fire Simulation", 1000, 500)
  win.setBackground('white')

  forest = Forest(15, 10, win)
  input_field, buttons = init_inputs(win)
  quit_button = render_quit_button(win)

  clicked_tree = None

  while True:
    click = win.getMouse()
    if point_in_rect(click, buttons[0]):
      handle_random_start(forest, input_field)
    elif point_in_rect(click, buttons[1]):
      handle_click_start(forest, input_field, clicked_tree)
    elif point_in_rect(click, buttons[2]):
      handle_reset(forest)
    elif point_in_rect(click, quit_button):
      win.close()
      print('Goodbye!')
      return
    else:
      if forest.is_burning:
        continue
      clicked_tree = forest.get_tree_from_click(click)

def get_probability(input_field):
  prob = None
  try:
    prob = float(input_field.getText())
    if prob < 0 or prob > 1:
      raise ValueError
    input_field.setTextColor('black')
  except:
    input_field.setTextColor('red')
  return prob

def handle_random_start(forest, input_field):
  handle_reset(forest)
  probability = get_probability(input_field)

  if probability is None:
    return

  rand_row = random.randint(0, forest.rows - 1)
  rand_col = random.randint(0, forest.cols - 1)

  forest.tree_grid[rand_row][rand_col].burn()
  forest.burn(probability)

def handle_click_start(forest, input_field, clicked_tree):
  handle_reset(forest)
  probability = get_probability(input_field)

  if not probability or not clicked_tree:
    return

  clicked_tree.burn()
  forest.burn(probability)

def handle_reset(forest):
  forest.is_burning = False
  forest.reset()

def point_in_rect(point, rect):
  x, y = point.getX(), point.getY()
  x1, y1 = rect.getP1().getX(), rect.getP1().getY()
  x2, y2 = rect.getP2().getX(), rect.getP2().getY()

  return x1 <= x <= x2 and y1 <= y <= y2

main()