from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Si la raiz es el objetivo
        if grid.objective_test(root.state):
            return Solution(root, reached)

        # Initialize frontier with the root node
        frontier = QueueFrontier()
        frontier.add(root)

        # Loop principal
        while not frontier.is_empty():
            node = frontier.remove() # Extraer el nodo mas antiguo
            
            # Expandir nodo
            for action in grid.actions(node.state):
                # Guardar estado resultante
                new_state = grid.result(node.state, action)
                # Si el nodo no estaba alcanzado lo guardo
                if new_state not in reached:
                    reached[new_state] = True
                    new_cost = node.cost + grid.individual_cost(node.state, action)
                    new_node = Node("", state=new_state, cost=new_cost, parent=node, action=action)
                # Probar si el nuevo nodo es el objetivo
                    if grid.objective_test(new_state):
                        return Solution(new_node, reached)
                # Si no lo es, lo agrego a la frontera
                    frontier.add(new_node)

            
        # Si la frontera se vacia sin encontrar objetivo, no hay solucion
        return NoSolution(reached)
