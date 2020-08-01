from monster import Monster
import random
import pygame

class Alien(Monster):

    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.image.load('assets/alien.png')
        self.image = pygame.transform.scale(self.image, (1, 1))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 500

        #animation deplacement des momies
        self.all_movement = [pygame.image.load('assets/alien/alien1.png'),
                             pygame.image.load('assets/alien/alien2.png'),
                             pygame.image.load('assets/alien/alien3.png'),
                             pygame.image.load('assets/alien/alien4.png'),
                             pygame.image.load('assets/alien/alien5.png'),
                             pygame.image.load('assets/alien/alien6.png'),
                             pygame.image.load('assets/alien/alien7.png'),
                             pygame.image.load('assets/alien/alien8.png'),
                             pygame.image.load('assets/alien/alien9.png'),
                             pygame.image.load('assets/alien/alien10.png'),
                             pygame.image.load('assets/alien/alien11.png'),
                             pygame.image.load('assets/alien/alien12.png'),
                             pygame.image.load('assets/alien/alien13.png'),
                             pygame.image.load('assets/alien/alien14.png'),
                             pygame.image.load('assets/alien/alien15.png'),
                             pygame.image.load('assets/alien/alien16.png'),
                             pygame.image.load('assets/alien/alien17.png'),
                             pygame.image.load('assets/alien/alien18.png'),
                             pygame.image.load('assets/alien/alien19.png'),
                             pygame.image.load('assets/alien/alien20.png'),
                             pygame.image.load('assets/alien/alien21.png'),
                             pygame.image.load('assets/alien/alien22.png'),
                             pygame.image.load('assets/alien/alien23.png'),
                             pygame.image.load('assets/alien/alien24.png')]
        self.walkCounter = 0