import pygame
from projectile import Projectile

#Classe qui représente le joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        #Stat du joueur
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 10
        #Image du joueur
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/wizard.png')
        self.image = pygame.transform.scale(self.image, (250, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        #mouvement pour le saut
        self.movex = 0
        self.movey = 0

        #animation mouvement du joueur
        self.all_raw_image_player_walk = [pygame.image.load('assets/wizard/Walk/0.png'),
                                          pygame.image.load('assets/wizard/Walk/1.png'),
                                          pygame.image.load('assets/wizard/Walk/2.png'),
                                          pygame.image.load('assets/wizard/Walk/3.png'),
                                          pygame.image.load('assets/wizard/Walk/4.png'),
                                          pygame.image.load('assets/wizard/Walk/5.png'),
                                          pygame.image.load('assets/wizard/Walk/6.png'),
                                          pygame.image.load('assets/wizard/Walk/7.png'),
                                          pygame.image.load('assets/wizard/Walk/8.png'),
                                          pygame.image.load('assets/wizard/Walk/9.png')]
        self.player_walk = []
        self.walkCounter = 0
        self.jumpCount = 0
        self.all_raw_image_player_jump = [pygame.image.load('assets/wizard/Jump/0.png'),
                                          pygame.image.load('assets/wizard/Jump/1.png'),
                                          pygame.image.load('assets/wizard/Jump/2.png'),
                                          pygame.image.load('assets/wizard/Jump/3.png'),
                                          pygame.image.load('assets/wizard/Jump/4.png'),
                                          pygame.image.load('assets/wizard/Jump/5.png'),
                                          pygame.image.load('assets/wizard/Jump/6.png'),
                                          pygame.image.load('assets/wizard/Jump/7.png'),
                                          pygame.image.load('assets/wizard/Jump/8.png'),
                                          pygame.image.load('assets/wizard/Jump/9.png')]
        self.player_jump = []
        self.isJump = False
        self.jumpCounter = 10

    def damage(self, amount):
        if self.health > 0:
            self.health -= amount
        else:
            #si le joueur n'a plus de point de vie
            self.game.reinitialize_game()

    def update_health_bar(self, surface):
        #dessiner notre bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 78, self.rect.y + 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 78, self.rect.y + 20, self.health, 5])

    def launch_projectile(self):
        #Creer une nouvelle instance de la classe Projectile
        self.all_projectiles.add(Projectile(self))
        effect = pygame.mixer.Sound('assets/sounds/tir.wav')
        effect.play()

    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocity

    def move_left(self):
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x -= self.velocity

    def jump(self):
        if self.jumpCounter >= -10:
            neg = 1
            if self.jumpCounter < 0:
                neg = -1
            self.rect.y -= (self.jumpCounter ** 2) * 0.5 * neg
            self.jumpCounter -= 1
        else:
            self.isJump = False
            self.jumpCounter = 10
            #réinitialisation du positionnement du joueur
            self.rect.y = 500

    def transform_player_image_movement(self):
        for image in self.all_raw_image_player_walk:
            self.player_walk.append(pygame.transform.scale(image, (250, 200)))
        for image in self.all_raw_image_player_jump:
            self.player_jump.append(pygame.transform.scale(image, (250, 200)))

    def animate_player_deplacement(self, screen):
        self.image = self.player_walk[self.walkCounter // 3]
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.walkCounter == 27:
            self.walkCounter = 0
        else:
            self.walkCounter += 1

    def animate_player_jump(self, screen):
        self.image = self.player_jump[self.jumpCount // 3]
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.jumpCount == 27:
            self.jumpCount = 0
        else:
            self.jumpCount += 1

    def initialise_player_image(self, screen):
        self.image = pygame.image.load('assets/wizard.png')
        self.image = pygame.transform.scale(self.image, (250, 200))
        screen.blit(self.image, (self.rect.x, self.rect.y))
