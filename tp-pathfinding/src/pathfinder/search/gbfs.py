from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        
        # Inicializamos la frontera con el nodo raíz y su prioridad (distancia Manhattan)
        frontier = PriorityQueueFrontier()
        initial_priority = abs(root.state[0] - grid.end[0]) + abs(root.state[1] - grid.end[1])
        frontier.add(root, priority=initial_priority)

        while not frontier.is_empty():
            node = frontier.pop()

            # Test del objetivo al extraer de la frontera
            if grid.objective_test(node.state):
                return Solution(node, reached)

            # Generamos los sucesores (vecinos válidos)
            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
                cost = node.cost + grid.individual_cost(node.state, action)

                # Si el sucesor no fue alcanzado o encontramos un camino con menor costo
                if successor not in reached or cost < reached[successor]:
                    reached[successor] = cost
                    child = Node(
                        "",
                        state=successor,
                        cost=cost,
                        parent=node,
                        action=action,
                    )
                    
                    # Calculamos la prioridad heurística (distancia Manhattan al objetivo)
                    priority = abs(successor[0] - grid.end[0]) + abs(successor[1] - grid.end[1])
                    frontier.add(child, priority=priority)

        return NoSolution(reached)