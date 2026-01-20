# versión n en raya

fichas= ['o','x']

# vamos a modelar el tablero como una matriz de n x n caracteres
# donde cada casilla puede tener los valores:
# '_' casilla vacía 
# 'o' ficha del jugador 1
# 'x' ficha del jugador 2

# Las posiciones de los jugadores acumuladas durante la partida
# se representan como un diccionario de listas
# donde la clave es la fila y el valor es la lista de columnas
# ocupadas en esa fila por el jugador
# Ejemplo:
# jugador_1 = {0:[0,2], 1:[1], 2:[2]}
# jugador_2 = {0:[1], 1:[0,2], 2:[0]}
from typing import List
def generar_tablero(n, posiciones_jugadores) -> List[List[str]]:
    tablero= []
    for i in range(n):
        fila= ['_'] * n
        for k in range(len(posiciones_jugadores)):
            movimientos_jugador= posiciones_jugadores[k]
            if i in movimientos_jugador:
                columnas= movimientos_jugador[i]
                for j in columnas:
                    fila[j]= fichas[k]
        tablero.append(fila)
    return tablero


def test_generar_tablero():
    n = 4
    mov_jugador_1 = {0:[0,2], 1:[1], 2:[2]}
    mov_jugador_2 = {0:[1], 1:[0,2], 2:[0]}
    movimientos_jugadores=[mov_jugador_1, mov_jugador_2]

    t= generar_tablero(n, movimientos_jugadores)
    assert len(t) == n

    for f in t:
        assert len(f) == n

    # Imprimir el tablero para visualización
    for fila in t:
        print(fila)

t = generar_tablero(4, [{0:[0,2], 1:[1], 2:[2]}, {0:[1], 1:[0,2], 2:[0]}])
for fila in t:
        print(fila)