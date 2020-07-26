import statistics

#code

notes = [
    20, 5, 15,
    16, 12, 18,
]

print(notes)


result = statistics.mean(notes)

print("La moyenne de l'élève est {} !".format(result))
