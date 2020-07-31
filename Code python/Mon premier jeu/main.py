import pygame
import math
import platform
from game import Game
from system_language import OsLanguage
pygame.init()

#Verifier l'OS du joueur
user_platform = platform.system()
#Si Window --> Vérifier le language du systeme du joueur
if user_platform == 'Windows':
    os_language = OsLanguage()
    os_language.check_user_default_language()

#Générer la fenetre du jeu
pygame.display.set_caption("Shooter Game")
screen = pygame.display.set_mode((1080, 720))

#charger l'arrière plan du jeu
background = pygame.image.load('assets/bg.jpg')

#importer la banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

#charge bouton de lancement de partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)

#charger le jeu
game = Game(os_language)

game.player.update_player_image_movement()

running = True

#Boucle tant que la condition est vrai
while running:

    #"appliquer l'arriere plan au jeu
    screen.blit(background, (0, -200))

    #Vérifier si le jeu a commencé ou non
    if game.is_playing:
        #déclencher la partie
        game.update(screen)
        print(os_language.user_default_language)
    #vérifier si notre jeu n'a pas commencé
    else:
        #créer l'écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        #si l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("La fenêtre s'est fermée")
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est enclenché pour lancer projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

            elif event.key == pygame.K_UP:
                game.player.jump(screen)

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification si la souris clique sur le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                game.start()
