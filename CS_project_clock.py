import pygame
import math
from datetime import datetime
pygame.font.init()






def rotateclockhand(clock_dict , clock_hand,key, In_WIDTH, In_Height, radius_list):
    x=In_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi/2)
    y=In_Height + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi/2) 
    return x, y 

font=pygame.font.SysFont("Arial",60)

def drawclock(SURFACE, WIDTH, HEIGHT):
    clock12=dict(zip(range(12) , range(0,360,30))) 
    clock60=dict(zip(range(60) ,range(0,360,6)))
    In_WIDTH , In_Height= WIDTH//2 , HEIGHT//4
    RADIUS = 100
    radius_list={"sec":RADIUS-10,"min":RADIUS-55,"hour":RADIUS-100,"digit":RADIUS-30}
    """Extracting time"""
    t=datetime.now()
    hour , minute , second=((t.hour%12)*5 + t.minute//12)%60 , t.minute , t.second
    pygame.draw.circle(SURFACE,pygame.Color('WHITE') , (In_WIDTH, In_Height), RADIUS )
    for digit, pos in clock60.items():
        radius=20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2 
        pygame.draw.circle(SURFACE, pygame.Color("Black"), rotateclockhand(clock60, digit, "digit", In_WIDTH, In_Height, radius_list),radius,5)
    pygame.draw.line(SURFACE, pygame.Color('Black'), (In_WIDTH, In_Height), rotateclockhand(clock60, hour,"hour", In_WIDTH, In_Height, radius_list), 15)
    pygame.draw.line(SURFACE, pygame.Color('green'), (In_WIDTH, In_Height), rotateclockhand(clock60, minute,"min", In_WIDTH, In_Height, radius_list), 10)
    pygame.draw.line(SURFACE, pygame.Color('Blue'), (In_WIDTH, In_Height), rotateclockhand(clock60, second,'sec', In_WIDTH, In_Height, radius_list), 10)
    time_render= font.render(f'{t:%H:%M:%S}', True , pygame.Color('forestgreen') , pygame.Color('orange'))
    SURFACE.blit(time_render,(0 , 0))



def main():
    global clock12, clock60, In_WIDTH, In_Height, radius_list, RADIUS
    RES=WIDTH,HEIGHT=1200,800

    pygame.init()
    SURFACE=pygame.display.set_mode(RES)
    clock=pygame.time.Clock()

    clock12=dict(zip(range(12) , range(0,360,30))) 
    clock60=dict(zip(range(60) ,range(0,360,6)))

    In_WIDTH , In_Height= WIDTH//2 , HEIGHT//2
    RADIUS = 125
    radius_list={"sec":RADIUS-10,"min":RADIUS-55,"hour":RADIUS-100,"digit":RADIUS-30}
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        drawclock(SURFACE,WIDTH,HEIGHT)
        pygame.display.update
        pygame.display.flip()
    pygame.quit()
    clock.tick(60)



if __name__ == "__main__":
    main()
