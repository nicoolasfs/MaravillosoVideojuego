import pygame
from Actor import Actor
class Bala(Actor):
    
    def __init__(self,_x, _y, _ancho, _alto, _imagen):
        super().__init__(_x, _y, _ancho, _alto, _imagen)
        
        #metodos de clase