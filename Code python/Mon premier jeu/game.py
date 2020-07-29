from player import Player
from monster import Monster
import pygame

class Game:

    def __init__(self):
        #générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}
        #génération groupe de monstre
        self.all_monster = pygame.sprite.Group()
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monster.add(monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
