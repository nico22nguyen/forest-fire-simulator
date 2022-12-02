from graphics import *

IMAGES = ['images/0_tree.png', 'images/1_little_burn.png', 'images/2_lot_burn.png', 'images/3_charcoal.png']
class Tree:
  def __init__(self, x, y, win):
    self.location = Point(x, y)
    self.win = win
    self.burn_severity = 0
      
  def draw_self(self):
    self.Image = Image(self.location, IMAGES[0])
    self.Image.draw(self.win)

  def burn(self):
    if self.burn_severity >= 3:
      return
    self.burn_severity += 1
    self.Image.undraw()
    self.Image = Image(self.location, IMAGES[self.burn_severity])
    self.Image.draw(self.win)

  def reset(self):
    if self.burn_severity == 0:
      return
    self.burn_severity = 0
    self.Image.undraw()
    self.Image = Image(self.location, IMAGES[self.burn_severity])
    self.Image.draw(self.win)
