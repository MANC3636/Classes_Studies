import pygame as pg
import sys
import scratch_15
WIDTH=500; HEIGHT=500
pg.init()
screen=pg.display.set_mode((WIDTH, HEIGHT))

text="pie:            $2.50"
text1="half-sandwich: $4.50"
customer_list=[]#start with an empty list
font=pg.font.Font('freesansbold.ttf',20)

#text surfaces for menu items
text_surface=font.render(text, True, (55, 2, 222), (0,0,0))
text_surface1=font.render(text1, True, (55, 199, 22), (0,0,0))

#text rects for menu text surfaces
text_rect=text_surface.get_rect(center =(100, 100))
text_rect1=text_surface1.get_rect(center=(100, 130))

#prices
price_surface = font.render("$2.50", True,
                            (55, 30, 99), (0, 0, 0))
price_surface2 = font.render("$4.50", True,
                             (55, 30, 99), (0, 0, 0))

running =True
scratch_15.show_start_screen("start")
while running:
    mouse_loc = pg.mouse.get_pos()
    collision1 = pg.Rect.collidepoint(text_rect, mouse_loc)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
        if event.type==pg.MOUSEBUTTONDOWN:
            if collision1 == True and pg.mouse.get_pressed():
                screen.blit(price_surface, (WIDTH - 50, 55))
                customer_list.append(2.50)

            if collision2==True and pg.mouse.get_pressed():
                screen.blit(price_surface2, (WIDTH-50, 75))
                customer_list.append(4.50)

    collision2 = pg.Rect.collidepoint(text_rect1, mouse_loc)
    #draw
    screen.fill((100,100,199))
    screen.blit(text_surface, text_rect)
    screen.blit(text_surface1, text_rect1)

    price_sum=sum(customer_list)
    price_sum_surface=font.render(str(price_sum), True, (255, 100, 100))
    screen.blit(price_sum_surface, (WIDTH-100, 450))

    #prep to redraw
    pg.display.flip()

