import random

def devine():
    nombre = random.randint(1, 100)
    print("Je pense à un nombre entre 1 et 100. Devine-le.")
    devine = 0
    while devine != nombre:
        devine = int(input())
        if devine < nombre:
            if nombre - devine > 10:
                print("Tu gèles")
            elif nombre - devine > 5:
                print("Tu refroidis")
            else:
                print("Tu chauffes")
        elif devine > nombre:
            if devine - nombre > 10:
                print("Tu gèles")
            elif devine - nombre > 5:
                print("Tu refroidis")
            else:
                print("Tu chauffes")
    print("Bravo! Tu as deviné le nombre.")
    print()

devine()