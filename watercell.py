import pygame

#cell size in pixels
CELL_WIDTH = 40
CELL_HEIGHT = 40

class WaterCell(pygame.sprite.Sprite):

	def __init__(self):
		super(WaterCell, self).__init__()

		self.image = pygame.image.load("water_slot.png").convert()
		self.image = pygame.transform.scale(self.image,(CELL_WIDTH,CELL_HEIGHT))