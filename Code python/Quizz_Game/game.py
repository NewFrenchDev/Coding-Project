from quizz import Quizz

class Game:

    def __init__(self):
        self.running = True
        self.list_of_quizz = []

    def get_game_stat(self):
        return self.running

    def choose_number_of_quizz(self, number):
        for i in range(0, number):
            self.list_of_quizz.append(Quizz(self.running))

    def launch_the_game(self):
        trying = True
        while trying:
            try:
                number_of_quizz = int(input("Choose the number of quizz : "))
                break
            except:
                print("You should try a number ;)")
        self.choose_number_of_quizz(number_of_quizz)
        for quizz in self.list_of_quizz:
            quizz.select_random_quizz()
            quizz.launch_quizz()
            if not quizz.game_running:
                self.running = False
                self.list_of_quizz.clear()
                break
        self.relaunch_game()

    def relaunch_game(self):
        restart = input("Do you want to retry? Y/N")
        if restart in ['Yes', 'Y', 'y']:
            self.running = True
            self.launch_the_game()
        elif restart in ['No', 'N', 'n']:
            print("See you soon!")
        else:
            print('Incorrect entry...')
            self.relaunch_game()
