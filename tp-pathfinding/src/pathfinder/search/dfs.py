from ..models.grid import Grid
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
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Apply objective test to the root
        if grid.objective_test(root.state):
            return Solution(root, dict())

        # Initialize frontier with the root node
        frontier = StackFrontier()
        frontier.add(root)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        while True:
            # Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(expanded)

            # Remove a node from the frontier
            node = frontier.remove()

            # Skip the node if its state was already expanded
            if node.state in expanded:
                continue

            # Mark the node as expanded
            expanded[node.state] = True

            # Expand the node: consider every possible action
            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)

                # Skip already expanded states
                if successor not in expanded:
                    # Initialize the child node
                    child = Node(
                        "",
                        successor,
                        cost=node.cost + grid.individual_cost(node.state, action),
                        parent=node,
                        action=action,
                    )

                    # Apply objective test
                    if grid.objective_test(successor):
                        return Solution(child, expanded)

                    # Add the child node to the frontier
                    frontier.add(child)
