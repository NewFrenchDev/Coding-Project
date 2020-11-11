class SolutionFile:

    def __init__(self):
        self.filename = "./QuizzFolder/Solutions.txt"

    def create_solution_file(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write("Staline\n"
                       "L'Espagne\n"
                       "César\n"
                       "Pedro Almodovar\n"
                       "Bob Marley\n"
                       "L'Allemagne\n"
                       "Vérone\n"
                       "Une marâtre\n"
                       "Arès\n"
                       "Le springbok\n"
                       "Feignons !\n"
                       "Henri IV\n"
                       "Homère\n"
                       "Georges Clemenceau\n"
                       "Matthew MacConaughey\n"
                       "La Loire\n"
                       "Rouge\n"
                       "Charlie Hebdo\n"
                       "Le lama\n"
                       "Ennio Morricone")
