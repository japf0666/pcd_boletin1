from . import juego_n_en_raya as jnr
import pytest

def test_generar_tablero():
    n = 4
    mov_jugador_1 = {0:[0,2], 1:[1], 2:[2]}
    mov_jugador_2 = {0:[1], 1:[0,2], 2:[0]}
    movimientos_jugadores=[mov_jugador_1, mov_jugador_2]

    t= jnr.generar_tablero(n, movimientos_jugadores)
    assert len(t) == n

    for f in t:
        assert len(f) == n

    # Imprimir el tablero para visualización
    for fila in t:
        print(fila)
