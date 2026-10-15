from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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

        # Initialize frontier with the root node, ordered by accumulated cost
        frontier = PriorityQueueFrontier()
        frontier.add(root, priority=root.cost)

        while True:
            # Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(reached)

            # Remove the node with the lowest accumulated cost
            node = frontier.pop()

            # Apply objective test
            if grid.objective_test(node.state):
                return Solution(node, reached)

            # Expand the node: consider every possible action
            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
                new_cost = node.cost + grid.individual_cost(node.state, action)

                # Skip states already reached with an equal or lower cost
                if successor not in reached or new_cost < reached[successor]:
                    reached[successor] = new_cost

                    child = Node(
                        "",
                        successor,
                        cost=new_cost,
                        parent=node,
                        action=action,
                    )

                    frontier.add(child, priority=new_cost)
