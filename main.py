import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Top Down Shooter")


### Variable intialization
bulletRadius = 15
enemyMinSpeed = 2
enemyMaxSpeed = 5
shootSpeed = 30
### Class definitions
class sprite:
  def __init__(self, file, x, y):
    self.sprite = pygame.image.load(file)
    self.y = y
    self.x = x
    self.rect = pygame.Rect((x, y), self.sprite.get_size())
  def blit(self):
    self.rect = pygame.Rect((self.x, self.y), self.sprite.get_size())
    screen.blit(self.sprite, (self.x, self.y))
  def resize(self, w, h):
    self.sprite = pygame.transform.scale(self.sprite, (w, h))
  def rotate(self, deg):
    self.sprite = pygame.transform.rotate(self.sprite, deg)
  def drawHitBox(self):
    pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

class player(sprite):
  def __init__(self, file, x, y):
    sprite.__init__(self, file, x, y)
    self.shooting = False
    
class enemy(sprite):
  def __init__(self, file, x, y, hitpoints, minSpeed, maxSpeed):
    sprite.__init__(self, file, x, y)
    self.isDead = False
  def ranPos(self):
    self.x = random.randint(100, 700)
    self.y = 0
  def move(self, min, max):
    self.y  += random.uniform(min, max)
  def hit(self):
    self.hitpoints -= 1
    if self.hitpoints <= 0:
      self.isDead = True
      self.ranPos()
      print("score: ", self.score)

### Sprite Initalization
spritey_da_sprite = player("sprite.png", 100, 100)      
spritey_da_sprite.resize(90, 85)

background = sprite("background.png", 0, 0)
background.resize(800, 600)
lazer = sprite("bullet.png", 0, 0)
lazer.resize(bulletRadius * 2, bulletRadius * 2)

enemy = enemy('EMEMY.png', 400, 300, hitpoints=1, minSpeed=enemyMinSpeed, \
              maxSpeed=enemyMaxSpeed)
enemy.resize(60, 55)
enemy.ranPos()
speed = 15


while 1:
  pygame.event.get()
  keys = pygame.key.get_pressed()

  ### Key Detection and Movement
  if keys[100]:
    spritey_da_sprite.x = spritey_da_sprite.x + speed
  if keys[97]:
    spritey_da_sprite.x = spritey_da_sprite.x - speed
  if keys[115]:
    spritey_da_sprite.y = spritey_da_sprite.y + speed
  if keys[119]:
    spritey_da_sprite.y = spritey_da_sprite.y - speed
  if keys[pygame.K_q]:
    break
  if keys[pygame.K_SPACE]:
    spritey_da_sprite.shooting = True
    
  ### Lazer
  if spritey_da_sprite.shooting:
    lazer.y -= shootSpeed
  else:
    lazer.x = spritey_da_sprite.x + 66.5
    lazer.y = spritey_da_sprite.y + 5
  if lazer.y < 0:
    spritey_da_sprite.shooting = False

  ### Test
  if lazer.rect.colliderect(enemy.rect):
    print('my nem jef')
  ### Placing sprites and configuring screen
  screen.fill((255, 255, 255))
  background.blit()
  spritey_da_sprite.blit()
  spritey_da_sprite.drawHitBox()
  enemy.blit()
  enemy.drawHitBox()
  lazer.blit()
  lazer.drawHitBox()
  pygame.display.flip()
quit()

