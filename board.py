import pygame
from groundcell import GroundCell
from brickcell import BrickCell
from stonecell import StoneCell
from watercell import WaterCell

# Game constants
CELL_WIDTH = 40
CELL_HEIGHT = 40
NUM_ROWS = 20
NUM_COLS = 20

class Board():
	def __init__(self):
		# grid matrix for the entire map.
		self.grid = [[0]*NUM_COLS for a in range(NUM_ROWS)]
		#cell group
		self.cells = pygame.sprite.Group()
		
	#This method accepts a list of element cordinated (x,y) and type (0,-1,-2)
	#and apply them accordingly
	def set_terrain(self,coords,ttype):
		for xY in coords:
			print xY[0], xY[1], ttype
			self.grid[xY[0]][xY[1]] = ttype
	
	#Instantiate cells
	def draw_board(self):
		
		for i in range(NUM_ROWS):
			for j in range(NUM_COLS):
				if self.grid[i][j] == 0: # normal ground
					cell = GroundCell()
				elif self.grid[i][j] == -1: # breakable brick
					cell = BrickCell()
				elif self.grid[i][j] == "GRID_STONE": # unbreakable stone barrier
					cell = StoneCell()
				elif self.grid[i][j] == "GRID_WATER": # water hole
					cell = WaterCell()
					# pass
				
				#manually assign the x,y cordinates acording to our
				#width and height options
				x = j*CELL_WIDTH
				y = i*CELL_HEIGHT
				#also assign them to a rect, this is a requirement of a Sprite
				cell.rect = pygame.Rect(x,y,CELL_WIDTH,CELL_HEIGHT)

				#finally add it to the group we defined earlier
				self.cells.add(cell)
