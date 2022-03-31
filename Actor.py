import pygame

class Actor:
    def __init__(self,_x, _y, _ancho, _alto, _imagen):
        self.xPos = _x
        self.yPos = _y
        self.ancho = _ancho
        self.alto = _alto
        self.imagen = pygame.image.load(_imagen)
        self.vX =0
        self.vY =0
        #Metodos de la clase 
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, [self.xPos, self.yPos])
            
    
    def definirPantalla(self, ancho,alto):
        self.anchoPantalla =ancho
        self.altoPantalla =alto
    
    def mover(self):
        self.xPos = self.vX
        self.yPos = self.vY
        
    def colision(self, personaje,pantalla):
            #Averiguar si hay colisión por el lado izquierdo del jugador
        if self.xPos < (personaje.xPos + personaje.ancho):
            return True
            #Averiguar si hay colisión por el lado derecho del jugador
        if (self.xPos + self.ancho) > personaje.xPos:
            return True
            #Averiguar si hay colisión por el lado de arriba del jugador
        if (self.yPos- self.alto) < personaje.yPos:
            return True
            #Averiguar si hay colisión por el lado inferior del jugador
        if self.yPos > (personaje.yPos - personaje.alto): 
            return True
            
        return False    

    def limites(self):
        if self.xPos < 0:
            self.xPos = 800
        if self.xPos > 800:
            self.xPos = 0
    def actualizar(self,pantalla):
        self.mover()
        self.limites()
        self.dibujar(pantalla)