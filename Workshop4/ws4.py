import string

# Définissez le texte à analyser
texte = "afrgthykighlompfdshygtfghygjkhlfdkshygtfhybgjukilofm"

# Supprimez les ponctuations et convertissez le texte en minuscules
texte_nettoye = texte.translate(str.maketrans("", "", string.punctuation)).lower().replace(" ", "")

# Créez un dictionnaire pour stocker les fréquences des lettres
frequences = {}

# Calculez les fréquences des lettres
for lettre in texte_nettoye:
    if lettre in frequences:
        frequences[lettre] += 1
    else:
        frequences[lettre] = 1

# Trouvez la fréquence maximale
freq_max = max(frequences.values())

# Affichez les résultats
for lettre, freq in frequences.items():
    print(lettre, "|", "■" * int((freq / freq_max) * 40), "|", freq)
