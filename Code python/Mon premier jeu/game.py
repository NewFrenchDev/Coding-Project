from player import Player
from monster import Monster
from alien import Alien
import pygame
import random
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
        self.my_font = pygame.font.SysFont("Comic", 32)
        self.score_int = 0
        self.score = 'SCORE : 0'
        #compteur de frame
        self.frame_counter = 0

    def update_score(self):
        self.score = "SCORE : {}".format(self.score_int)

    def start(self):
        effect = pygame.mixer.Sound('assets/sounds/clic.wav')
        effect.play()
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def reinitialize_game(self):
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.score_int = 0
        self.update_score()
        self.is_playing = False

    def update(self, screen):
        score_display = self.my_font.render(self.score, 1, (255, 255, 0))
        screen.blit(score_display, (100, 100))

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
            self.player.isLeft = False
            # permet le saut si la touche up ou z est pressé
            if self.player.isJump:
                self.player.animate_player_jump(screen)
                self.player.jump()
            else:
                #Animation du mouvement
                self.player.animate_player_deplacement(screen)
            #Déplacement du joueur
            self.player.move_right()
        elif (self.pressed.get(pygame.K_LEFT) or self.pressed.get(pygame.K_q)) and self.player.rect.x > 0:
            self.player.isLeft = True
            # permet le saut si la touche up ou z est pressé
            if self.player.isJump:
                self.player.animate_player_jump(screen)
                self.player.jump()
            #Animation du mouvement
            else:
                self.player.animate_player_deplacement(screen)
            #déplacement du joueur
            self.player.move_left()
        else:
            if self.player.isJump:
                self.player.animate_player_jump(screen)
                self.player.jump()
            else:
                self.player.animate_player_stand(screen)
                # self.player.initialise_player_image(screen)

    def spawn_monster(self):
        mummy_appears = random.randint(0, 1)
        if mummy_appears:
            self.monster = Monster(self)
        else:
            self.monster = Alien(self)
            self.monster.transform_alien_image_movement()
        monster_from_Left = random.randint(0, 1)
        if monster_from_Left:
            self.monster.from_Left = True
            self.monster.velocity = self.monster.velocity * -1
            self.monster.rect.x = 0 - random.randint(0, 300)
        else:
            self.monster.from_Left = False
        self.all_monster.add(self.monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
