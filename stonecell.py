import pygame

#cell size in pixels
CELL_WIDTH = 40
CELL_HEIGHT = 40

class StoneCell(pygame.sprite.Sprite):

	def __init__(self):
		super(StoneCell, self).__init__()

		self.image = pygame.image.load("stone_slot.jpg").convert()
		self.image = pygame.transform.scale(self.image,(CELL_WIDTH,CELL_HEIGHT))
