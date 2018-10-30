#DimHour2
import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 500
HEIGHT = 680
FPS = 60

#colorfulstuffs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# pygame and windowsan
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DimHour 2: Multi Cloning Catastrophy")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midleft = (x, y)
    surf.blit(text_surface, text_rect)
    
def newgunera():
    g = Gunera()
    all_sprites.add(g)
    guneras.add(g)

def newguneram():
    m = Guneram()
    all_sprites.add(m)
    guneram.add(m)
    
def newunchar():
    u = Unknownchar()
    all_sprites.add(u)
    unchar.add(u)


def draw_resistance_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 15
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, BLACK, outline_rect, 3)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
        



class Scara(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image = pygame.transform.scale(scara_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 12
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.resistance = 100
        self.shoot_delay = 250
        self.last_dimshot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
       

    def update(self):
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.center = (WIDTH / 2, HEIGHT - 10)
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -6
        if keystate[pygame.K_RIGHT]:
            self.speedx = 6
        if keystate[pygame.K_z]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0     
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_dimshot > self.shoot_delay:
            self.last_dimshot = now
            dimshot = Dimshot(self.rect.centerx, self.rect.top)
            all_sprites.add(dimshot)
            dimshots.add(dimshot)
            shot_sound.play()
            
    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)


class Gunera(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,50))
        self.image = gunera_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .80 / 2)
       # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
                          
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-4, 4)
        

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < - 27 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 9)
        
            
class Dimshot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image = pygame.transform.scale(dimshot_img, (25, 19))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Guneram(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image = pygame.transform.scale(guneram_img, (49, 100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 12
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = 100
        self.speedx = 0

    def update(self):
     self.rect.center = (WIDTH / 2, 100)
     self.speedx = 0

class Unknownchar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image = pygame.transform.scale(unchar_img, (350, 260))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = 12
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = 100
        self.speedx = 0

    def update(self):
     self.rect.center = (WIDTH / 2, 100)
     self.speedx = 0

def show_new_scene():
    screen.fill(BLUE)
    pygame.mixer.music.load(path.join(snd_dir, 'Another End To Another Tale.mp3'))
    draw_text(screen, "Thanks for playing DimHour - Multi Cloning Catastrophy", 20, 10, 10)
    draw_text(screen, "Scara - Looks like we Cleared the depths of the interdimension...", 15, 10, 30)
    draw_text(screen, "WeirdoFairy - Miss Scara whats wrong you seem disturbed?", 15, 10, 50)
    draw_text(screen, "Scara - ~I guess she didnt notice that weird thing that showed up~ Its nothing!", 15, 1, 70)
    draw_text(screen, "Scara - Anyway its looks like those annoying clones are gone", 15, 10, 100)
    draw_text(screen, "...", 15, 10, 120)
    draw_text(screen, "Gunera - Ugh my head hurts, what happened? Nevermind im going back...", 15, 10, 140)
    draw_text(screen, "Scara - I guess we'll let her get away but I wonder where she meant to go back to...", 15, 10, 160)
    draw_text(screen, "The end/credits - all art, music, etc was created by me Reimi, of the DimHourProject.", 15, 10, 180)
    pygame.mixer.music.play(loops =- 1)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    

background = pygame.image.load(path.join(img_dir, "DH2background.png")).convert()   
background_rect = background.get_rect()
guneram_img = pygame.image.load(path.join(img_dir, "GuneraM.png")).convert()
guneram_img.set_colorkey(BLACK)
unchar_img = pygame.image.load(path.join(img_dir, "UnknownChar.png")).convert()
unchar_img.set_colorkey(BLACK)
scara_img = pygame.image.load(path.join(img_dir, "Scara.png")).convert()
lives_img = pygame.image.load(path.join(img_dir, "LifeIcon.png")).convert()
lives_img = pygame.transform.scale(lives_img, (25, 25))
lives_img.set_colorkey(WHITE)
gunera_img = pygame.image.load(path.join(img_dir, "GuneraCCC.png")).convert()
dimshot_img = pygame.image.load(path.join(img_dir, "scarashot.png")).convert()
shot_sound = pygame.mixer.Sound(path.join(snd_dir, 'dimshot.wav'))
destroyed_sound = pygame.mixer.Sound(path.join(snd_dir, 'destroyed.wav'))
pygame.mixer.music.load(path.join(snd_dir, 'CloneChaos.wav'))





all_sprites = pygame.sprite.Group()
guneras = pygame.sprite.Group()
dimshots = pygame.sprite.Group()
guneram = pygame.sprite.Group()
unchar = pygame.sprite.Group()
scara = Scara()
all_sprites.add(scara)
for i in range(16):
    newgunera()
for i in range(60):
    newguneram()
GuneraHealth = 60
DimScore = 0


pygame.mixer.music.play(loops =- 1)
    
# Gloop
new_screen = False
running = True
while running:
    
    clock.tick(FPS)
    # event process stuffs
    for event in pygame.event.get():
        # checking window for close cmon man
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                scara.shoot()

    if new_screen:
        show_new_scene()
        new_screen = True
    # Uperdater
    all_sprites.update()
    #Did it hit?

    attacks = pygame.sprite.groupcollide(guneras, dimshots, True, True)
    for attack in attacks:
        DimScore += 1
        destroyed_sound.play()
        newgunera()
        if DimScore >= 500:
            all_sprites.remove(guneras)
        if GuneraHealth == 0 and DimScore >= 500:
            for i in range(30):
                newunchar()
                UncharHealth = 30
                draw_text(screen, str(UncharHealth), 50, 400, 20)

           
            
        
            
    
    attacks = pygame.sprite.groupcollide(guneram, dimshots, True, True)
    for attack in attacks:
        GuneraHealth -= 1
        if GuneraHealth == 0:
            guneram.remove

    attacks = pygame.sprite.groupcollide(unchar, dimshots, True, True)
    for attack in attacks:
        UncharHealth -= 1
        if UncharHealth == 0:
            unchar.remove
            pygame.mixer.music.stop()
            show_new_scene()
        
    #did the gunera hit scara

        
    attacks = pygame.sprite.spritecollide(scara, guneras, True, pygame.sprite.collide_circle)
    for attack in attacks:
        scara.resistance -= attack.radius * 2
        newgunera()
        if scara.resistance <= 0:
            scara.hide()
            scara.lives -= 1
            scara.resistance = 100

        if scara.lives == 0:
            running = False
    

    # D-raw and dude-render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, "Gunera Clones Destroyed:", 18, WIDTH / 8, 10)
    draw_text(screen, str(DimScore), 18, WIDTH / 2, 10)
    draw_text(screen, str(GuneraHealth), 50, 400, 20)
    draw_resistance_bar(screen, 270, 660, scara.resistance)
    draw_lives(screen, WIDTH - 100, 650, scara.lives, lives_img)
    # after drawing flip it... flip the display!!!
    pygame.display.flip()

pygame.quit()

