import csv
import numpy as np

class grid:
  'Documentation'

  def __init__(self, N):
    self.N = N
    self.grid = np.zeros((N,N), dtype=np.int)

  def turn_on(self, i1, j1, i2, j2):
    self.grid[i1:i2+1, j1:j2+1] = 1

  def turn_off(self, i1, j1, i2, j2):
    self.grid[i1:i2+1, j1:j2+1] = 0

  def toggle(self, i1, j1, i2, j2):
    self.grid[i1:i2+1, j1:j2+1] = np.abs(self.grid[i1:i2+1, j1:j2+1] - 1)

  def count_lights_on(self):
    print "Lights lit:", np.sum(self.grid == 1)
  
  def display_grid(self):
    print "Current grid:", self.grid

if __name__ == '__main__':
  # Initialize matrix
  x = grid(1000)

  # Read instructions to arr
  with open('data/day6.txt', 'rb') as f:
    instructions = f.readlines()
  
  # Translate each instruction
  for instruction in instructions:
    coord = [int(s) for s in instruction.replace(',',' ').split() if s.isdigit()]
    if instruction.split(" ")[0] == "toggle":
      x.toggle(coord[0], coord[1], coord[2], coord[3])
    elif instruction.split(" ")[0] + instruction.split(" ")[1] == "turnon":
      x.turn_on(coord[0], coord[1], coord[2], coord[3])
    elif instruction.split(" ")[0] + instruction.split(" ")[1] == "turnoff":
      x.turn_off(coord[0], coord[1], coord[2], coord[3])
    else:
      print "Unknown instruction"
