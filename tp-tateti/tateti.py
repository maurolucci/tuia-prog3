"""
Módulo para la formulación del juego del Tateti (Tic-Tac-Toe)

Estados: Matriz 3x3 con "X", "O" y "-" (casilla vacía)
Acciones: Par ordenado (fila, columna)
Jugadores: "MAX" (X) y "MIN" (O)
Utilidad: 1 (gana), 0 (pierde), 0.5 (empate)
"""

import copy
from typing import List, Tuple, Optional

# Constantes del juego
JUGADOR_MAX = "X"
JUGADOR_MIN = "O"
CASILLA_VACIA = "-"


class Tateti:
    """Clase que encapsula toda la lógica del juego Tateti"""
    
    def __init__(self):
        """Inicializa el juego con el estado inicial"""
        self.estado_inicial = [[CASILLA_VACIA for _ in range(3)] for _ in range(3)]

    def jugador(self, estado: List[List[str]]) -> str:
        """
        Determina qué jugador debe mover en el estado dado.
        
        En tateti, MAX (X) siempre empieza. Contamos las fichas para determinar
        el turno actual.
        
        Args:
            estado: Estado actual del tablero
            
        Returns:
            str: JUGADOR_MAX si es turno de MAX, JUGADOR_MIN si es turno de MIN
        """
        contador_x = sum(fila.count(JUGADOR_MAX) for fila in estado)
        contador_o = sum(fila.count(JUGADOR_MIN) for fila in estado)
        
        # Si hay más X que O, es turno de MIN
        # Sino, es turno de MAX
        return JUGADOR_MIN if contador_x > contador_o else JUGADOR_MAX

    def acciones(self, estado: List[List[str]]) -> List[Tuple[int, int]]:
        """
        Retorna todas las acciones posibles en el estado dado.
        
        Args:
            estado: Estado actual del tablero
            
        Returns:
            List[Tuple[int, int]]: Lista de pares (fila, columna) de casillas vacías
        """
        acciones_posibles = []
        for fila in range(3):
            for columna in range(3):
                if estado[fila][columna] == CASILLA_VACIA:
                    acciones_posibles.append((fila, columna))
        return acciones_posibles

    def resultado(self, estado: List[List[str]], accion: Tuple[int, int]) -> List[List[str]]:
        """
        Retorna el estado resultante de aplicar la acción al estado dado.
        
        Args:
            estado: Estado actual del tablero
            accion: Par (fila, columna) donde colocar la ficha
            
        Returns:
            List[List[str]]: Nuevo estado después de aplicar la acción
            
        Raises:
            ValueError: Si la acción no es válida
        """
        fila, columna = accion
        
        # Validar que la acción sea válida
        if not (0 <= fila < 3 and 0 <= columna < 3):
            raise ValueError(f"Acción inválida: {accion}. Debe estar en rango [0,2]")
        
        if estado[fila][columna] != CASILLA_VACIA:
            raise ValueError(f"Casilla ({fila}, {columna}) ya está ocupada")
        
        # Crear nuevo estado
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[fila][columna] = self.jugador(estado)
        
        return nuevo_estado

    def test_terminal(self, estado: List[List[str]]) -> bool:
        """
        Determina si el estado es terminal (juego terminado).
        
        Un estado es terminal si:
        1. Hay un ganador (tres en línea)
        2. No hay un ganador y el tablero está lleno (empate)
        
        Args:
            estado: Estado del tablero a evaluar
            
        Returns:
            bool: True si el juego terminó, False si continúa
        """
        # Verificar si hay ganador
        if self._hay_ganador(estado) is not None:
            return True
        
        # Verificar si el tablero está lleno
        return all(casilla != CASILLA_VACIA 
                  for fila in estado 
                  for casilla in fila)

    def utilidad(self, estado: List[List[str]], jugador: str = JUGADOR_MAX) -> float:
        """
        Calcula la utilidad de un estado terminal desde la perspectiva del jugador especificado.
        
        Args:
            estado: Estado terminal del juego
            jugador: Jugador desde cuya perspectiva calcular la utilidad (por defecto JUGADOR_MAX)
            
        Returns:
            float: 1.0 si el jugador gana, 0.0 si el jugador pierde, 0.5 si empate
            
        Raises:
            ValueError: Si el estado no es terminal
        """
        if not self.test_terminal(estado):
            raise ValueError("No se puede calcular utilidad en estado no terminal")
        if jugador not in (JUGADOR_MAX, JUGADOR_MIN):
            raise ValueError(f"Jugador inválido: {jugador}")
        
        ganador = self._hay_ganador(estado)
        
        if ganador == jugador:
            return 1.0
        elif ganador is not None and ganador != jugador:
            return 0.0
        else:
            return 0.5  # Empate

    def _hay_ganador(self, estado: List[List[str]]) -> Optional[str]:
        """
        Función auxiliar para verificar si hay un ganador.
        
        Args:
            estado: Estado del tablero
            
        Returns:
            Optional[str]: El jugador ganador ("X" o "O") o None si no hay ganador
        """
        # Verificar filas
        for fila in estado:
            if fila[0] == fila[1] == fila[2] != CASILLA_VACIA:
                return fila[0]
        
        # Verificar columnas
        for col in range(3):
            if estado[0][col] == estado[1][col] == estado[2][col] != CASILLA_VACIA:
                return estado[0][col]
        
        # Verificar diagonales
        if estado[0][0] == estado[1][1] == estado[2][2] != CASILLA_VACIA:
            return estado[0][0]
        
        if estado[0][2] == estado[1][1] == estado[2][0] != CASILLA_VACIA:
            return estado[0][2]
        
        return None

    def mostrar_tablero(self, estado: List[List[str]]) -> str:
        """
        Función auxiliar para mostrar el tablero de forma legible.
        
        Args:
            estado: Estado del tablero
            
        Returns:
            str: Representación visual del tablero
        """
        resultado = "\n  0   1   2\n"
        for i, fila in enumerate(estado):
            resultado += f"{i} "
            for j, casilla in enumerate(fila):
                resultado += f" {casilla} "
                if j < 2:
                    resultado += "|"
            resultado += "\n"
            if i < 2:
                resultado += "  -----------\n"
        return resultado


