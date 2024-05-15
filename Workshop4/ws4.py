import string

# Définir le texte à analyser
texte = "afrgthykighlompfdshygtfghygjkhlfdkshygtfhybgjukilofm"

# Supprimer les ponctuations et convertir le texte en minuscules
texte_nettoye = texte.translate(str.maketrans("", "", string.punctuation)).lower().replace(" ", "")

# Créer un dictionnaire pour stocker les fréquences des lettres
frequences = {}

# Calculer les fréquences des lettres
for lettre in texte_nettoye:
    if lettre in frequences:
        frequences[lettre] += 1
    else:
        frequences[lettre] = 1

# Demander à l'utilisateur de choisir l'ordre d'affichage
tri = input("Choisissez l'ordre d'affichage (A pour alphabétique, F pour fréquence): ")

# Trier le dictionnaire selon l'ordre choisi
if tri.upper() == "A":
    frequences_triees = dict(sorted(frequences.items()))
else:
    frequences_triees = dict(sorted(frequences.items(), key=lambda x: x[1], reverse=True))

# Trouver la fréquence maximale
freq_max = max(frequences_triees.values())

# Afficher les résultats
for lettre, freq in frequences_triees.items():
    print(lettre, "|", "■" * int((freq / freq_max) * 40), "|", freq)
