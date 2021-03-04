import pygame as pg

"""Bookmarking code: ctrl/shift/#"""
pg.init()
FPS= 5
#screen = pg.display.set_mode((800, 800))
clock=pg.time.Clock()




class Animated():
    def __init__(self):
        self.x=200
        self.y=100
        #load images into a list
        self.list_of_pics = ["run1.png", "run2.png", "run2.png"]
        self.loaded_pics = [pg.image.load(pic) for pic in self.list_of_pics]
        self.anime_pos=0
        self.image=self.loaded_pics[self.anime_pos]
        self.anime_max=len(self.loaded_pics)-1

    def update(self, screen):
        for x in "limited ranges":
            self.image=self.loaded_pics[self.anime_pos]
            if self.anime_pos==self.anime_max:
                self.anime_pos=0
            else:self.anime_pos+=1
            print(id(self.image))
            screen.blit(self.image, (self.x, self.y))
            pg.display.flip()


#anime=Animated()
#game loop------------------------------------
# yellow_grapes=True
# while yellow_grapes:
#     clock.tick(FPS)
#     last_time_update = 0
#     screen.fill((100,100,100))
#     for event in pg.event.get():
#         if event.type==pg.QUIT:
#             yellow_grapes=False
#         if event.type==pg.KEYDOWN:
#             if event.key==pg.K_LEFT:
#                 pos=1
#
#     #update-----------------------------------
#     pg.display.update()
#     #anime.update()
#     #draw------------------------------------
#
#     pg.display.flip()
# pg.quit()