import pygame as pg
import sys

pg.init()
#------------------values-------------------------------------
dict_screen={"WIDTH": 500, "HEIGHT":500}

screen=pg.display.set_mode((dict_screen["WIDTH"], dict_screen["HEIGHT"]))
px_font=pg.font.SysFont("arial", 15)
text="pie:            $2.50"
text1="half-sandwich: $4.50"
customer_list=[]

class Textbox:
    def __init__(self, x, y, text):
        self.font=pg.font.Font('freesansbold.ttf',20)
        self.x=x; self.y=y
        self.text=text

    def text_surface(self, color:"a tuple of three ints", background:"usually black"=(0,0,0)):
    #text surfaces for menu items
        self.text_surface=self.font.render(self.text, True, color, background)
        return self.text_surface, self.text_surface.get_rect(center=(self.x,self.y))
    def blit_text(self):
        self.text_surface, self.text_surf_rect=self.text_surface()
        screen.blit(self.text_surface, self.text_surf_rect)

text_box_250=Textbox(20, 50, "2.50")
text_box_450=Textbox(20, 70, "4.50")
text_surface250, text_rect250=text_box_250.text_surface((100,100,100))
text_surface450, text_rect450=text_box_450.text_surface((100,100,100))

price_surface = px_font.render("$2.50", True, (55, 30, 99), (0, 0, 0))
price_surface2 = px_font.render("$4.50", True, (55, 30, 99), (0, 0, 0))
running =True
while running:
    mouse_loc = pg.mouse.get_pos()
    collision1 = pg.Rect.collidepoint(text_rect250, (mouse_loc[0], mouse_loc[1]))
    collision2 = pg.Rect.collidepoint(text_rect450, (mouse_loc[0], mouse_loc[1]))
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
        if event.type==pg.MOUSEBUTTONDOWN:
            if collision1 == True and pg.mouse.get_pressed():
                screen.blit(price_surface, (dict_screen["WIDTH"] - 50, 55))
                customer_list.append(2.50)
            if collision2==True and pg.mouse.get_pressed():
                screen.blit(price_surface2, (dict_screen["WIDTH"]-50, 75))
                customer_list.append(4.50)
    #draw
    screen.fill((100,100,199))

    screen.blit(text_surface250, text_rect250)
    screen.blit(text_surface450, text_rect450)

    price_sum=sum(customer_list)
    price_sum_surface=px_font.render(str(price_sum), True, (255, 100, 100))

    screen.blit(price_sum_surface, (dict_screen["WIDTH"]-50, 100))

    #prep to redraw
    pg.display.flip()