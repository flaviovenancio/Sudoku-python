# Retorna a posição da próxima célula vazia
def procura_proximo_espaco(puzzle):
    for l in range(9):
        for c in range(9):
            if puzzle[l][c] == -1:
                return l, c
            
    # Retorna None se não houver células vazias        
    return None, None 

# Retorna False se o palpite já estiver na mesma linha
def valido(puzzle, adivinha, lin, col):
    lin_valor = puzzle[lin]
    if adivinha in lin_valor:
        return False

    # Retorna False se o palpite já estiver na mesma coluna 
    col_valor = [puzzle[i][col] for i in range(9)] 
    if adivinha in col_valor:
        return False
     
    lin_inicia = (lin // 3) * 3
    col_inicia = (col // 3) * 3

    # Retorna False se o palpite já estiver na mesma sub-grade de 3x3
    for l in range(lin_inicia, lin_inicia + 3):
        for c in range(col_inicia, col_inicia + 3):
            if puzzle[l][c] == adivinha:
                return False
    # Retorna True se o palpite for válido em relação à linha, coluna e sub-grade         
    return True

# Retorna True se o tabuleiro estiver completamente preenchido
def resolve_sudoku(puzzle):
    lin, col = procura_proximo_espaco(puzzle)

    if lin is None:
        return True
    
    # Atribui o palpite se for válido
    for adivinha in range(1, 10):
        if valido(puzzle, adivinha, lin, col):
            puzzle[lin][col] = adivinha
            

            # Retorna True se a solução for encontrada
            if resolve_sudoku(puzzle):
                return True
            
            # Reseta a célula se a solução não for encontrada
            puzzle[lin][col] = -1  

    # Retorna False se nenhuma solução for encontrada    
    return False

if __name__ == '__main__':
    exemplo_board = [
        [5, 3, -1, -1, 7, -1, -1, -1, -1],
        [6, -1, -1, 1, 9, 5, -1, -1, -1],
        [-1, 9, 8, -1, -1, -1, -1, 6, -1],
        [8, -1, -1, -1, 6, -1, -1, -1, 3],
        [4, -1, -1, 8, -1, 3, -1, -1, 1],
        [7, -1, -1, -1, 2, -1, -1, -1, 6],
        [-1, 6, -1, -1, -1, -1, 2, 8, -1],
        [-1, -1, -1, 4, 1, 9, -1, -1, 5],
        [-1, -1, -1, -1, 8, -1, -1, 7, 9],
    ]
    resolve_sudoku(exemplo_board)
    for linha in exemplo_board:
        # Imprime o sudoku resolvido
        print(linha)


    