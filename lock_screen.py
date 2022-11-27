import pygame, phoneHomeScreen
l=[
    pygame.Rect(200,0,120,120),
    pygame.Rect(340,0,120,120),
    pygame.Rect(482,0,120,120),
    pygame.Rect(200,130,120,120),
    pygame.Rect(340,130,120,120),
    pygame.Rect(482,130,120,120),
    pygame.Rect(200,260,120,120),
    pygame.Rect(340,260,120,120),
    pygame.Rect(482,260,120,120),
    pygame.Rect(340,385,120,120)
    
]
numbers=[1,2,3,4,5,6,7,8,9,0]
def main():
    global input
    SCREEN_HEIGHT=500
    SCREEN_WIDTH=800
    pw='1234'
    input=""
    screen=pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    pygame.display.set_caption("Buttons trail")
    image=pygame.image.load("numbers.png")
    image=pygame.transform.scale(image,(400,SCREEN_HEIGHT))
    image_ok=pygame.image.load("ok image.jpeg")
    image_ok=pygame.transform.scale(image_ok,(120,120))
    image_backspace=pygame.image.load("backspace image.jpeg")
    image_backspace=pygame.transform.scale(image_backspace,(120,120))
    ok_rect=pygame.Rect(482,385,120,120)
    backspace_rect=pygame.Rect(200,385,120,120)
    run=True
    while run:
        screen.fill((202,228,241))
        screen.blit(image,(200,0))
        screen.blit(image_ok,(ok_rect))
        screen.blit(image_backspace,(backspace_rect))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type== pygame.MOUSEBUTTONDOWN:
                for rect in l:
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        input=input+str(numbers[l.index(rect)])
                        
                if backspace_rect.collidepoint(pygame.mouse.get_pos()):
                    input=input[:-1]
                
                if ok_rect.collidepoint(pygame.mouse.get_pos()):
                    if input==pw:
                        phoneHomeScreen.main()
                    else:
                        print("Wrong password")
        pygame.display.update()
if __name__=="__main__":
    main()