import pygame
import datetime
import math

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# initialize pygame
pygame.init()
screen_size = (500, 500)
myfont = pygame.font.SysFont('Comic Sans MS', int(min(screen_size)/7))

# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")

# clock is used to set a max fps
clock = pygame.time.Clock()

dps = 1/2
hour_pointer_length = dps * 1/2
minute_pointer_length = dps * 4/5
second_pointer_length = dps

# create a demo surface, and draw a red line diagonally across it
surface_size = (25, 45)
main_surf = pygame.Surface(surface_size)
main_surf.fill(WHITE)
DIGITAL = 0
ANALOG = 1
mode = ANALOG
JUMP = 0
CONTINOUS = 1
analog_mode = JUMP
running = True
while running:+
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                mode = DIGITAL
                screen_size = (500,300)
                pygame.display.set_mode(screen_size)
            if event.key == pygame.K_a:
                mode = ANALOG
                screen_size = (500,500)
                pygame.display.set_mode(screen_size)
            if event.key == pygame.K_p and mode == ANALOG:
                if analog_mode == JUMP:
                    analog_mode = CONTINOUS
                else:
                    analog_mode = JUMP

    # clear the screen
    screen.fill(WHITE)

    # draw to the screen
    # YOUR CODE HERE

    x = int(screen_size[0] / 2)
    y = int(screen_size[1] / 2)
    width = screen_size[0]
    height = screen_size[1]
    center = (x,y)
    scale_factor = min(screen_size)
    if mode == ANALOG:
        pygame.draw.circle(screen, (170,170,50), center, int(scale_factor/2*1.01))
        pygame.draw.circle(screen, BLACK, center, int(scale_factor/2*0.96))
        for x in range(60):

            if x%60 == 0:
                l = 1 / 8
            elif x % 5 == 0:
                l = 1 / 16
            else:
                l = 1 / 32
            pygame.draw.line(screen, (255,255,0),
            (center[0] + math.sin(x/60*math.pi*2) * scale_factor * (1-l) * dps,
            center[1] - math.cos(x/60*math.pi*2) * scale_factor * (1-l) * dps)
            ,
            (center[0] + math.sin(x/60*math.pi*2) * scale_factor * dps,
            center[1] - math.cos(x/60*math.pi*2) * scale_factor * dps),4)
        current_time = datetime.datetime.now()

        hour =current_time.hour+(current_time.minute/60+current_time.second/3600 if analog_mode == CONTINOUS else 0)
        minute = current_time.minute+(current_time.second/60 if analog_mode == CONTINOUS else 0)
        second = current_time.second+(current_time.microsecond/1000000 if analog_mode == CONTINOUS else 0)
        hour_prog = hour%12/6
        minute_prog = minute/30
        second_prog = second/30
        hour_deg = hour_prog*math.pi
        minute_deg = minute_prog*math.pi
        second_deg = second_prog*math.pi

        pygame.draw.line(screen,(50,255,0),center,((center[0]+math.sin(hour_deg)*scale_factor*hour_pointer_length), (center[1]-math.cos(hour_deg)*scale_factor*hour_pointer_length)))
        pygame.draw.line(screen,(255,0,0),center,((center[0]+math.sin(second_deg)*scale_factor*second_pointer_length), (center[1]-math.cos(second_deg)*scale_factor*second_pointer_length)))
        pygame.draw.line(screen,(255,200,0),center,((center[0]+math.sin(minute_deg)*scale_factor*minute_pointer_length), (center[1]-math.cos(minute_deg)*scale_factor*minute_pointer_length)))

        pygame.draw.circle(screen,(170,170,50),center,int(scale_factor/2*0.03))
    elif mode == DIGITAL:
        woff = width/30
        hoff = height / 30

        pygame.draw.rect(screen,(50,30,50),(0,0,width,height))
        pygame.draw.rect(screen,(250,160,50),(woff,hoff,width-woff*2,height-hoff*2))
        pygame.draw.rect(screen,(69,160,50),(woff*2,hoff*2,width-woff*4,height-hoff*4))
        textsurf = myfont.render(datetime.datetime.now().strftime("%H : %M : %S"), False, (250, 0, 0))

        centered_rect = textsurf.get_rect(center=(width//2,height//2)) # https://stackoverflow.com/questions/23982907/python-library-pygame-centering-text#39580531
        screen.blit(textsurf, centered_rect)
        current_time = datetime.datetime.now()
        hour = current_time.hour
        minute = current_time.minute
        second = current_time.second
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
    # how many updates per second
    clock.tick(60)

pygame.quit()