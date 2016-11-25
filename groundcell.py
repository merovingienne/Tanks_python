import pygame

#these are the sie of a cell in pixels
CELL_WIDTH = 40
CELL_HEIGHT = 40

#we make a GroundCell class by extending the Sprite class
#much OOP
class GroundCell(pygame.sprite.Sprite):
	#this is how we write constructors in python
	def __init__(self):
		#IMPORTANT: that you call the super class constructor first
		super(GroundCell, self).__init__()
		#here use any texture you like for ground.png
		self.image = pygame.image.load("ground.jpg").convert()
		#once we load the image we scale is to suit the cell sie as we define
		self.image = pygame.transform.scale(self.image,(CELL_WIDTH,CELL_HEIGHT))
