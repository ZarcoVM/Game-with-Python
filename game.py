# Imports para el proyecto
import pygame  # Corrección del import

# pip install pygame

# Inicialización de Pygame
pygame.init()
#Comenzamos con el desarrollo
ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode
([ANCHO, ALTO])

jugando = True

#ciclo para que la ventana del juego abra y cierre

while jugando:
  eventos = pygame.event.get()

  for evento in eventos:
    if evento.type == pygame.
    QUIT:
      jugando = false
      
  pygame.display.update()

quit ()
