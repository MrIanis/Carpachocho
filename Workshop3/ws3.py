import random

def generate_board(n: int) -> dict[int, int]:
    """Génère un échiquier de n x n cases rempli par n reines placées aléatoirement

    Args:
        n (int): Nombre de dames

    Returns:
        dict: L'échiquier
    """
    max = n ** 2 
    board = {i: 0 for i in range(max)}
    placed_queens = 0

    while placed_queens < n:
        queen_index = random.randint(0, max - 1)
        if board[queen_index] == 0:
            board[queen_index] = 1
            placed_queens += 1

    return board

def get_queens_position(board: dict[int, int]) -> list[int]:
    """Renvoie les positions des dames sous forme d'un tableau"""
    return [item[0] for item in board.items() if item[1] == 1]

def grid_coords_to_list_index(row: int, col: int, n: int) -> int:
    """Convertit les coordonnées d'une grille en coordonnées aplaties"""
    return row * n + col

def list_index_to_grid_coords(x: int, n: int) -> tuple[int, int]:
    """Convertit une position dans le vecteur en coordonnées de grille"""
    return (x // n, x % n)

def get_reachable_positions(position: tuple[int, int], n: int) -> list[int]:
    """Renvoie toutes les positions atteignables par une reine à partir de la position donnée"""
    row, col = position
    coords = set()

    for i in range(n):
        # Même ligne et même colonne
        coords.add(grid_coords_to_list_index(row, i, n))
        coords.add(grid_coords_to_list_index(i, col, n))

        # Diagonales
        if row + i < n and col + i < n:
            coords.add(grid_coords_to_list_index(row + i, col + i, n))
        if row - i >= 0 and col - i >= 0:
            coords.add(grid_coords_to_list_index(row - i, col - i, n))
        if row + i < n and col - i >= 0:
            coords.add(grid_coords_to_list_index(row + i, col - i, n))
        if row - i >= 0 and col + i < n:
            coords.add(grid_coords_to_list_index(row - i, col + i, n))

    coords.discard(grid_coords_to_list_index(row, col, n))
    return list(coords)

def validate_board(board: dict[int, int], n: int) -> bool:
    queen_positions = get_queens_position(board)

    for queen in queen_positions:
        grid_coords = list_index_to_grid_coords(queen, n)
        reachable = get_reachable_positions(grid_coords, n)

        for pos in reachable:
            if board.get(pos, 0) == 1:
                return False

    return True

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


def print_board(board: dict[int, int], n: int):
    """Affiche l'échiquier sous forme de grille"""
    for i in range(n):
        row = ""
        for j in range(n):
            if board[grid_coords_to_list_index(i, j, n)] == 1:
                row += "Q "
            else:
                row += ". "
        print(row)

while True:
    board = generate_board(n)
    if validate_board(board, n):
        print_board(board, n)
        print("Cette configuration est correcte !")
        break
    else:
        print_board(board, n)
        print("Incorrect... Nouvelle tentative.")
