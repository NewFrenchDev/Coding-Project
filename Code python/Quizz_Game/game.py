from quizz import Quizz
from quizz_file import QuizzFile

class Game:

    def __init__(self):
        self.quizz_files = QuizzFile()
        self.running = True
        self.list_of_quizz = []
        self.create_quizz_files()

    def generate_a_number_of_quizz(self, number):
        for i in range(0, number):
            self.list_of_quizz.append(Quizz(self.running))

    def create_quizz_files(self):
        self.quizz_files.create_quizz_files()

    def launch_the_game(self):
        trying = True
        while trying:
            try:
                print("Choose the number of quizz to answer : ")
                number_of_quizz = int(input())
                if number_of_quizz > self.quizz_files.get_total_number_of_question():
                    print(f"There are only {self.quizz_files.get_total_number_of_question()} questions")
                    continue
                else:
                    break
            except:
                print("You should try a number ;)")
        self.generate_a_number_of_quizz(number_of_quizz)
        for quizz in self.list_of_quizz:
            quizz.create_random_quizz()
            quizz.launch_quizz()
            if not quizz.game_running:
                self.running = False
                self.list_of_quizz.clear()
                break
        self.relaunch_game()

    def relaunch_game(self):
        print("\nDo you want to retry? Y/N")
        restart = input()
        if restart in ['Yes', 'Y', 'y']:
            self.running = True
            self.create_quizz_files()
            self.launch_the_game()
        elif restart in ['No', 'N', 'n']:
            print("See you soon!")
        else:
            print('Incorrect entry...')
            self.relaunch_game()
