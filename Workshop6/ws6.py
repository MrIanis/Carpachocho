import random

# Liste de mots possibles pour le jeu du pendu
f = open("mots.txt", "r", encoding="utf8")
choix = f.readlines()

# On choisit un mot au hasard dans la liste pour être la solution du jeu
solution = random.choice(choix)

tentatives = 7
lettres_trouvees =""

# On initialise une variable pour afficher le mot à deviner avec des underscores
affichage = ""

# On parcourt chaque lettre du mot solution
for l in solution:
  # On remplace chaque lettre du mot par un underscore
  affichage = affichage + "_ "

# On affiche un message de bienvenu
print("=> Bienvenu dans le jeu du pendu! <=\n")

while tentatives > 0:
  # On affiche le mot à deviner avec les lettres déjà trouvées
  print("\nMot à deviner : ", affichage)

  proposition = input("proposez une lettre : ")[0:1].lower()

  # Si la lettre proposée est dans le mot solution
  if proposition in solution:
      # On ajoute la lettre aux lettres déjà trouvées
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Oui!")
  else:
    # Sinon, on enlève une tentative au joueur
    tentatives = tentatives - 1
    print("-> Non\n")

    # On dessine le pendu en fonction du nombre de tentatives restantes (j'avoue je me suis un peu inspiré pour le dessin du pendu)
    if tentatives==0:
        print(" ==========Y= ")
    if tentatives<=1:
        print(" ||/       |  ")
    if tentatives<=2:
        print(" ||        0  ")
    if tentatives<=3:
        print(" ||       /|\ ")
    if tentatives<=4:
        print(" ||       /|  ")
    if tentatives<=5:
        print("/||           ")
    if tentatives<=6:
        print("==============\n")

  # On réinitialise la variable affichage
  affichage = ""

  # On parcourt chaque lettre du mot solution
  for x in solution:
      # Si la lettre est déjà trouvée, on l'affiche
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          # Sinon, on affiche un underscore
          affichage += "_ "

  if "_" not in affichage:
      print("=> Gagné! <=\n")
      break

print("\n    - Fin de la partie -    ")
print("La solution était :", solution)
