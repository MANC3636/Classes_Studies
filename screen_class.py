import pygame as pg
import sys
from animation_basic1 import Animated
#------------------values-------------------------------------
dict_screen={"WIDTH": 500, "HEIGHT":500}

FPS=20
clock=pg.time.Clock()
pg.font.init()
px_font=pg.font.SysFont("arial", 15)
text="pie:            $2.50"
text1="half-sandwich: $4.50"
customer_list=[]

class Textbox:
    def __init__(self, x, y, text):
        self.font=pg.font.Font('freesansbold.ttf',20)
        self.x=x; self.y=y
        self.text=text

    def text_surface_func(self, color:"a tuple of three ints", background:"usually black"=(0,0,0)):
        #text surfaces for menu items
        self.text_surface=self.font.render(self.text, True, color, background)
        return self.text_surface, self.text_surface.get_rect(center=(self.x,self.y))

def show_start_screen(text):
    pg.init()
    anime=Animated()
    start_screen=pg.display.set_mode((500,500))
    start_screen.fill((250,0,250))
    box1=Textbox(dict_screen["WIDTH"] / 3, dict_screen["HEIGHT"] / 3, text)
    func=box1.text_surface_func((23,78,99))
    font=pg.font.SysFont("arial", 20)
    text_surf=font.render(text, True, (100,100,100))
    #start_screen.blit(func[0], func[1])
    waiting =True
    while waiting:
        clock.tick(FPS)
        start_screen.blit(text_surf, (100,100))
        if text=="bye":
            anime.update(start_screen)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYUP:
                waiting = False
                print("working")



# class Animated:
#     def __init__(self):
#         self.x=100
#         self.y=100
#         #load images into a list
#         self.list_of_pics = ["run1.png", "run2.png", "run2.png"]
#         self.loaded_pics = [pg.image.load(pic) for pic in self.list_of_pics]
#         self.anime_pos=0
#         self.image=self.loaded_pics[self.anime_pos]
#         self.anime_max=len(self.loaded_pics)-1
#
#     def update(self, screen):
#
#             self.image=self.loaded_pics[self.anime_pos]
#             if self.anime_pos==self.anime_max:
#                 self.anime_pos=0
#             else:self.anime_pos+=1
#             print(id(self.image))
#             screen.blit(self.image, (self.x, self.y))
#             pg.display.flip()



class Game:
    def __init__(self):
        pg.init()
        #self.clock=pg.time.Clock()
        self.running_man=Animated()
        self.screen = pg.display.set_mode((dict_screen["WIDTH"], dict_screen["HEIGHT"]))
        self.text_box_250 = Textbox(20, 50, "2.50")
        self.text_box_450 = Textbox(20, 70, "4.50")

        self.text_surface250, self.text_rect250 = self.text_box_250.text_surface_func((100, 100, 100))
        self.text_surface450, self.text_rect450 = self.text_box_450.text_surface_func((100, 100, 100))

        self.price_surface = px_font.render("$2.50", True, (55, 30, 99), (0, 0, 0))
        self.price_surface2 = px_font.render("$4.50", True, (55, 30, 99), (0, 0, 0))
    def run_game(self):
        running =True

        while running:
            clock.tick(FPS)
            mouse_loc = pg.mouse.get_pos()
            collision1 = pg.Rect.collidepoint(self.text_rect250, (mouse_loc[0], mouse_loc[1]))
            collision2 = pg.Rect.collidepoint(self.text_rect450, (mouse_loc[0], mouse_loc[1]))
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    show_start_screen("Bye")
                    sys.exit()
                if event.type==pg.MOUSEBUTTONDOWN:
                    if collision1 == True and pg.mouse.get_pressed():
                        self.screen.blit(self.price_surface, (dict_screen["WIDTH"] - 50, 55))
                        customer_list.append(2.50)
                    if collision2==True and pg.mouse.get_pressed():
                        self.screen.blit(self.price_surface2, (dict_screen["WIDTH"]-50, 75))
                        customer_list.append(4.50)
            #draw
            self.screen.fill((100,100,199))

            self.screen.blit(self.text_surface250, self.text_rect250)
            self.screen.blit(self.text_surface450, self.text_rect450)

            price_sum=sum(customer_list)
            if price_sum>10:
                # self.running_man.update(self.screen)
                # pg.time.delay(1000)
                show_start_screen("bye")
            price_sum_surface=px_font.render(str(price_sum), True, (255, 100, 100))

            self.screen.blit(price_sum_surface, (dict_screen["WIDTH"]-50, 100))

            #prep to redraw
            pg.display.flip()

g=Game()
show_start_screen("starting")
g.run_game()

