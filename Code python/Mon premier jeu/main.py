import pygame
from game import Game
pygame.init()

#Générer la fenetre du jeu
pygame.display.set_caption("Shooter Game")
screen = pygame.display.set_mode((1080, 720))

#charger l'arrière plan du jeu
background = pygame.image.load('assets/bg.jpg')

#charger le jeu
game = Game()

running = True

#Boucle tant que la condition est vrai
while running:

    #"appliquer l'arriere plan au jeu
    screen.blit(background, (0, -200))

    #appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    #récupérer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    #appliquer l'ensemble des images du groupe de projectiles
    game.player.all_projectiles.draw(screen)

    #vérifier la direction du joueur
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

