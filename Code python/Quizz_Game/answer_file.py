class AnswerFile:

    def __init__(self):
        self.filename = "./QuizzFolder/Answer.txt"

    def create_answer_file(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write("Trotski//Lénine//Staline//Molotov\n"
                       "La France//Le Portugal//L'Italie//L'Espagne\n"
                       "Vercingétorix//César//Attila//Auguste\n"
                       "Pedro Almodovar//Pablo Trapero//Guillermo del Toro//Woody Allen\n"
                       "UB40//Jim Morrison//Eric Clapton//Bob Marley\n"
                       "L'Allemagne//L'Italie//Le Brésil//L'Argentine\n"
                       "Venise//Vérone//Milan//Rome\n"
                       "Une marâtre//Une godiche//Une chenapan//Une jocrisse\n"
                       "Apollon//Hermès//Arès//Hadès\n"
                       "Le léopard//Le mgbobe//Le chevreuil//Le springbok\n"
                       "Feignons !//Feins !//Feignez !//Feindez !\n"
                       "Louis XIV//François Ier//Henri IV//Louis XIII\n"
                       "Virgile//Homère//Euripide//Sophocle\n"
                       "Léon Blum//Charles de Gaulle//Aristide Briand//Georges Clemenceau\n"
                       "Léonardo DiCaprio//Brad Pitt//Matthew MacConaughey//Tom Cruise\n"
                       "Le Rhône//La Loire//Le Rhin//La Seine\n"
                       "Rouge//Jaune//Vert//Noir\n"
                       "Libération//Le Monde//Le Figaro//Charlie Hebdo\n"
                       "Le lama//Le yak//Le chameau//Le buffle\n"
                       "John Barry//Vladimir Cosma//Hans Zimmer//Ennio Morricone")