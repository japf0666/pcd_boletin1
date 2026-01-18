# juego de las tres en raya.

fichas= ['o','x']

def generar_tablero(n, movimientos_jugadores):
    tablero=[]
    for i in range(n):
        fila=['_' for i in range(n)]
        for j in range(n):
            casilla_vacia = True
            for k in range(len(movimientos_jugadores)):
                movimientos_jugador= movimientos_jugadores[k]
                if i in movimientos_jugador:
                    if j in movimientos_jugador[i]:
                        fila[j]=fichas[k]
        tablero.append(fila)
    return tablero

##########################################################################
import pytest

def test_generar_tablero():
    mov_jugador_1 = {}
    mov_jugador_2 = {}
    movimientos_jugadores=[mov_jugador_1, mov_jugador_2]
    n=3

    t= generar_tablero(n, movimientos_jugadores)
    assert len(t) == n

    for f in t:
        assert len(f) == n

def prueba_tablero_vacío():
    mov_jugador_1 = {}
    mov_jugador_2 = {}
    movimientos_jugadores=[mov_jugador_1, mov_jugador_2]
    n=3

    t= generar_tablero(n, movimientos_jugadores)
    esperado= [['_','_','_'],
               ['_','_','_'],
               ['_','_','_']]
    assert t == esperado
    print(t, len(t))

def prueba_simple():
    mov_jugador_1 = {0:[0,2], 1:[1], 2:[2]}
    mov_jugador_2 = {0:[1], 1:[0,2], 2:[0]}
    movimientos_jugadores=[mov_jugador_1, mov_jugador_2]
    n=3

    t= generar_tablero(n, movimientos_jugadores)
    esperado= [['o','x','o'],
               ['x','o','x'],
               ['x','_','o']]
    assert t == esperado
    print(t, len(t))

n=3

"""
Método que comprueba que un movimiento de un jugador es válido
* x: fila donde el jugador quiere colocar la ficha.
* y: columna donde el jugador quiere colocar su ficha.
* movimientos_otro_jugador: listado con las celdas ocupadas por el otro jugador.
"""
def movimiento_valido(x, y, movimientos_otro_jugador):
    if x > n or y > n:
       return False
    if x in movimientos_otro_jugador:
        movimientos_en_columna= movimientos_otro_jugador[x]
        if y in movimientos_en_columna:
            return False
    return True 

def test_movimiento_columna_fuera_tablero():
    movimientos_otro_jugador= {}
    x = 1
    y = 4
    assert movimiento_valido(x, y, movimientos_otro_jugador) == False

def test_movimiento_fila_y_columna_fuera_tablero():
    movimientos_otro_jugador= {}
    x = 4
    y = 4
    assert movimiento_valido(x, y, movimientos_otro_jugador) == False

def test_movimiento_incorrecto():
    movimientos_otro_jugador= {2:[3]}
    x = 2
    y = 3
    assert movimiento_valido(x, y, movimientos_otro_jugador) == False

def jugada_ganadora(movimientos_jugador):
    """
    Método que permite determinar si los movimientos de un jugador le permite ganar una partida.
    Parámetros:
    * movimientos_jugador: dict con el conjunto de movimientos de un jugador
    """
    #Comprobamos si hay 3 fichas en una fila
    for fila in movimientos_jugador:
        if len(movimientos_jugador[fila]) >= 3:
            return True
    return False

def test_no_ganador():
   movimientos_jugador={2:[2,3]}
   assert False == jugada_ganadora(movimientos_jugador)

def test_ganador():
   movimientos_jugador={2:[1,2,3]}
   assert True == jugada_ganadora(movimientos_jugador)

prueba_tablero_vacío()
prueba_simple()
#t= generar_tablero(n, movimientos_jugadores)
#print(t, len(t))