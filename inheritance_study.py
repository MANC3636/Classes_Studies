import sys
import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface((50,50))#can be any size
        self.image.fill((240, 80,90))
        #get a rect
        self.rect=self.image.get_rect()
        self.speedx=0;self.speedy=0
        self.x=x; self.y=y



    def update(self, *args):
        self.speedx = 0
        self.speedy = 0
        keys = pg.key.get_pressed()
        if keys[args[0]]:
            self.speedy = -4
        if keys[args[1]]:
            self.speedy = 1
        if keys[args[2]]:
            self.speedx = -1
        if keys[args[3]]:
            self.speedx = 1
            # processes user input
        self.rect.y += self.speedy
        self.rect.x += self.speedx

class Small_Player(Player): #inheritance
    def __init__(self, x=0, y=0):
        Player.__init__(self, x, y)
        self.image=pg.Surface((30,50))#can be any size
        self.image.fill((20, 180,190))
        #get a rect
        self.rect=self.image.get_rect(center=(100, 40))
        self.speedx=0;self.speedy=0
        self.x=x; self.y=y


#the problem is polymorphism
class Run_Game:
    def __init__(self):
        self.screen=pg.display.set_mode((600,660))
        self.clock=pg.time.Clock()
        self.goliath=Player(100,200)
        self.david=Small_Player()
        self.all_sprites=pg.sprite.Group()#we use sprite.Group b/c it reduces our need for separate blit & update
        self.all_sprites.add(self.goliath)
        self.all_sprites.add(self.david)


    def gaming(self):
        pg.init()
        while True:
            self.clock.tick(20)
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    sys.exit()
            self.screen.fill((1, 4, 89))
            #self.all_sprites.update(pg.K_u, pg.K_d)
            self.david.update(pg.K_w,pg.K_s, pg.K_a, pg.K_d )
            self.goliath.update(pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)

            self.all_sprites.draw(self.screen)

            #self.screen.blit(self.goliath.image, self.goliath.rect )
            #self.screen.blit(self.david.image, self.david.rect)
            pg.display.flip()


game1=Run_Game()
game1.gaming()