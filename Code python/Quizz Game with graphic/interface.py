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
        self.original_button_color = [133, 133, 133]
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.icon = pygame.image.load('assets/icon.png')
        self.background = pygame.image.load('assets/bg.jpg')
        self.instruction = pygame.draw.rect(self.screen, [0, 0, 205], [self.width / 1.8, self.height / 5, 600, 200])
        self.play_button = pygame.image.load('assets/button.png')
        self.play_button_rect = self.play_button.get_rect()
        self.button_A = Button(self.original_button_color, x=self.width / 20, y=self.height / 2, width=400, height=50,
                               text="A")
        self.button_B = Button(self.original_button_color, x=self.width / 1.7, y=self.height / 2, width=400, height=50,
                               text='B')
        self.button_C = Button(self.original_button_color, x=self.width / 20, y=self.height / 1.5, width=400, height=50,
                               text='C')
        self.button_D = Button(self.original_button_color, x=self.width / 1.7, y=self.height / 1.5, width=400,
                               height=50, text='D')

    def create_window(self, res=(1080, 720)):
        # Générer la fenetre du jeu
        pygame.display.set_caption("Quizz Game")
        self.screen = pygame.display.set_mode(res)

        # Charger l'icone du jeu
        pygame.display.set_icon(self.icon)

        # charger l'arrière plan du jeu

    def generate_window(self):

        # charger l'arrière plan du jeu
        self.screen.fill([66, 178, 236])
        pygame.display.update()

        # charge bouton de lancement de partie
        self.play_button = pygame.transform.scale(self.play_button, (400, 150))
        self.play_button_rect.x = math.ceil(self.screen.get_width() / 3.33)
        self.play_button_rect.y = math.ceil(self.screen.get_height() / 2)

    # def update_question(self, text="question"):
    #     self.

    def display_buttons(self, text_a="A", text_b="B", text_c="C", text_d="D"):
        self.button_A = Button(self.button_A.color, x=self.width / 20, y=self.height / 2, width=400, height=50,
                               text=text_a, action=self.button_A.display)
        self.button_A.draw(self.screen, (0, 0, 0))
        self.button_B = Button(self.button_B.color, x=self.width / 1.7, y=self.height / 2, width=400, height=50,
                               text=text_b, action=self.button_B.display)
        self.button_B.draw(self.screen, (0, 0, 0))
        self.button_C = Button(self.button_C.color, x=self.width / 20, y=self.height / 1.5, width=400, height=50,
                               text=text_c, action=self.button_C.display)
        self.button_C.draw(self.screen, (0, 0, 0))
        self.button_D = Button(self.button_D.color, x=self.width / 1.7, y=self.height / 1.5, width=400, height=50,
                               text=text_d, action=self.button_D.display)
        self.button_D.draw(self.screen, (0, 0, 0))

    def running_game(self):

        self.create_window()

        self.generate_window()

        running = True
        button_displayed = False

        # Boucle tant que la condition est vrai
        while running:

            pygame.display.update()

            # Vérifier si le jeu a commencé ou non
            if self.game.running:
                if not button_displayed:
                    self.display_buttons()
                    button_displayed = True
                # print("Game is running")
            # déclencher la partie
            # self.game.update(self.screen)

            # vérifier si notre jeu n'a pas commencé
            else:
                # créer l'écran de bienvenue
                self.screen.blit(pygame.transform.scale(self.background, (1080, 720)), (0, 0))
                small_font = pygame.font.SysFont('Corbel', 35)
                text = small_font.render(
                    "Instruction : Pour chaque question, 4 propositions\n 1 seule bonne réponse possible\n Bonne chance ;)",
                    True, (255, 255, 255))
                self.screen.blit(text, (self.width / 8 + 20, self.height / 5))
                self.screen.blit(self.play_button, self.play_button_rect)
                print("Game is not running")

            # mettre à jour l'écran
            pygame.display.flip()

            # si le joueur ferme la fenetre
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                # si l'evenement est fermeture de fenetre
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        # "appliquer l'arriere plan au jeu
                        self.game.start()
                        # self.screen.fill([68, 178, 236])
                        self.screen.blit(pygame.transform.scale(self.background, (1080, 720)), (0, 0))
                        self.display_buttons()

                    self.button_A.click_on_button()
                    self.button_B.click_on_button()
                    self.button_C.click_on_button()
                    self.button_D.click_on_button()

                if event.type == pygame.MOUSEMOTION and button_displayed:
                    if self.button_A.is_over(pos):
                        self.button_A.color = (255, 255, 255)
                        self.button_A.draw(self.screen, outline=(0, 0, 0))
                    else:
                        self.button_A.color = (133, 133, 133)
                        self.button_A.draw(self.screen, outline=(0, 0, 0))
                    if self.button_B.is_over(pos):
                        self.button_B.color = (255, 255, 255)
                        self.button_B.draw(self.screen, outline=(0, 0, 0))
                    else:
                        self.button_B.color = (133, 133, 133)
                        self.button_B.draw(self.screen, outline=(0, 0, 0))
                    if self.button_C.is_over(pos):
                        self.button_C.color = (255, 255, 255)
                        self.button_C.draw(self.screen, outline=(0, 0, 0))
                    else:
                        self.button_C.color = (133, 133, 133)
                        self.button_C.draw(self.screen, outline=(0, 0, 0))
                    if self.button_D.is_over(pos):
                        self.button_D.color = (255, 255, 255)
                        self.button_D.draw(self.screen, outline=(0, 0, 0))
                    else:
                        self.button_D.color = (133, 133, 133)
                        self.button_D.draw(self.screen, outline=(0, 0, 0))

        pygame.time.delay(10)
