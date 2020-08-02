from monster import Monster
import random
import pygame

class Alien(Monster):

    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.health = 80
        self.max_health = 80
        self.attack = 0.6
        self.velocity = random.randint(2, 4)
        self.isAlien = True
        self.image = pygame.image.load('assets/alien.png')
        self.image = pygame.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 400

        #animation deplacement des aliens
        self.from_Left = False
        self.all_raw_movement = [pygame.image.load('assets/alien/alien1.png'),
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
        self.all_movement = []
        self.walkCounter = 0

    def update_health_bar(self, screen):
        #dessiner notre bar de vie
        pygame.draw.rect(screen, (60, 63, 60), [self.rect.x + 35, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(screen, (111, 210, 46), [self.rect.x + 35, self.rect.y - 10, self.health, 5])

    def transform_alien_image_movement(self):
        for image in self.all_raw_movement:
            self.all_movement.append(pygame.transform.scale(image, (150, 100)))
