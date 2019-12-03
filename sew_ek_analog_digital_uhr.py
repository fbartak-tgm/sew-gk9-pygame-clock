import pygame
import datetime
import math
from time_manager import TimeManager
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# initialize pygame
pygame.init()

# create a window
pygame.display.set_caption("Pygame clock")


dps = 1/2
hour_pointer_length = dps * 1/2
minute_pointer_length = dps * 4/5
second_pointer_length = dps

# create a demo surface, and draw a red line diagonally across it
surface_size = (25, 45)
main_surf = pygame.Surface(surface_size)
main_surf.fill(WHITE)

class Clock(object):
    DIGITAL = 0
    ANALOG = 1
    mode = ANALOG
    screen_size = (500, 500)
    myfont = pygame.font.SysFont('Comic Sans MS', int(min(screen_size)/7))
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    running = True

    def __init__(self):
        self.time_manager = TimeManager()

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)

            # clear the screen
            self.screen.fill(WHITE)

            self.x = int(self.screen_size[0] / 2)
            self.y = int(self.screen_size[1] / 2)
            self.width = self.screen_size[0]
            self.height = self.screen_size[1]
            self.center = (self.x,self.y)
            scale_factor = min(self.screen_size)
            if self.mode == self.ANALOG:
                pygame.draw.circle(self.screen, (170,170,50), self.center, int(scale_factor/2*1.01))
                pygame.draw.circle(self.screen, BLACK, self.center, int(scale_factor/2*0.96))
                for x in range(60):
                    if x%60 == 0:
                        l = 1 / 8
                    elif x % 5 == 0:
                        l = 1 / 16
                    else:
                        l = 1 / 32
                    pygame.draw.line(self.screen, (255,255,0),
                    (self.center[0] + math.sin(x/60*math.pi*2) * scale_factor * (1-l) * dps,
                    self.center[1] - math.cos(x/60*math.pi*2) * scale_factor * (1-l) * dps)
                    ,
                    (self.center[0] + math.sin(x/60*math.pi*2) * scale_factor * dps,
                    self.center[1] - math.cos(x/60*math.pi*2) * scale_factor * dps),4)
                current_time = datetime.datetime.now()


                hour_deg, minute_deg, second_deg = self.time_manager.get_arm_rotations_for_clock()

                pygame.draw.line(self.screen,(50,255,0),self.center,((self.center[0]+math.sin(hour_deg)*scale_factor*hour_pointer_length), (self.center[1]-math.cos(hour_deg)*scale_factor*hour_pointer_length)))
                pygame.draw.line(self.screen,(255,0,0),self.center,((self.center[0]+math.sin(second_deg)*scale_factor*second_pointer_length), (self.center[1]-math.cos(second_deg)*scale_factor*second_pointer_length)))
                pygame.draw.line(self.screen,(255,200,0),self.center,((self.center[0]+math.sin(minute_deg)*scale_factor*minute_pointer_length), (self.center[1]-math.cos(minute_deg)*scale_factor*minute_pointer_length)))

                pygame.draw.circle(self.screen,(170,170,50),self.center,int(scale_factor/2*0.03))
            elif self.mode == self.DIGITAL:
                woff = self.width/30
                hoff = self.height / 30

                pygame.draw.rect(self.screen,(50,30,50),(0,0,self.width,self.height))
                pygame.draw.rect(self.screen,(250,160,50),(woff,hoff,self.width-woff*2,self.height-hoff*2))
                pygame.draw.rect(self.screen,(69,160,50),(woff*2,hoff*2,self.width-woff*4,self.height-hoff*4))
                textsurf = self.myfont.render(str(self.time_manager), False, (250, 0, 0))

                centered_rect = textsurf.get_rect(center=(self.width//2,self.height//2)) # https://stackoverflow.com/questions/23982907/python-library-pygame-centering-text#39580531
                self.screen.blit(textsurf, centered_rect)
            # flip() updates the screen to make our changes visible
            pygame.display.flip()
            # how many updates per second
            self.clock.tick(60)
        pygame.quit()

    def rotate_point_to_position(self,point_to_rotate_around,rot,arm_length):
        return ((point_to_rotate_around[0] + math.sin(rot) * arm_length),
         (point_to_rotate_around[1] - math.cos(rot) * arm_length))

    def handle_event(self,event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.mode = self.DIGITAL
                self.screen_size = (500,300)
                pygame.display.set_mode(self.screen_size)
            if event.key == pygame.K_a:
                self.mode = self.ANALOG
                self.screen_size = (500,500)
                pygame.display.set_mode(self.screen_size)
            if event.key == pygame.K_p and self.mode == self.ANALOG:
                self.time_manager.toggle_continuous_mode()

c = Clock()
c.run_game()