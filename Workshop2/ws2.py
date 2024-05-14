import random

def tri_tableau(tableau):
    return sorted(tableau)

def recherche_dichotomique(tableau, entier):
    tableau_trie = tri_tableau(tableau)
    debut = 0
    fin = len(tableau_trie) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        if tableau_trie[milieu] == entier:
            return milieu
        elif tableau_trie[milieu] < entier:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1

def main():
    tableau = [5, 3, 8, 1, 6, 2, 9, 7, 4]
    entier = 6

    tableau = tri_tableau(tableau)
    print("Tableau trié :", tableau)

    position = recherche_dichotomique(tableau, entier)

    if position != -1:
        print("L'entier", entier, "a été trouvé à la position", position)
    else:
        print("L'entier", entier, "n'a pas été trouvé dans le tableau")

if __name__ == "__main__":
    main()