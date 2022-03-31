import pygame

from Jugador import *
from Bala import *
from Base import *
from Enemigo import *
from Actor import *

NEGRO = (0,0,0)

FPS=60
def main():
    pygame.init()
    
    JUGANDO = True
    tam = (800,600)
    pantalla = pygame.display.set_mode(tam)
    pantalla.fill(NEGRO)
    pygame.display.set_caption("Juego")
    
    jugadorIMG= "assets\ship.png"
    enemigoIMG= "assets/bot.png"
    balaIMG = "assets/bullet.png"
    muroIMG = "assets/muro.png"
    
    jugador = Jugador(400,500, 49,45,jugadorIMG)
    enemigo = Enemigo(400,200,49,49, enemigoIMG)
    bala = Bala(400,750,8,16,balaIMG)
    base = Base(400, 600, 50,20, muroIMG)
    jugador.dibujar(pantalla)
    
    
    while JUGANDO:
    
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_LEFT]: 
            print("izquierda")# flecha izquierda
            jugador.moverIzquierda() # borde del área izquierda
        elif tecla[pygame.K_RIGHT]: 
            print("derecha")# flecha derecha
            jugador.moverIzquierda() # borde del área derecha
        elif tecla[pygame.K_UP]:  # flecha derecha
            jugador.moverArriba()
        elif tecla[pygame.K_DOWN]:  # flecha derecha
            jugador.moverAbajo()    
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ACTIVO = False

    
            # actualizar pantalla
        pygame.display.update()
        jugador.actualizar(pantalla)
    
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)
    
    
    
if __name__ == "__main__":
    main()
