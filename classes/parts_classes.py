class Part:
  def __init__(self, name, width, height, depth, weight):
    self.name = name
    self.width = width
    self.height = height
    self.depth = depth
    self.weight = weight

  def volume(self):
    volume = self.width * self.height * self.depth
    return volume

class Wheel(Part):
  pass