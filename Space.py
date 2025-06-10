import pygame
import random
import math
from pygame import mixer

# initialize the pygame
pygame.init()



# display the window

screen = pygame.display.set_mode((800 , 600))

# caption and Icon
pygame.display.set_caption("Space Invaders")
Icon = pygame.image.load('D:\\python\\Games\\rocket.png')
pygame.display.set_icon(Icon)

#background image
background = pygame.image.load("D:\\python\\Games\\space.webp")
 
#background sound 

mixer.music.load('D:\\python\\Games\\background.wav')
mixer.music.play(-1) # works in loop



 
#Player
PlayerImg = pygame.image.load("D:\\python\\Games\\spaceship.png")
ReSized_Image = pygame.transform.scale(PlayerImg , (64 , 64))   
PlayerX = 400
PlayerY = 480
PlayerX_change = 0
PlayerY_change = 0
def player(x , y):
    #blit drawing function
    screen.blit(ReSized_Image , (x , y))

#Enemy
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 6  
for i in range(num_of_enemies):
    EnemyImg.append(pygame.image.load("D:\\python\\Games\\alien.png"))
    EnemyX.append(random.randint(0 , 736))
    EnemyY.append(random.randint(50 , 150))
    EnemyX_change.append(0.3)
    EnemyY_change.append(40)



def Enemy(x , y , i):
    screen.blit(EnemyImg[i] , (x , y))
    
#score
score_value = 0
font = pygame.font.Font("freesansbold.ttf" , 32)
textX = 10
textY = 10
#Game over
over_font = pygame.font.Font("freesansbold.ttf" , 64)

def game_over_text():
    
    game_over = over_font.render("GAME OVER!" , True , (255 , 255 , 255))
    screen.blit(game_over, (200 , 250))
    

def show_score(x , y):
    score = font.render("Score : "+str(score_value) , True , (0 , 255 , 0))
    screen.blit(score , (x , y))
    
#Bullet
bulletImg = pygame.image.load("D:\\python\\Games\\bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"



 
def fire_bullet(x , y):
    global bullet_state
    bullet_state = "fire"
    
    screen.blit(bulletImg , (x + 16 , y + 10))
    
#collision
def iscollision(EnemyX , EnemyY , bulletX , bulletY):
    distance = math.sqrt((math.pow(EnemyX - bulletX , 2)) +(math.pow(EnemyY - bulletY , 2)))
    
    if distance < 27:
        return True
    else:
        return False
    
#Game loop
running = True


while running:
    
    screen.fill((0, 0 , 0))
    
    screen.blit(background , (0 , 0))
     
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_change = -0.7
            if event.key == pygame.K_RIGHT:
                PlayerX_change = 0.7
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('D:\\python\\Games\\Laser.wav')
                    bullet_sound.play()
                    bulletX = PlayerX
                    bulletY = PlayerY
                    fire_bullet(bulletX , bulletY)
                    
        if  event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0
           
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                PlayerY_change = -0.7
            if event.key == pygame.K_DOWN:
                PlayerY_change = 0.7
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletY = PlayerY
                    fire_bullet(bulletX , bulletY)
        if  event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                PlayerY_change = 0
    
    
    
    
    PlayerX += PlayerX_change
    
    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >=736:
        PlayerX = 736
    PlayerY += PlayerY_change  
    
    if PlayerY <= 0:
        PlayerY = 0
    elif PlayerY >= 536:
        PlayerY = 536
    #Enemy movement
    for i in range(num_of_enemies):
        #Game Over
        if EnemyY[i] > 440:
            for j in range(num_of_enemies):
                EnemyY[j] = 2000
            game_over_text()
            break
        
        EnemyX[i] += EnemyX_change[i]
    
        if EnemyX[i] <= 0:
            EnemyX_change[i] = 0.3
            EnemyY[i] += EnemyY_change[i]
        elif EnemyX[i] >= 736:
            EnemyX_change[i] = -0.3
            EnemyY[i] += EnemyY_change[i]
        collision = iscollision(EnemyX[i] , EnemyY[i] , bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('D:\\python\\Games\\explosion.wav')
            explosion_sound.play()
            
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            
            EnemyX[i] = random.randint(0 , 736)
            EnemyY[i] = random.randint(50 , 150)
        Enemy(EnemyX[i] , EnemyY[i] , i)
        
    
    #Bullet movement
    
    if bulletY <= 0:
        bulletY = 480
        bullet_state ="ready"
    
    if bullet_state =="fire":
        fire_bullet(bulletX , bulletY)
        bulletY -= bulletY_change
        
   
    
    
        
    player(PlayerX , PlayerY)  
    show_score(textX , textY)
    pygame.display.update()
    



