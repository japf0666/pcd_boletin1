import pytest
from juego_n_en_raya import generar_tablero as gt

def test_generar_tablero():
    n = 4
    mov_jugador_1 = {0:[0,2], 1:[1], 2:[2]}
    mov_jugador_2 = {0:[1], 1:[0,2], 2:[0]}
    movimientos_jugadores=[mov_jugador_1, mov_jugador_2]

    t= gt(n, movimientos_jugadores)
    assert len(t) == n

    for f in t:
        assert len(f) == n

    # Imprimir el tablero para visualización.
    # usar la opción -s o --capture=no al ejecutar pytest para ver la salida
    # Ejemplo: pytest -s test_juego_n_en_raya.py
    for fila in t:
        print(fila)
