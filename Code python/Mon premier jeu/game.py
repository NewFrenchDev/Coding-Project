from player import Player
from monster import Monster
import pygame
pygame.init()

class Game:

    def __init__(self, language):
        #definir si notre jeu a commencé ou non
        self.is_playing = False
        #détecter le language de l'OS
        self.language = language
        #générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #Sauvegarde la liste des boutons utilisé
        self.pressed = {}
        #générer un monstre
        self.monster = Monster(self)
        #génération groupe de monstre
        self.all_monster = pygame.sprite.Group()
        #Score du joueur
        self.score = 0
        #Indication de la mort d'un monstre
        self.monster_dead = False
        #delimitation du sol
        self.ground = 0

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        #réinitialiser le jeu
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False


    def update(self, screen):

        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la vie du joueur
        self.player.update_health_bar(screen)

        # récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # déplacement des monstres
        for monster in self.all_monster:
            monster.forward(screen)
            monster.update_health_bar(screen)

        # appliquer l'ensemble des images du groupe de monstre
        self.all_monster.draw(screen)

        # appliquer l'ensemble des images du groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # vérifier la direction du joueur
        if (self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_d)) and self.player.rect.x + self.player.rect.width < screen.get_width():
            #Animation du mouvement
            self.player.animate_player_deplacement(screen)
            #Déplacement du joueur
            self.player.move_right()
        elif (self.pressed.get(pygame.K_LEFT) or self.pressed.get(pygame.K_q)) and self.player.rect.x > 0:
            #Animation du mouvement
            self.player.animate_player_deplacement(screen)
            #déplacement du joueur
            self.player.move_left()
        else:
            self.player.initialise_player_image(screen)

    def spawn_monster(self):
            self.monster = Monster(self)
            self.all_monster.add(self.monster)
            #réinitialiser l'indicateur de monstre mort après apparition d'un autre monstre
            self.monster_dead = False

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
