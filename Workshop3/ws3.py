# Pour l'ESGI - B3 Python
# Template afin de faciliter l'intégration de l'algorithme des N-Reines
#
# L'approche est naïve : on génère un échiquier de N x N cases rempli aléatoirement
# On calcule les positions possibles de chaque dame
# Et on s'assure qu'il n'y ait pas de conflit.
#
# Toutes les fonctions ne sont pas forcément utiles selon votre approche.
 
import random
 
def generate_board(n: int) -> dict[int, int]:
    """Génère un échiquier de n x n cases rempli par n reines
    placées aléatoirement
 
    Args:
        n (int): Nombre de dames
 
    Returns:
        dict: L'échiquier
    """
 
    # 
    max = n ** 2 
 
    # On remplit l'échiquier avec 25 cases
    # La structure résultant est un dictionnaire ayant ce format : 
    #   { 0: 0, 1: 0, 2: 0, 3: 0 ... jusqu'à 24: 0 }
    #
    # Le zéro en valeur signifie qu'il n'y a pas de dame sur cette case.
    # 
    # Voir le cours sur les compréhensions pour la syntaxe
    board = { i:0 for i in range(max) }
    
    placed_queens = 0
 
    # Tant que l'on a pas placé toutes les dames...
    while placed_queens < n:
        queen_index = random.randint(0, max - 1) # - 1 car randint inclus la borne supérieure, hors l'index max est 24 (on commence à zéro)
        if board[queen_index] == 0: # s'il n'y a pas de dame...
            board[queen_index] = 1  # ...on en place une.
            placed_queens += 1
 
    return board
 
 
def get_queens_position(board: dict[int,int]) -> list[int]:
    """
        Renvoie les positions des dames sous forme d'un tableau
        Par exemple, [1, 4, 13, 18, 22]
    """
    return [ item[0] for item in dict.items(board) if item[1] == 1 ]
 
def grid_coords_to_list_index(row: int, col: int, n: int) -> int:
    """
        Convertit les coordonnées d'une grille (avec ligne et colonne) et coordonnées aplaties
        Exemple avec n = 3 et 3 dames de placées aléatoirement
        
          0   1   2
        ┌──
      0   0 │ 1 │ 0           
         ───┼───┼───        index:   0  1  2  3  4  5  6  7  8
      1   0 │ 0 │ 1     -->        [ 0, 1, 0, 0, 0, 1, 1, 0, 0 ]
         ───┼───┼───                                   ^
      2   1 │ 0 │ 0
          ^        ──┘
 
        Nous avons une dame en colonne 0, ligne 2 par exemple, indiquée au-dessus du ^
        Elle correspond à la dame d'index 6 en mode liste
        Vérification la formule, avec row = 2 et col = 0
            row * n + col = 2 * 3 + 0 = 6
    """
 
    return row * n + col
 
def list_index_to_grid_coords(x: int, n: int) -> tuple[int, int]:
    """
        Fait précisement l'opération inverse de la méthode précédente.
        On part de la position dans le vecteur pour récupérer les coordonnées dans la grille.
 
        Pour la valeur de retour, CF les cours sur les tuples.
        On renvoie ici un vecteur (row, col) et les valeurs sont accessibles comme avec une liste : tuple[0] et tuple[1]
 
        Exemple pour n = 3 et x = 7
        row = x // n = 7 // 3 = 2  (résultat de la division entière)
        col = x % n = 7 % 3 = 1    (reste de la division entière)
    """
    return (x // n, x % n)
 
def get_reachable_positions(position: tuple[int, int], n: int) -> list[int]:
    """ A vous de bosser ici ! """
    coords = set()
    # TODO : l'algo
    return list(coords)
 
def validate_board(board: dict[int, int], n):
 
    queen_positions = get_queens_position(board)
    
    # Pour chaque dame...
    for queen in queen_positions:
        # on récupère ses coordonnées en grille (j, i)
        grid_coords = list_index_to_grid_coords(queen, n)
        # On récupère les mouvements possibles...
        reachable = get_reachable_positions(grid_coords, n)
 
        # Pour chaque mouvement possible...
        for pos in reachable:
            # On vérifie si une dame est déjà en place.
            if pos in queen_positions:
                return False
            
    # Aucune collision
    return False
 
 
# Nombre de dames
n = 5
 
# Répétez ce code jusqu'à générer une bonne position...
board = generate_board(n)
 
# Ou testez avec un échiquier qui fonctionne !
correct_board = {
    0:  0, 1:  1,  2: 0,  3: 0, 4:  0,
    5:  0, 6:  0,  7: 0,  8: 1, 9:  0,
    10: 1, 11: 0, 12: 0, 13: 0, 14: 0,
    15: 0, 16: 0, 17: 1, 18: 0, 19: 0,
    20: 0, 21: 0, 22: 0, 23: 0, 24: 1 
}
 
if validate_board(correct_board, n):
    print("Cette configuration est correcte !")
else:
    print("Incorrect...")