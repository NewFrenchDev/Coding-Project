import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.velocity = random.randint(1, 3)
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540

        #animation deplacement des momies
        # animation mouvement du joueur
        self.all_movement = [pygame.image.load('assets/mummy/mummy1.png'),
                             pygame.image.load('assets/mummy/mummy2.png'),
                             pygame.image.load('assets/mummy/mummy3.png'),
                             pygame.image.load('assets/mummy/mummy4.png'),
                             pygame.image.load('assets/mummy/mummy5.png'),
                             pygame.image.load('assets/mummy/mummy6.png'),
                             pygame.image.load('assets/mummy/mummy7.png'),
                             pygame.image.load('assets/mummy/mummy8.png'),
                             pygame.image.load('assets/mummy/mummy9.png'),
                             pygame.image.load('assets/mummy/mummy10.png'),
                             pygame.image.load('assets/mummy/mummy11.png'),
                             pygame.image.load('assets/mummy/mummy12.png'),
                             pygame.image.load('assets/mummy/mummy13.png'),
                             pygame.image.load('assets/mummy/mummy14.png'),
                             pygame.image.load('assets/mummy/mummy15.png'),
                             pygame.image.load('assets/mummy/mummy16.png'),
                             pygame.image.load('assets/mummy/mummy17.png'),
                             pygame.image.load('assets/mummy/mummy18.png'),
                             pygame.image.load('assets/mummy/mummy19.png'),
                             pygame.image.load('assets/mummy/mummy20.png'),
                             pygame.image.load('assets/mummy/mummy21.png'),
                             pygame.image.load('assets/mummy/mummy22.png'),
                             pygame.image.load('assets/mummy/mummy23.png'),
                             pygame.image.load('assets/mummy/mummy24.png')]
        self.walkCounter = 0

    def remove(self):
        self.game.all_monster.remove(self)

    def damage(self, amount):
        #infliger des dégâts
        self.health -= amount
        #vérifier si le monstre n'a plus de vie
        if self.health <= 0:
            self.remove()
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.game.spawn_monster()

    def update_health_bar(self, surface):
        #dessiner notre bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 15, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 15, self.rect.y - 10, self.health, 5])

    def forward(self, screen):
        # si il n'y a pas de collision avec le joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.animate_monster(screen)
            self.rect.x -= self.velocity
        #si le monstre est en collision avec le joueur
        else:
            #infliger des dégats
            self.game.player.damage(self.attack)

    def animate_monster(self, screen):
        self.image = self.all_movement[self.walkCounter // 3]
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.walkCounter == 23:
            self.walkCounter = 0
        else:
            self.walkCounter += 1


