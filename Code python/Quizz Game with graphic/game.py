from quizz import Quizz
from quizz_file import QuizzFile
from button import Button
import threading
import time
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
        self.solution = ""
        self.next = False
        # Initialize buttons
        self.width = 1080
        self.height = 720
        self.original_button_color = [133, 133, 133]
        self.button_A = Button()
        self.button_B = Button()
        self.button_C = Button()
        self.button_D = Button()
        self.thread1 = threading.Thread
        self.thread2 = threading.Thread
        #Question display
        self.question = None

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
        self.redraw(screen)

        if not self.stay_on_the_quizz:
            x = self.thread1(target=self.create_quizz)
            x.start()
            x.join()

            self.get_question()
            self.get_propositions()

            self.stay_on_the_quizz = True

        if self.next:
            x = self.thread2(target=self.next_question)
            x.start()


        self.check_answer()

    def redraw(self, screen):
        text = str(self.list_of_quizz[self.index_list_quizz].question)
        font = pygame.font.SysFont("Corbel", 25)
        text = font.render(text, True, (255, 255, 255))
        screen.blit(text, (100, 225))
        # self.drawText(surface=screen, text=str(self.list_of_quizz[self.index_list_quizz].question), color=(255, 255, 255), rect=(900, 300, 100, 100)
        #               , font={10, 12, 14, 20})

        self.button_A.draw(screen, (0, 0, 0))
        self.button_B.draw(screen, (0, 0, 0))
        self.button_C.draw(screen, (0, 0, 0))
        self.button_D.draw(screen, (0, 0, 0))

    def create_quizz(self):
        self.list_of_quizz[self.index_list_quizz].create_random_quizz()
        # time.sleep(0.2)

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
        elif not self.button_A.button_pressed:
            self.button_A.color = (133, 133, 133)

        if self.button_B.is_over(pos) and not self.button_B.button_pressed:
            self.button_B.color = (255, 255, 255)
        elif not self.button_B.button_pressed:
            self.button_B.color = (133, 133, 133)

        if self.button_C.is_over(pos) and not self.button_C.button_pressed:
            self.button_C.color = (255, 255, 255)
        elif not self.button_C.button_pressed:
            self.button_C.color = (133, 133, 133)

        if self.button_D.is_over(pos) and not self.button_D.button_pressed:
            self.button_D.color = (255, 255, 255)
        elif not self.button_D.button_pressed:
            self.button_D.color = (133, 133, 133)

    def next_question(self):
        self.next = False
        self.delete_quizz_used()
        self.stay_on_the_quizz = False
        self.reinitialize_button()

    def delete_quizz_used(self):
        self.list_of_quizz[self.index_list_quizz].delete_line_used()

    def reinitialize_button(self):
        self.button_A.color = self.original_button_color
        self.button_A.button_pressed = False
        self.button_B.color = self.original_button_color
        self.button_B.button_pressed = False
        self.button_C.color = self.original_button_color
        self.button_C.button_pressed = False
        self.button_D.color = self.original_button_color
        self.button_D.button_pressed = False

    def get_question(self):
        if self.list_of_quizz:
            self.question_to_display = self.list_of_quizz[self.index_list_quizz].question

    def get_solution(self):
        if self.list_of_quizz:
            self.solution = self.list_of_quizz[self.index_list_quizz].solution

    def get_propositions(self):
        if self.list_of_quizz:
            self.button_A.text = self.list_of_quizz[self.index_list_quizz].all_answer[0]
            self.button_B.text = self.list_of_quizz[self.index_list_quizz].all_answer[1]
            self.button_C.text = self.list_of_quizz[self.index_list_quizz].all_answer[2]
            self.button_D.text = self.list_of_quizz[self.index_list_quizz].all_answer[3]

    def check_answer(self):
        if self.list_of_quizz[self.index_list_quizz].solution == self.button_A.text[3:] and self.button_A.button_pressed:
            self.button_A.color = (0, 255, 0)
            self.next = True
            # time.sleep(0.2)
        elif self.list_of_quizz[self.index_list_quizz].solution != self.button_A.text[3:] and self.button_A.button_pressed:
            self.button_A.color = (255, 0, 0)

        if self.list_of_quizz[self.index_list_quizz].solution == self.button_B.text[3:] and self.button_B.button_pressed:
            self.button_B.color = (0, 255, 0)
            self.next = True
            # time.sleep(0.2)
        elif self.list_of_quizz[self.index_list_quizz].solution != self.button_B.text[3:] and self.button_B.button_pressed:
            self.button_B.color = (255, 0, 0)

        if self.list_of_quizz[self.index_list_quizz].solution == self.button_C.text[3:] and self.button_C.button_pressed:
            self.button_C.color = (0, 255, 0)
            self.next = True
            # time.sleep(0.2)
        elif self.list_of_quizz[self.index_list_quizz].solution != self.button_C.text[3:] and self.button_C.button_pressed:
            self.button_C.color = (255, 0, 0)

        if self.list_of_quizz[self.index_list_quizz].solution == self.button_D.text[3:] and self.button_D.button_pressed:
            self.button_D.color = (0, 255, 0)
            self.next = True
            # time.sleep(0.2)
        elif self.list_of_quizz[self.index_list_quizz].solution != self.button_D.text[3:] and self.button_D.button_pressed:
            self.button_D.color = (255, 0, 0)

    def drawText(self, surface, text, color, rect, font, aa=False, bkg=None):
        rect = pygame.Rect(rect)
        y = rect.top
        lineSpacing = -2

        # get the height of the font
        fontHeight = font.size("Corbel")[1]

        while text:
            i = 1

            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break

            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # if we've wrapped the text, then adjust the wrap to the last word
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)

            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing

            # remove the text we just blitted
            text = text[i:]

        return text