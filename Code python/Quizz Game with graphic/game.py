from quizz import Quizz
from quizz_file import QuizzFile

class Game:

    def __init__(self):
        self.quizz_files = QuizzFile()
        self.running = False
        self.list_of_quizz = []
        self.create_quizz_files()

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
        self.generate_a_number_of_quizz(20)
        for quizz in self.list_of_quizz:
            quizz.create_random_quizz()
            quizz.launch_quizz()
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
