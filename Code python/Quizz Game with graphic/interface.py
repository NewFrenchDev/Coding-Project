import pygame
from game import Game
from button import Button
import math

pygame.init()


class Interface:

    def __init__(self, game=Game()):
        self.game = game
        self.width = 1080
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.icon = pygame.image.load('assets/icon.png')
        self.background = pygame.image.load('assets/bg.jpg')
        self.instruction = pygame.draw.rect(self.screen, [0, 0, 205], [self.width / 1.8, self.height / 5, 600, 200])
        self.play_button = pygame.image.load('assets/button.png')
        self.play_button_rect = self.play_button.get_rect()

    def create_window(self, res=(1080, 720)):
        # Générer la fenetre du jeu
        pygame.display.set_caption("Quizz Game")
        self.screen = pygame.display.set_mode(res)

        # Charger l'icone du jeu
        pygame.display.set_icon(self.icon)

    def display_welcome_screen(self):

        # charger l'arrière plan du jeu
        self.screen.fill([66, 178, 236])
        pygame.display.update()

        # charge bouton de lancement de partie
        self.play_button = pygame.transform.scale(self.play_button, (400, 150))
        self.play_button_rect.x = math.ceil(self.screen.get_width() / 3.33)
        self.play_button_rect.y = math.ceil(self.screen.get_height() / 2)

        # créer l'écran de bienvenue
        self.screen.blit(pygame.transform.scale(self.background, (1080, 720)), (0, 0))
        small_font = pygame.font.SysFont('Corbel', 35)
        text = small_font.render(
            "Instruction : Pour chaque question, 4 propositions\n 1 seule bonne réponse possible\n Bonne chance ;)",
            True, (255, 255, 255))
        self.screen.blit(text, (self.width / 8 + 20, self.height / 5))
        self.screen.blit(self.play_button, self.play_button_rect)

    def running_game(self):

        self.create_window()

        self.display_welcome_screen()

        self.game.generate_a_number_of_quizz(50)

        running = True
        button_displayed = False

        # Boucle tant que la condition est vrai
        while running:

            pygame.display.update()

            # Vérifier si le jeu a commencé ou non
            if self.game.running:
                if not button_displayed:
                    self.screen.blit(pygame.transform.scale(self.background, (1080, 720)), (0, 0))
                    self.game.initialize_buttons(self.screen)
                    button_displayed = True
                else:
                    self.screen.blit(pygame.transform.scale(self.background, (1080, 720)), (0, 0))
                    self.game.update(self.screen)

            # mettre à jour l'écran
            pygame.display.flip()

            # si le joueur ferme la fenetre
            for event in pygame.event.get():
                #récupère la position de la souris
                pos = pygame.mouse.get_pos()
                # si l'evenement est fermeture de fenetre
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        self.game.start()

                    self.game.activate_click_on_button_function(self.screen)

                if event.type == pygame.MOUSEMOTION and button_displayed:
                    self.game.button_animation(pos)

        pygame.time.delay(10)
