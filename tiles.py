import pyxel
from constants import *
from random import randint

class Tile:
    def __init__(self, x, y, u, v, name):
        self.sprite_coord = [u, v, TL, TL]
        self.coord = [x, y]
        self.x, self.y = x, y
        self.w, self.h = TL, TL
        self.hitbox = [0, 0, self.w, self.h]
        self.name = name
        self.solid = 0 # By default tiles won't collide with the character
    def draw(self):
        pyxel.blt(*self.coord, 0, *self.sprite_coord, COL_KEY)

