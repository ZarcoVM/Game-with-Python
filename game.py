# Imports para el proyecto 
import pygame  


# Corrección del import
from personaje import cubo
from enemigo import enemigo
# pip install pygame
# para instalar libreria 






# Inicialización de Pygame
pygame.init()

# Definimos dimensiones de la ventana
ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode([ANCHO, ALTO])

jugando = True

cubo = Cubo(100, 100)

def gestionar_teclas(teclas):
    if teclas[pygame.k_w]:
        cubu.y -= cubo.velocidad
    if teclas[pygame.k_s]:
        cubu.y += cubo.velocidad
    if teclas[pygame.k_a]:
        cubu.x -= cubo.velocidad
    if teclas[pygame.k_d]:
        cubu.x += cubo.velocidad
        
# Título de la ventana (opcional)
pygame.display.set_caption("ZarcoGame with Pygame")

# Ciclo para mantener la ventana abierta
while jugando:
    # Obtener eventos de Pygame
    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed
    ()

    gestionar_teclas(teclas)

    # Procesar eventos
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False  
    VENTANA.fill("black")
    cubo.dibujar(VENTANA)
     # Actualizar pantalla
    pygame.display.update()

    #Salir del pygame
quit ()
