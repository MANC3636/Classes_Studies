import sys
import pygame as pg

HEIGHT=800;WIDTH=800

class Player:
    def __init__(self, x, y):
        self.image=pg.Surface((50,50))
        self.image.fill((255,33,2))
        self.image_rect=self.image.get_rect(center=(600,500))

        self.speedy = 0  #
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.speedx = 0
        self.speedy = 0

        #collects user input
        keys=pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.speedy=-1
        if keys[pg.K_DOWN]:
            self.speedy=1
        if keys[pg.K_LEFT]:
            self.speedx=-1
        if keys[pg.K_RIGHT]:
            self.speedx=1
        #processes user input
        self.image_rect.y+=self.speedy
        self.image_rect.x+=self.speedx

class Sound:
    def __init__(self, wav_music):
        self.music_attribute=wav_music
        self.clock=pg.time.Clock()

    def play_music(self):
        #import pygame; pygame.init()
        pg.mixer.init()
        pg.mixer.music.load(self.music_attribute)
        #pg.mixer.music.set_volume(0.8)
        pg.mixer.music.play(-1)
        while pg.mixer.music.get_busy():
            self.clock.tick(10)

class Run_Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.player=Player(500,400)#"has a" relationship
        self.sound=Sound("opera1.mp3")


    def gaming(self):
        pg.init()
        #self.sound.play_music()

        while True:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    sys.exit()
            self.screen.fill((77, 120, 250))
            self.screen.blit(self.player.image,self.player.image_rect)
            self.player.update()
            print(self.player.image_rect.x)
            if self.player.image_rect.x <=100:
                self.player.image_rect.y+=-1;self.player.image_rect.x+=-1
                self.player.image=pg.transform.scale(self.player.image, (100,10))
            pg.display.flip()

game=Run_Game()
game.gaming()