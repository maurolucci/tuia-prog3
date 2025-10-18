from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    def heuristic(state, goal):
        x1, y1 = state
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)
    
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

        frontier = PriorityQueueFrontier()
        h_root = GreedyBestFirstSearch.heuristic(root.state, grid.end)
        frontier.add(root, priority=h_root)

        while not frontier.is_empty():
            node = frontier.pop()

            if grid.objective_test(node.state):
                return Solution(node, reached)

            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
                new_cost = node.cost + grid.individual_cost(node.state, action)

                if successor not in reached or new_cost < reached[successor]:
                    child = Node(
                        "",
                        state=successor,
                        cost=new_cost,
                        parent=node,
                        action=action,
                    )
                    reached[successor] = new_cost
                    h_child = GreedyBestFirstSearch.heuristic(successor, grid.end)
                    frontier.add(child, priority=h_child)

        return NoSolution(reached)
