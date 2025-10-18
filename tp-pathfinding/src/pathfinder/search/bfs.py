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
        reached[root.state] = root

        # Initialize frontier with the root node
        frontier = QueueFrontier()
        frontier.add(root)

        # Main loop
        while not frontier.is_empty():
            current_node = frontier.remove()
            current_state = current_node.state

            # Check if we reached the goal
            if grid.objective_test(current_state):
                return Solution(current_node, reached)

            # Expand node
            for action in grid.actions(current_state):
                next_state = grid.result(current_state, action)

                if next_state not in reached:
                    cost = current_node.cost + grid.individual_cost(current_state, action)
                    next_node = Node(
                        value="",
                        state=next_state,
                        cost=cost,
                        parent=current_node,
                        action=action
                    )
                    reached[next_state] = next_node
                    frontier.add(next_node)

        # No solution found
        return NoSolution(reached)

