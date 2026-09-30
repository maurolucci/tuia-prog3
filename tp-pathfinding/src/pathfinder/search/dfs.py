from ..models.grid import Grid
#Importamos StackFrontier, que es una pila (LIFO: Last In, First Out)
# A diferencia de BFS que usa una cola (FIFO), la pila hace que DFS explore a lo profundo primero
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        expanded = dict()

        # Inicializamos la frontera como una Pila (Stack)
        frontier = StackFrontier()
        frontier.add(root)

        #Bucle principal: se ejecuta mientras haya nodos pendientes por explorar
        while not frontier.is_empty():
            node = frontier.remove()

            if node.state in expanded:
                continue

            # Marcamos el estado del nodo actual como expandido guardándolo en el diccionario
            expanded[node.state] = node

            #Test del objetivo: ¿Llegamos a la meta?
            if grid.objective_test(node.state):
            #Si llegamos, retornamos la Solución con el nodo final y la lista de explorados
                return Solution(node, expanded)

            #Generamos los sucesores (vecinos válidos) del nodo actual
            for action in grid.actions(node.state):
                #Obtenemos las coordenadas resultantes al aplicar la acción ("up", "down", etc.)
                successor = grid.result(node.state, action)

                # Si el vecino no fue expandido todavía, lo procesamos
                if successor not in expanded:

                    # Calculamos el costo acumulado usando la función oficial de la cátedra
                    cost = node.cost + grid.individual_cost(node.state, action)

                    # Creamos el nuevo nodo hijo vinculándolo a su padre (node)
                    child = Node(
                        "",
                        state=successor,
                        cost=cost,
                        parent=node,
                        action=action,
                    )
                    frontier.add(child)

        return NoSolution(expanded)