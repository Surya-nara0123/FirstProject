import pygame as pyg, sys
import socket
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))

width, height = 400, 600
window = pyg.display.set_mode((width, height))
pyg.display.set_caption("Chatsapp")
pyg.font.init()

run = True
textBoxRect = pyg.Rect(20, height-60, width-100, 50)
sendBoxRect = pyg.Rect(textBoxRect.right+10, height-60, 60, 50)
inputText = ''
font = pyg.font.SysFont("Arial Black", 20, False, False)
sendImage = pyg.image.load("SuryaAssets/send-message.png")
sendImage = pyg.transform.scale(sendImage, (30, 25))
while run:
    window.fill((255, 200, 100))
    pyg.draw.rect(window, (255, 255, 255), textBoxRect, 0, 100)
    pyg.draw.rect(window, (100, 255, 100), sendBoxRect, 0, 20)
    window.blit(sendImage, (sendBoxRect.x+15, sendBoxRect.y+14))
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
            s.send("close".encode())
            pyg.quit()
            #sys.exit()

        if event.type == pyg.MOUSEBUTTONDOWN:
            if sendBoxRect.collidepoint(pyg.mouse.get_pos()):
                print("send")
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_BACKSPACE:
                inputText = inputText[:-1]
            else:
                inputText += event.unicode
    window.blit(font.render(inputText, False, (0, 0, 0)), (textBoxRect.x+20, textBoxRect.y+10))
    pyg.display.update()