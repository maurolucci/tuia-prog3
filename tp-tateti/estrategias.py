"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)

def minimax_max(tateti: Tateti, estado: List[List[str]]) -> float:
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado)
    
    valor = float('-inf')
    for accion in tateti.acciones(estado):
        sucesor = tateti.resultado(estado, accion)
        valor = max(valor, minimax_min(tateti, sucesor))
    return valor

def minimax_min(tateti: Tateti, estado: List[List[str]]) -> float:
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado)
    
    valor = float('inf')
    for accion in tateti.acciones(estado):
        sucesor = tateti.resultado(estado, accion)
        valor = min(valor, minimax_max(tateti, sucesor))
    return valor

def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
    """
    jugador_actual = tateti.jugador(estado)
    acciones = tateti.acciones(estado)
    
    mejor_accion = None
    if jugador_actual == JUGADOR_MAX:
        mejor_valor = float('-inf')
        for accion in acciones:
            sucesor = tateti.resultado(estado, accion)
            valor = minimax_min(tateti, sucesor)
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_accion = accion
    else:
        mejor_valor = float('inf')
        for accion in acciones:
            sucesor = tateti.resultado(estado, accion)
            valor = minimax_max(tateti, sucesor)
            if valor < mejor_valor:
                mejor_valor = valor
                mejor_accion = accion
    
    return mejor_accion