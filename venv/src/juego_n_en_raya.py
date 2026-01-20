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
import os
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

def mostrar_tablero(tablero):
    """
    Método que muestra el estado actual del tablero
    Parámetros:
    * tablero: dict con el tablero a mostrar
    """
    for fila in tablero:
        for celda in fila:
            print(celda,end='')
        print('\n')

def movimiento_valido(x, y, n, posiciones_otro_jugador) -> bool:
    # Comprobamos que la posición está dentro del tablero
    if x >= n or y >= n or x < 0 or y < 0:
       return False
    
    # Comprobamos que la posición no ya está ocupada por el otro jugador
    if x in posiciones_otro_jugador:
        movimientos_en_columna = posiciones_otro_jugador[x]
        if y in movimientos_en_columna:
            return False
    return True 

def jugada_ganadora(n, posiciones_jugador) -> bool:
    """
    Método que permite determinar si los movimientos de un jugador 
    le permite ganar una partida.
    Comprobar si hay 3 fichas en una fila, columna o diagonal.
    """

    # Codificamos las posiciones del jugador en un array bidimensional
    # de n x n con valores booleanos, siendo True las posiciones ocupadas
    # por el jugador.
    tablero = [[False] * n for _ in range(n)]
    for fila in posiciones_jugador:
        for col in posiciones_jugador[fila]:
            tablero[fila][col] = True

    # Comprobamos filas y columnas
    for i in range(n):
        if all(tablero[i][j] for j in range(n)):
            return True
        if all(tablero[j][i] for j in range(n)):
            return True

    # Comprobamos diagonales
    if all(tablero[i][i] for i in range(n)):
        return True

    return False

#################################################################################
# datos iniciales del juego.
n = 3
casillas_libres = n*n
jugador_activo = 0
movimientos_jugador_1 = {}
movimientos_jugador_2 = {}
movimientos_jugadores = [movimientos_jugador_1, movimientos_jugador_2]
tablero = []
end_game= False


def init_juego() -> int:
    m =int(input('Introduce el tamaño del tablero cuadrado:'))
    casillas_libres = m*m
    tablero = generar_tablero(m,movimientos_jugadores)
    mostrar_tablero(tablero)
    return m
###############################################################################
# Código de prueba

import pytest
def test_generar_tablero(n = 4):
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

def test_movimiento_columna_fuera_tablero(n= 4):
    movimientos_otro_jugador= {}
    x = 1
    y = 4
    assert movimiento_valido(x, y, n, movimientos_otro_jugador) == False

def test_movimiento_fila_y_columna_fuera_tablero(n = 4):
    movimientos_otro_jugador= {}
    x = n
    y = n
    assert movimiento_valido(x, y, n,movimientos_otro_jugador) == False

def test_movimiento_incorrecto(n = 4):
    movimientos_otro_jugador= {2:[3]}
    x = 2
    y = 3
    assert movimiento_valido(x, y, n, movimientos_otro_jugador) == False

def test_jugada_ganadora(n=4):
    movimientos_jugador= {1:[0,1,2,3]}
    assert jugada_ganadora(n, movimientos_jugador) == True
    movimientos_jugador= {1:[0,1,2,3]}
    assert jugada_ganadora(n, movimientos_jugador) == True
    movimientos_jugador= {0:[2], 1:[2], 2:[2], 3:[2]}
    assert jugada_ganadora(n, movimientos_jugador) == True
    movimientos_jugador= {0:[0], 1:[1], 2:[2], 3:[3]}
    assert jugada_ganadora(n, movimientos_jugador) == True

def test_jugada_no_ganadora(n = 4):
    movimientos_jugador= {0:[0,1], 1:[1,2], 2:[2]}
    assert jugada_ganadora(n, movimientos_jugador) == False

###############################################################################

# inicializamos el juego
n = init_juego()

while casillas_libres > 0 and not end_game:

    # solicitamos movimiento al jugador activo
    casilla_jugador = input(f"JUGADOR {jugador_activo+1}: \
                            Introduce movimiento (x,y): ")
    # procesamos la entrada
    casilla_jugador= casilla_jugador.strip()
    x= int(casilla_jugador.split(',')[0])-1
    y= int(casilla_jugador.split(',')[1])-1

    print(casilla_jugador,x,y)

    # Comprobamos si el movimiento es válido
    if movimiento_valido(x,y, n, movimientos_jugadores[(jugador_activo+1)%2]):
        # Añadimos la posición resultante al jugador activo
        mov_col= movimientos_jugadores[jugador_activo].get(x,[])
        mov_col.append(y)
        movimientos_jugadores[jugador_activo][x]= mov_col

        # Recomponemos el tablero con el nuevo movimiento.
        tablero = generar_tablero(n,movimientos_jugadores)

        # Mostramos el tablero actualizado
        clear = lambda: os.system('cls')
        clear()
        mostrar_tablero(tablero)

        # Comprobamos si el jugador activo ha ganado
        if jugada_ganadora(n, movimientos_jugadores[jugador_activo]):
            print(F"ENHORABUENA EL JUGADOR {jugador_activo+1} HA GANADO")
            end_game= True
    else:
        frequency = 2000 # Set Frequency To 2500 Hertz
        duration = 1000 # Set Duration To 1000 ms == 1 second
        print('\a')
        print("Movimiento invalido. Turno para el siguiente jugador")

    # Actualizamos las variables del juego
    if not end_game:
        casillas_libres= casillas_libres -1
        jugador_activo = (jugador_activo+1) % 2

