import pygame

#définition de la classe qui va générer les projectiles du joueur
class Projectile(pygame.sprite.Sprite):

    #Constructeur de la classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 130
        self.rect.y = player.rect.y + 100
        self.origin_image = self.image
        self.angle = 0

    def remove(self):
        self.player.all_projectiles.remove(self)

    def rotate(self):
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        #vérifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            #supprimer le projectile
            self.remove()
            #infliger des dégats au monstre
            monster.damage(self.player.attack)

        #vérifier si le projectile n'est plus présent sur l'écran
        if self.rect.x > 1080:
            #supprimer le projectile
            self.remove()

