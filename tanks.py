import pygame
from pygame.locals import *
import sys
from board import Board
from socketclient import ServerClient
import SocketServer


pygame.init()
screen = pygame.display.set_mode((800, 800))


#we keep 2 variables to get messages from the server listen thread to
#our main thread
hasUpdate = False
updateData = None

# TCPRequestHandler from Python std library
class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
    	global hasUpdate
    	global updateData
    	try:
        	data = self.request.recv(1024)
        	updateData = data
        	hasUpdate = True
        except:
        	print "Exception at server"
        	

sc = ServerClient(ThreadedTCPRequestHandler)

sc.start_server()

sc.connect_client("127.0.0.1", 6000)

#send the JOIN command
sc.send_message("JOIN#")

#once we are connected,we wait for the initialiation message
while not hasUpdate:
	pass

hasUpdate = False

comps = updateData[:-1].split(":")
print comps

playerNum = int(comps[1][1])

#let's extract the bricks list
brickList = list()
for c in comps[2].split(";"):
    tmp = c.split(",")
    print tmp, "brick"
    brickList.append(( int(tmp[1]), int(tmp[0]) ))

stoneList = list()
for c in comps[3].split(";"):
    tmp = c.split(",")
    print tmp, "stone"
    stoneList.append(( int(tmp[1]), int(tmp[0]) ))

waterList = list()
for c in comps[-1].split(";"):
    tmp = c.split(",")
    print tmp, "water"
    waterList.append(( int(tmp[1]), int(tmp[0]) ))

#now we use this bricks list to generate the bricks on the board

#create a new board instane
board = Board()


board.set_terrain(brickList,-1)
board.set_terrain(stoneList,"GRID_STONE")
board.set_terrain(waterList,"GRID_WATER")


board.draw_board()

board.cells.draw(screen)

while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	
	pygame.display.update()
