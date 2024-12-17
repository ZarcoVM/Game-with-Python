
import pygame
 

class Cubo:
  def __init__(self, x, y):
    self.x = y
    self.y = y
    self.ancho = 50
    self.alto = 50
    self.velocidad = 1
    self.color = "red"
    self.rect = pygame.React(self.x, self.y, self.ancho, self.alto)

  def dibujar (self, ventana):
    pygame.draw.rect(ventana, self.color, self.rect) 
