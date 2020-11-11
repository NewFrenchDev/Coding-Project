import os

class QuestionFile:

    def __init__(self):
        self.directory = "QuizzFolder"
        self.filename = "./QuizzFolder/Questions.txt"

    def create_folder(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            print("Folder is created")

    def create_question_file(self):
        self.create_folder()
        with open(self.filename, 'w', encoding='utf-8') as file:
            print("Question file created!")
            file.write("Quel célèbre dictateur dirigea l’URSS du milieu des années 1920 à 1953 ?\n"
                       "Dans quel pays peut-on trouver la Catalogne, l’Andalousie et la Castille ?\n"
                       "Qui a dit : « Le sort en est jeté » (Alea jacta est) ?\n"
                       "Quel cinéaste a réalisé « Parle avec elle » et « Volver » ?\n"
                       "À qui doit-on la chanson « I Shot the Sheriff » ?\n"
                       "Quel pays a remporté la coupe du monde de football en 2014 ?\n"
                       "Dans quelle ville italienne l’action de la pièce de Shakespeare « Roméo et Juliette » se situe-t-elle ?\n"
                       "Par quel mot désigne-t-on une belle-mère cruelle ?\n"
                       "Qui était le dieu de la guerre dans la mythologie grecque ?\n"
                       "Parmi les animaux suivants, lequel peut se déplacer le plus rapidement ?\n"
                       "Quel est l’impératif du verbe feindre à la première personne du pluriel ?\n"
                       "Quel roi de France proclama l’Édit de Nantes ?\n"
                       "À quel écrivain attribue-t-on la rédaction de l’Illiade et l’Odyssée ?\n"
                       "Qui s’est déclaré « premier flic de France » ?\n"
                       "Quel acteur américain incarne le héros du film de Christopher Nolan de 2014 « Interstellar » ?\n"
                       "Quel est le plus long fleuve de France selon la partie coulant sur le territoire ?\n"
                       "Le drapeau russe est blanc, bleu et…?\n"
                       "Quel journal a été attaqué par des terroristes islamistes en janvier 2015 ?\n"
                       "Quel animal andin de la famille des camélidés est élevé pour sa laine ?\n"
                       "À quel compositeur doit-on les bandes-son de films comme « Il était une fois en Amérique », « Pour une poignée de dollars », ou le « Le clan des Siciliens »?")