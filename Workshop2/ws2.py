def tri_tableau(tableau):
    return sorted(tableau)

def recherche_dichotomique(tableau, entier):
    debut = 0
    fin = len(tableau) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        if tableau[milieu] == entier:
            return milieu
        elif tableau[milieu] < entier:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1