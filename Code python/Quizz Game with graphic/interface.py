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
        self.instruction = pygame.draw.rect(self.screen, [0, 0, 205], [self.width/1.8, self.height/5, 600, 200])
        self.play_button = pygame.image.load('assets/button.png')
        self.play_button_rect = self.play_button.get_rect()
        self.button_A = pygame.draw.rect(self.screen, self.original_button_color, (self.width / 20, self.height / 2, 400, 50), 0)
        # self.button_A = pygame.Rect(self.width / 20, self.height / 2, 400, 50)
        # self.button_A = Button(self.original_button_color, self.width / 20, self.height / 2, 400, 50, "A")
        self.button_B = Button(self.original_button_color, self.width / 1.7, self.height / 2, 400, 50, 'B')
        self.button_C = Button(self.original_button_color, self.width / 20, self.height / 1.5, 400, 50, 'C')
        self.button_D = Button(self.original_button_color, self.width / 1.7, self.height / 1.5, 400, 50, 'D')

    def create_window(self, res=(1080, 720)):
        # Générer la fenetre du jeu
        pygame.display.set_caption("Quizz Game")
        self.screen = pygame.display.set_mode(res)

        # Charger l'icone du jeu
        pygame.display.set_icon(self.icon)

        # charger l'arrière plan du jeu

    def generate_window(self):

        #charger l'arrière plan du jeu
        self.screen.fill([66, 178, 236])
        pygame.display.update()

        # charge bouton de lancement de partie
        self.play_button = pygame.transform.scale(self.play_button, (400, 150))
        self.play_button_rect.x = math.ceil(self.screen.get_width() / 3.33)
        self.play_button_rect.y = math.ceil(self.screen.get_height() / 2)

    # def update_question(self, text="question"):
    #     self.

    def update_buttons(self, text_a="A", text_b="B", text_c="C", text_d="D"):
        self.button_A = pygame.draw.rect(self.screen, self.original_button_color, (self.width / 20, self.height / 2, 400, 50), 0)
        # self.button_A = pygame.Rect(self.width / 20, self.height / 2, 400, 50)
        # self.button_A = Button(self.original_button_color, self.width / 20, self.height / 2, 400, 50, text_a)
        # self.button_A.draw(self.screen, (0, 0, 0))
        self.button_B = Button(self.original_button_color, self.width / 1.7, self.height / 2, 400, 50, text_b)
        self.button_B.draw(self.screen, (0, 0, 0))
        self.button_C = Button(self.original_button_color, self.width / 20, self.height / 1.5, 400, 50, text_c)
        self.button_C.draw(self.screen, (0, 0, 0))
        self.button_D = Button(self.original_button_color, self.width / 1.7, self.height / 1.5, 400, 50, text_d)
        self.button_D.draw(self.screen, (0, 0, 0))

    def running_game(self):

        self.create_window()

        self.generate_window()

        running = True

        # Boucle tant que la condition est vrai
        while running:

            # "appliquer l'arriere plan au jeu
            # self.screen.blit(pygame.transform.scale(self.background, (1080, 720)), (0, 0))

            # Vérifier si le jeu a commencé ou non
            if self.game.running:
                pass
                # print("Game is running")
            # déclencher la partie
            # self.game.update(self.screen)

            # vérifier si notre jeu n'a pas commencé
            else:
                # créer l'écran de bienvenue
                small_font = pygame.font.SysFont('Corbel', 35)
                text = small_font.render("Instruction : Pour chaque question, 4 propositions\n 1 seule bonne réponse possible\n Bonne chance ;)", True, (255, 255, 255))
                self.screen.blit(text, (self.width/8 + 20, self.height/5))
                self.screen.blit(self.play_button, self.play_button_rect)
                print("Game is not running")
            #     screen.blit(banner, banner_rect)

            # mettre à jour l'écran
            pygame.display.flip()

            # si le joueur ferme la fenetre
            for event in pygame.event.get():
                # si l'evenement est fermeture de fenetre
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        # charger l'arrière plan du jeu
                        self.game.start()
                        self.screen.fill([68, 178, 236])
                        self.update_buttons(text_a="Il était bon de vivre en son temps pour voyager tranquillement au que ce temps me manque bien")
                        pygame.display.update()

                    elif self.button_A.collidepoint(event.pos):
                        print("Button A is pressed")
                    # elif self.button_B.collidepoint(event.pos):
                    #     print("Button B is pressed")
                    # elif self.button_C.collidepoint(event.pos):
                    #     print("Button C is pressed")
                    # elif self.button_D.collidepoint(event.pos):
                    #     print("Button D is pressed")

        pygame.time.delay(10)