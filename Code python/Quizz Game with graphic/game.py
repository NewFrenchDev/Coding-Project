from quizz import Quizz
from quizz_file import QuizzFile
from button import Button
import pygame

class Game:

    def __init__(self):
        self.quizz_files = QuizzFile()
        self.running = False
        self.list_of_quizz = []
        self.index_list_quizz = 0
        self.create_quizz_files()
        self.stay_on_the_quizz = False
        self.question_to_display = ""
        # Initialize buttons
        self.width = 1080
        self.height = 720
        self.original_button_color = [133, 133, 133]
        self.button_A = Button()
        self.button_B = Button()
        self.button_C = Button()
        self.button_D = Button()

    def start(self):
        self.running = True

    def generate_a_number_of_quizz(self, number):
        for i in range(0, number):
            self.list_of_quizz.append(Quizz(self.running))

    def create_quizz_files(self):
        self.quizz_files.create_quizz_files()

    def choose_quizz_number_for_the_game(self):
        no_correct_answer = True
        while no_correct_answer:
            try:
                print("Choisissez le nombre de question pour ce quizz : ")
                number_of_quizz = int(input())
                if number_of_quizz > self.quizz_files.get_total_number_of_question():
                    print(f"Il y a seulement {self.quizz_files.get_total_number_of_question()} questions")
                elif number_of_quizz < 1:
                    print("Oh vous ne voulez donc pas jouer :(")
                else:
                    no_correct_answer = False
            except ValueError:
                print("Essaie plutôt un nombre ;)")
        return number_of_quizz

    def launch_the_game(self):
        # number_of_quizz_to_generate = self.choose_quizz_number_for_the_game()
        self.generate_a_number_of_quizz(50)
        for quizz in self.list_of_quizz:
            quizz.create_random_quizz()
            # quizz.launch_quizz()
            if not quizz.game_running:
                self.running = False
                self.list_of_quizz.clear()
                break
        self.relaunch_game()

    def relaunch_game(self):
        print("\nRelancer le jeu? Y/N")
        restart = input()
        if restart in ['Yes', 'Y', 'y']:
            self.running = True
            self.create_quizz_files()
            self.launch_the_game()
        elif restart in ['No', 'N', 'n']:
            print("A bientôt!")
        else:
            print("Je n'ai pas compris...")
            self.relaunch_game()

    def update(self, screen):
        self.button_A.draw(screen, (0, 0, 0))
        self.button_B.draw(screen, (0, 0, 0))
        self.button_C.draw(screen, (0, 0, 0))
        self.button_D.draw(screen, (0, 0, 0))

        if not self.stay_on_the_quizz:
            self.list_of_quizz[self.index_list_quizz].create_random_quizz()
            self.get_question()
            self.get_propositions()

            self.stay_on_the_quizz = True

    def initialize_buttons(self, screen, text_a="A", text_b="B", text_c="C", text_d="D"):
        self.button_A = Button(self.button_A.color, x=self.width / 20, y=self.height / 2, width=400,
                               height=50, text=text_a, action=self.button_A.display_proposition(screen))
        self.button_A.draw(screen, (0, 0, 0))
        self.button_B = Button(self.button_B.color, x=self.width / 1.7, y=self.height / 2, width=400,
                               height=50, text=text_b, action=self.button_B.display)
        self.button_B.draw(screen, (0, 0, 0))
        self.button_C = Button(self.button_C.color, x=self.width / 20, y=self.height / 1.5, width=400,
                               height=50, text=text_c, action=self.button_C.display)
        self.button_C.draw(screen, (0, 0, 0))
        self.button_D = Button(self.button_D.color, x=self.width / 1.7, y=self.height / 1.5, width=400,
                               height=50, text=text_d, action=self.button_D.display)
        self.button_D.draw(screen, (0, 0, 0))

    def activate_click_on_button_function(self, screen):
        self.button_A.click_on_button(screen)
        self.button_B.click_on_button(screen)
        self.button_C.click_on_button(screen)
        self.button_D.click_on_button(screen)

    def button_animation(self, pos):
        if self.button_A.is_over(pos) and not self.button_A.button_pressed:
            self.button_A.color = (255, 255, 255)
        else:
            self.button_A.color = (133, 133, 133)

        if self.button_B.is_over(pos) and not self.button_B.button_pressed:
            self.button_B.color = (255, 255, 255)
        else:
            self.button_B.color = (133, 133, 133)

        if self.button_C.is_over(pos) and not self.button_C.button_pressed:
            self.button_C.color = (255, 255, 255)
        else:
            self.button_C.color = (133, 133, 133)

        if self.button_D.is_over(pos) and not self.button_D.button_pressed:
            self.button_D.color = (255, 255, 255)
        else:
            self.button_D.color = (133, 133, 133)

    def next_question(self):
        self.stay_on_the_quizz = False
        self.index_list_quizz += 1

    def get_question(self):
        if self.list_of_quizz:
            self.question_to_display = self.list_of_quizz[self.index_list_quizz].question

    def get_propositions(self):
        if self.list_of_quizz:
            self.button_A.text = self.list_of_quizz[self.index_list_quizz].all_answer[0]
            self.button_B.text = self.list_of_quizz[self.index_list_quizz].all_answer[1]
            self.button_C.text = self.list_of_quizz[self.index_list_quizz].all_answer[2]
            self.button_D.text = self.list_of_quizz[self.index_list_quizz].all_answer[3]

