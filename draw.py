from graphics import *

def init_inputs(win):
  X_COORD_LABEL = 825
  Y_COORD_LABEL = 200
  BUTTON_OFFSET = 5

  text = Text(Point(X_COORD_LABEL, Y_COORD_LABEL), 'Burn Probability:')
  text.setSize(18)

  input_field = Entry(Point(X_COORD_LABEL, Y_COORD_LABEL + 30), 20)
  input_field.setSize(16)

  button1 = render_button(win, X_COORD_LABEL, Y_COORD_LABEL + 55, 'Run (Random Start)')
  button2 = render_button(win, X_COORD_LABEL, Y_COORD_LABEL + 55 + 35 + BUTTON_OFFSET, 'Run (Click to Start)')
  button3 = render_button(win, X_COORD_LABEL, Y_COORD_LABEL + 55 + 2 * (35 + BUTTON_OFFSET), 'Reset Simulation')

  text.draw(win)
  input_field.draw(win)

  return input_field, [button1, button2, button3]
  
def render_button(win, x, y, text):
  WIDTH = 150
  HEIGHT = 35
  FONT_SIZE = 14
  COLOR = 'bisque'

  button = Rectangle(Point(x - WIDTH / 2 , y), Point(x + WIDTH / 2, y + HEIGHT))
  button.setFill(COLOR)

  button_text = Text(Point(x, (2*y + HEIGHT) / 2), text)
  button_text.setSize(FONT_SIZE)
  
  button.draw(win)
  button_text.draw(win)
  return button

def render_quit_button(win):
  SIZE = 24
  FONT_SIZE = 18
  COLOR = 'red'

  button = Rectangle(Point(win.getWidth() - SIZE, 0), Point(win.getWidth(), SIZE))
  button.setFill(COLOR)

  button_text = Text(Point(win.getWidth() - SIZE / 2, SIZE / 2), 'X')
  button_text.setSize(FONT_SIZE)
  
  button.draw(win)
  button_text.draw(win)
  return button