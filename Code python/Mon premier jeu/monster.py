import pygame

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540

    def forward(self):
        # si il n'y a pas de collision avec le joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

