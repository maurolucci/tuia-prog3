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

        # Initialize frontier with the root node
        frontier = QueueFrontier()
        frontier.add(root)

        if grid.objective_test(root.state):
            return Solution(root, reached)

        while not frontier.is_empty():
            node = frontier.remove()

            for action in grid.actions(node.state):
                successor_state = grid.result(node.state, action)

                if successor_state not in reached:
                    cost = node.cost + grid.individual_cost(node.state, action)
                    child = Node("", state=successor_state, cost=cost,parent=node,action=action)

                    reached[successor_state] = True

                    if grid.objective_test(child.state):
                        return Solution(child, reached)

                    frontier.add(child)

        return NoSolution(reached)
