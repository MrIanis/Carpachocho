import random

def devine():
    nombre = random.randint(1, 100)
    print("Je pense à un nombre entre 1 et 100. Devine-le.")
    devine = 0
    while devine != nombre:
        devine = int(input())
        if devine < nombre:
            print("Plus grand")
        elif devine > nombre:
            print("Plus petit")
    print
    print("Bravo! Tu as deviné le nombre.")
    print

devine()

