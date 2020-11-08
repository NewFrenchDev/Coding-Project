import random

class Quizz:

    def __init__(self, question="", solution="", answer="", game_running=True):
        self.question = question
        self.solution = solution
        self.answer = answer
        self.try_counter = 0
        self.game_running = game_running
        self.running = True
        self.quizz_path = "Quizz.txt"

    def define_question(self, question):
        self.question = question

    def define_solution(self, solution):
        self.solution = solution

    def select_random_quizz(self):
        question = ''
        solution = ''
        solution_part_reading = False
        with open(self.quizz_path) as f:
            lines = f.readlines()
            line_selected = random.choice(lines)
            if line_selected[-1] in ['\r\n', '\n', '\r', '\n\r']:
                line_selected = line_selected[:-1]
            for carac in line_selected:
                if carac == '&':
                    solution_part_reading = True
                    continue
                if not solution_part_reading:
                    question += carac
                else:
                    solution += carac
        f.close()
        self.define_question(question)
        self.define_solution(solution)

    def correct_answer_format(self, answer_to_correct):
        try:
            self.answer = answer_to_correct[0].upper() + answer_to_correct[1:].lower()
        except:
            self.answer = ""

    def answer_the_question(self):
        answer = input(self.question)
        self.correct_answer_format(answer)
        self.try_counter += 1

    def win_or_lose(self):
        if self.answer == self.solution:
            print('Good job! This is the right answer')
            print('\n')
            self.running = False
        else:
            print('Too bad! that is not the correct answer')
            try_left = 3 - self.try_counter
            print("Try left : {}".format(try_left))
            if self.try_counter == 3:
                self.running = False
                self.game_running = False
                print(":( You have lost the game\n")

    def launch_quizz(self):
        if self.game_running:
            while self.running:
                self.answer_the_question()
                self.win_or_lose()

    def relaunch_game(self):
        restart = input("Do you want to retry? Y/N")
        if restart in ['Yes', 'Y', 'y']:
            self.game_running = True
        elif restart in ['No', 'N', 'n']:
            print("See you soon!")
        else:
            print('Incorrect entry...')
            self.relaunch_game()
