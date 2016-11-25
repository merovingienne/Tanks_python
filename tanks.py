import pygame
from pygame.locals import *
import sys
from board import Board
from socketclient import ServerClient
import SocketServer


pygame.init()
screen = pygame.display.set_mode((400, 400))


#we keep 2 variables to get messages from the server listen thread to
#our main thread
hasUpdate = False
updateData = None

#This class is a request handler
#It has the handle method that fires when we recieve something from game server
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
        	
#Make new instance of the serverclient class
sc = ServerClient(ThreadedTCPRequestHandler)
#start our listening server on port 7000
sc.start_server()
#connect to the game server, remember to replace the IP with 127.0.0.1
#if you are using the same machine
sc.connect_client("127.0.0.1", 6000)
#send the JOIN command
sc.send_message("JOIN#")

#once we are connected,we wait for the initialiation message
while not hasUpdate:
	pass

hasUpdate = False
#now we has a message, should be the init message
#first split by : to get components
comps = updateData[:-1].split(":")
print comps
#second component of the message gives our player number
playerNum = int(comps[1][1])

#let's extract the bricks list
brickList = list()
for c in comps[2].split(";"):
	tmp = c.split(",")
	brickList.append(( int(tmp[1]), int(tmp[0]) ))

#now we use this bricks list to generate the bricks on the board

#create a new board instane
board = Board()

#see how our set_terrain method is useful
board.set_terrain(brickList,-1)

board.draw_board()

board.cells.draw(screen)

while 1:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	
	pygame.display.update()
