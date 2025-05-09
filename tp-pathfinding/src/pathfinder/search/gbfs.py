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
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {}

        # Add the node to the explored dictionary
        explored[node.state] = node.cost

        # Initialize the frontier with the initial node
        # In this example, the frontier is a priority queue
        frontier = PriorityQueueFrontier()
        frontier.add(node, grid.manhattan_distance(node.state, grid))

        while True:
            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored)

            # Remove a node from the frontier
            node = frontier.pop()

            # Return if the node contains a goal state
            # In this example, the goal test is run
            # before adding a new node to the frontier
            if node.state == grid.end:
                return Solution(node, explored)

            # print(f'node.state: {node.state}')
            # print(f'grid.end: {grid.end}')

            # GBFS
            successors = grid.get_neighbours(node.state)
            for neighbour in successors:
                new_state = successors[neighbour]
                cost = node.cost + grid.get_cost(new_state)

                # print(f'node.cost: {node.cost}')
                # print(f'get cost de node.state: {grid.get_cost(node.state)}')
                # print(f'get cost de new_state: {grid.get_cost(new_state)}')
                # print(f'Cost: {cost}')

                if new_state not in explored or cost < explored[new_state]:
                    new_node = Node("",
                                    new_state,
                                    cost,
                                    parent=node,
                                    action=neighbour)
                    explored[new_state] = cost
                    frontier.add(new_node, grid.manhattan_distance(new_node.state, grid))




        return NoSolution(explored)

# GBFS VS DFS
# function GRAPH-GBFS(problema,h) return solución o fallo
#     n₀ ← NODO(problema.estado-inicial, None, None, 0)
#     alcanzados ← {n₀.estado: n₀.costo}    => AGREGA EL COSTO
#     frontera ← ColaPrioridad()    => ESTO CAMBIA A PILA
#     frontera.encolar(n₀, h(n₀))   => ESTO NO INICIA VACIO
#     do
#         if frontera.vacía() then return fallo
#         n ← frontera.desencolar()
#         if problema.test-objetivo(n.estado) then return solución(n)   => ESTO ESTA MUCHO MAS ABAJO,
                                                                        #    LO SUBE
#         forall a in problema.acciones(n.estado) do
#             s’ ← problema.resultado(n.estado, a)
#             c’ ← n.costo + problema.costo-individual(n.estado,a)  => ESTO ES NUEVO

#       HASTA ACA ESTARIA
#             if s’ is not in alcanzados or c’ < alcanzados[s’] then    => ESTO NUEVO

#                 n’ ← Nodo(s’, n, a, c’)   => ESTO CAMBIA
#                 alcanzados[s’] ← c’       => ESTO?
#                 frontera.encolar(n’, h(n’))


