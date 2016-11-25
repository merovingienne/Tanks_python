import pygame

#cell size in pixels
CELL_WIDTH = 40
CELL_HEIGHT = 40

class BrickCell(pygame.sprite.Sprite):

	def __init__(self):
		super(BrickCell, self).__init__()

		self.image = pygame.image.load("brick.png").convert()
		self.image = pygame.transform.scale(self.image,(CELL_WIDTH,CELL_HEIGHT))
