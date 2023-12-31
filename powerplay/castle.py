import pygame

from constants import Image_Maps

class Castle:
    def __init__(self, game, health):
        
        self.constants = game.constants
        self.window = game.window
        self.clock = game.clock

        self.item_color = Image_Maps.CASTLE_MAP[0]
        self.item_img = Image_Maps.CASTLE_MAP[1]

        self.health = health
        self.x = self.constants.CASTLE_X
        self.y = self.constants.CASTLE_Y

        self.cooldown = 300
        self.last = -300
        self.now = 0
    
    def hurt(self, dmg):
        self.health -= dmg
        self.last = self.now
    
    def get_hp(self): return self.health

    def draw(self):
        self.now += self.clock.get_time()
        if ((self.now - self.last) < self.cooldown):
            self.item_color = Image_Maps.HURT_CASTLE_MAP[0]
        else:
            self.item_color = Image_Maps.CASTLE_MAP[0]
        if(self.health > 0):
            idy = self.y - 50
            for y in range(len(self.item_img[1])):
                idx = self.x - 50
                for x in range(len(self.item_img[1])):
                    if self.item_img[y][x] > 0:
                        pygame.draw.rect(
                            self.window, self.item_color[self.item_img[y][x] - 1], pygame.Rect(
                                idx, idy, self.constants.ITEM_TILE_WIDTH, self.constants.ITEM_TILE_WIDTH
                            ))
                    idx += self.constants.ITEM_TILE_WIDTH
                idy += self.constants.ITEM_TILE_WIDTH