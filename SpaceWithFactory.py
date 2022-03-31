import pygame

class jugador:
    def __init__(self, _x, _y, _ancho, _alto, _imagen):
        self.xPos = _x
        self.yPos = _y
        self.ancho = _ancho
        self.alto = _alto
        self.imagen = pygame.image.load(_imagen)
        self.vX =1
        self.vY =1
        
        
        #Metodos de la clase 
        def dibujar(self, pantalla):
            pantalla.blit(self.imagen, (self.xPos, self.yPos))
            
            
        def mover(self):
            self.xPos = self.vX
            self.yPos = self.vY
            
