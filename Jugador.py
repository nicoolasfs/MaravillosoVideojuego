import pygame
from Actor import Actor
class Jugador(Actor):
    def __init__(self,_x, _y, _ancho, _alto, _imagen):
        super().__init__(_x, _y, _ancho, _alto, _imagen)
        
        #movimientos
        
    def moverDerecha(self):
        self.vX += 1
    def moverIzquierda(self):
        self.vX -= 1
    def moverArriba(self):
        self.vY +=1
    def moverAbajo(self):
        self.vY -= 1
        
    