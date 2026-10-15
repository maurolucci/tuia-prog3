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

        # Apply objective test to the root
        if grid.objective_test(root.state):
            return Solution(root, reached)

        # Initialize frontier with the root node
        frontier = QueueFrontier()
        frontier.add(root)

        while True:
            # Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(reached)

            # Remove a node from the frontier
            node = frontier.remove()

            # Expand the node: consider every possible action
            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)

                # Skip already reached states
                if successor in reached:
                    continue

                # Initialize the child node
                child = Node(
                    "",
                    successor,
                    cost=node.cost + grid.individual_cost(node.state, action),
                    parent=node,
                    action=action,
                )

                # Mark the successor as reached
                reached[successor] = True

                # Apply objective test
                if grid.objective_test(successor):
                    return Solution(child, reached)

                # Add the child node to the frontier
                frontier.add(child)
