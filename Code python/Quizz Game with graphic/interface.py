import pygame
import math

class Interface():
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    # Générer la fenetre du jeu
    pygame.display.set_caption("Quizz Game")
    screen = pygame.display.set_mode((1080, 720))

    # Charger l'icone du jeu
    icon = pygame.image.load('assets/icon.png')
    pygame.display.set_icon(icon)

    # charge bouton de lancement de partie
    play_button = pygame.image.load('assets/button.png')
    play_button = pygame.transform.scale(play_button, (400, 150))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = math.ceil(screen.get_width() / 3.33)
    play_button_rect.y = math.ceil(screen.get_height() / 2)


    running = True

    # Boucle tant que la condition est vrai
    while running:

        # "appliquer l'arriere plan au jeu
        # screen.blit(background, (0, -200))

        # Vérifier si le jeu a commencé ou non
        # if quizz_game.running:
        # déclencher la partie
        # quizz_game.update(screen)

        # vérifier si notre jeu n'a pas commencé
        # else:
        #     # créer l'écran de bienvenue
        #     screen.blit(play_button, play_button_rect)
        #     screen.blit(banner, banner_rect)

        # mettre à jour l'écran
        pygame.display.flip()

        # si le joueur ferme la fenetre
        for event in pygame.event.get():
            # si l'evenement est fermeture de fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
