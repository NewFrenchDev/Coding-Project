import random
import os

#Need this for python 3.9
def re_encode(string_to_re_encode):
    string_reencoded = string_to_re_encode.encode('latin-1')
    string_decoded = string_reencoded.decode('utf-8')
    return string_decoded

class Quizz:

    def __init__(self, question="", solution="", answer="", game_running=True):
        self.question = question
        self.solution = solution
        self.all_answer = ["", "", "", ""]
        self.answer = answer
        self.try_counter = 0
        self.game_running = game_running
        self.running = True
        self.index_files = 0
        self.dumb_path = "./QuizzFolder/DumbFile.txt"
        self.question_path = "./QuizzFolder/Questions.txt"
        self.answer_path = "./QuizzFolder/Answer.txt"
        self.solution_path = "./QuizzFolder/Solutions.txt"

    def define_question(self, question):
        self.question = question

    def define_solution(self, solution):
        self.solution = solution

    def define_all_answer(self, answer_list):
        for index in range(0, len(answer_list)):
            self.all_answer[index] = answer_list[index]
            index += 1
        index = 0
        for el in ["A. ", "B. ", "C. ", "D. "]:
            if self.all_answer[index] != "":
                self.all_answer[index] = el + self.all_answer[index]
                index += 1

    def create_random_quizz(self):
        for path in [self.question_path, self.answer_path, self.solution_path]:
            with open(path, encoding='utf-8') as file:
                lines = file.readlines()
                if path == self.question_path:
                    tmp_list_question = []
                    for question in lines:
                        tmp_list_question.append(question)
                    for i in range(0, 5):
                        random.shuffle(tmp_list_question)
                    line_selected = random.choice(tmp_list_question)
                    self.index_files = lines.index(line_selected)
                else:
                    line_selected = lines[self.index_files]
                if line_selected[-1] in ['\r\n', '\n', '\r', '\n\r']:
                    line_selected = line_selected[:-1]
                if path == self.question_path:
                    self.define_question(line_selected)
                elif path == self.solution_path:
                    self.define_solution(line_selected)
                else:
                    answer_list = line_selected.split(sep='//')
                    random.shuffle(answer_list)
                    self.define_all_answer(answer_list)

    def delete_line_used(self):
        for path in (self.question_path, self.answer_path, self.solution_path):
            with open(path) as file_to_modify:
                with open(self.dumb_path, 'w') as dumb_file:
                    for index, line in enumerate(file_to_modify):
                        if index != self.index_files:
                            dumb_file.write(line)
            os.remove(path)
            os.rename(self.dumb_path, path)

    def rework_answer(self, answer_to_correct):
        self.answer = answer_to_correct.capitalize()

    def get_adjusted_solution(self):
        adjusted_solution = self.solution.capitalize()
        return adjusted_solution

    def display_quizz(self):
        print(self.question)
        print(self.all_answer[0] + "     " + self.all_answer[1])
        print(self.all_answer[2] + "     " + self.all_answer[3])

    def answer_the_question(self):
        self.answer = input()
        if self.answer in ["A", "a"]:
            self.answer = self.all_answer[0][3:]
        elif self.answer in ["B", "b"]:
            self.answer = self.all_answer[1][3:]
        elif self.answer in ["C", "c"] and self.all_answer[2] != "":
            self.answer = self.all_answer[2][3:]
        elif self.answer in ["D", "d"] and self.all_answer[3] != "":
            self.answer = self.all_answer[3][3:]
        self.rework_answer(self.answer)
        self.try_counter += 1

    def win_or_lose(self):
        if self.answer == self.get_adjusted_solution():
            print("Bien joué! C'est la bonne réponse!\n")
            self.delete_line_used()
            self.running = False
        else:
            print("Dommage! Ce n'est pas la bonne réponse!")
            try_left = 3 - self.try_counter
            print("Essai restant : {}".format(try_left))
            if self.try_counter == 3:
                self.running = False
                self.game_running = False
                print(":( Tu as perdu!\n")
                print(f"La réponse était {self.solution}")

    def launch_quizz(self):
        if self.game_running:
            while self.running:
                self.display_quizz()
                self.answer_the_question()
                self.win_or_lose()
