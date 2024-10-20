# Imports para el proyecto
import pygame  # Corrección del import

# pip install pygame


# Inicialización de Pygame
pygame.init()

# Definimos dimensiones de la ventana
ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode([ANCHO, ALTO])
# Título de la ventana (opcional)
pygame.display.set_caption("ZarcoGame with Pygame")

# Ciclo para mantener la ventana abierta
while jugando:
    # Obtener eventos de Pygame
    eventos = pygame.event.get()

    # Procesar eventos
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False  
     # Actualizar pantalla
    pygame.display.update()

    #Salir del pygame
quit ()
