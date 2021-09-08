import pygame as pygame
import random as random
import datetime as datetime
from pygame import mixer
pygame.font.init()
pygame.mixer.init()

#game verialbles 

width = 900
height = 500
fps= 60
mov= 5
lavel = 1
health_1=100
max_bullet=6
enmy_move= 2
val= enmy_move
enemy_count =[]
wave_enm= 20
bullet_1_dmg= 25
bullet_2_dmg= 50
ship_hight= 70
ship_weidth = 70
bullet_colour=(230,230,250)
white=(255,255,255)




#create windows 
WIN=pygame.display.set_mode((width,height))
pygame.display.set_caption(" space impect game ")


#load ships and background 
background=pygame.image.load("image/back2.jpg")
background_1=pygame.transform.scale(background, (width,height))


ship=pygame.image.load("image/spacex.png")
ship_2=pygame.transform.scale(ship,(ship_weidth,ship_hight))
ship_1=pygame.transform.rotate(ship_2, 270)

eship_1=pygame.transform.scale(pygame.image.load("image/boss.png"),(ship_weidth-40,ship_hight-40))
eship_2=pygame.transform.scale(pygame.image.load("image/ship2.png"),(ship_weidth-40,ship_hight-40))
eship_3=pygame.transform.scale(pygame.image.load("image/ship1.png"),(ship_weidth-40,ship_hight-40))

bullet_1=pygame.transform.scale(pygame.transform.rotate(pygame.image.load("image/bullet.png"),0),(10,10))
bullet_2=pygame.transform.scale(pygame.transform.rotate(pygame.image.load("image/misile.png"),0),(10,10))


#music load
mixer.music.load("music/background.wav")

#playing music under infinity loop 
mixer.music.play(-1)


#create event 
hit_event=pygame.USEREVENT+1
hit_event2=pygame.USEREVENT+2



#font
main_font= pygame.font.SysFont("comicsans", 20)

#game functions 





#ship movement 
def ship_move(key_press,rect_1):
    if key_press[pygame.K_a] and rect_1.x - mov > 0:
        rect_1.x -= mov
    if key_press[pygame.K_d] and rect_1.x +mov < (width/2)-20:
        rect_1.x += mov
    if key_press[pygame.K_w] and rect_1.y > 0:
        rect_1.y-= mov
    if key_press[pygame.K_s] and rect_1.y < 450:
        rect_1.y+= mov



#ship fire 
#ship_fire 


#display update 
def display_update(rect_1,bullet_count,health_1,lavel):
    WIN.blit(background_1,(0,0))
    labe=main_font.render(f"Game level:{lavel}",1,white)
    labe1=main_font.render(f"player health:{health_1}",1,white)
    WIN.blit(labe,(10,10))
    WIN.blit(labe1,(110,10))
    WIN.blit(ship_1,(rect_1.x,rect_1.y))
    for bullet in bullet_count:
        pygame.draw.rect(WIN,bullet_colour,bullet )
    
    for enamy in enemy_count:
        enamy.drow_ship(WIN)
    



    pygame.display.update()

    


def bullet_move(bullet_count):
    for bullets in bullet_count:
        bullets.x+= mov
        if bullets.x > height:
            bullet_count.remove(bullets)

def collision(self,obj1, obj2):
        offset_x= obj2.x - obj1.x
        offset_y= obj2.x - obj1.x
        return obj.mask.overlap(obj2.mask,(offset_x,offset_y)) != None
        

class Laser:
    def __init__(self,x,y,img):
        self.x=x
        self.y=y
        self.img=img
        self.mask=pygame.mask.from_surface(self.img)
    
    def move(self, val):
        self.x -= val*2 
    def draw(self,window):
        window.blit(self.img,(self.x,self.y))

    
    def collide(self,obj):
        return collision(obj, self)


class ship():
    def __init__(self,x,y, health=100):
        self.x=x
        self.y=y
        self.ship_image=None
        self.ship_lz_image=None
        self.lasers=[]
        self.health=health
        self.cool=0
    def cooldown(self):
        if self.cool >= 30:
            self.cool=0
        elif self.cool > 0:
            self.cool+=1

    def shoot(self):
        if self.cool ==0:
            laser=Laser(self.x, self.y,bullet_1)
            self.lasers.append(laser)
            self.cool=1 

    def drow_ship(self,window):
        window.blit(self.ship_image, (self.x, self.y))

    def height(self):
        return self.ship_image.get_height()
    
    def width(self):
        return self.ship_image.get_width()

class Enmy(ship):

    chos_ship = { 
        # "eship_1":(eship_1,bullet_1),
        "eship_2" :(eship_2, bullet_1),
        "eship_3": (eship_3,bullet_2)
                }


    def __init__(self,x,y,type,health=100 ):
        super().__init__(x,y,health)
        self.ship_image , self.ship_lz_image = self.chos_ship[type]

   

    def emove_x(self, val):
        self.x -= val
        # self.y += val

    def emove_y(self, val):
        self.y -= val
            
#enimey fire 
clock = pygame.time.Clock() 

def main():
    bullet_count=[]
    wave_enm =20
    lavel=1
    rect_1=pygame.Rect(0,400 , ship_weidth , ship_hight )
    health_1 =100
    


   
    run = True 
    while run:
        clock.tick(fps)

        if len(enemy_count)==0:
            lavel +=1
            wave_enm +=5
            for i in range(wave_enm):
                enamy= Enmy(width+random.randint(10,4000), random.randint(0,height),random.choice(["eship_2","eship_3"]))
                enemy_count.append(enamy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(bullet_count) <= max_bullet:
                    bullet=pygame.Rect(rect_1.x + rect_1.width, rect_1.y+(rect_1.height//2)-2 , 10,5)
                    bullet_count.append(bullet)



            

        bullet_move(bullet_count)
        key_press=pygame.key.get_pressed()
        ship_move(key_press,rect_1)
        for entry in enemy_count[:]:
            entry.emove_x(val)
            if entry.x <=0 :
                health_1 -= 10
                enemy_count.remove(entry)
                

        display_update(rect_1,bullet_count,health_1,lavel)

main()  


if __name__ == '__main__':
    main()    
    


