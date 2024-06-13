import pygame, sys, os, random, math
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

#colors
WHITE = (255, 255, 255) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

#globals
WIDTH = 800
HEIGHT = 600
time = 0

#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Asteroids")


#load images
bg = pygame.image.load(bs.path.join('images', 'bg.jpg'))
debris = pygame.image.load(os.path.join('images', 'debris2_brown.png'))



# asteroids game loop 
while True:
  draw(window)
  handle_input()
  
  #game logic
  update_screen()