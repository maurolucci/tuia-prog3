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
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        
        # Initialize the frontier with the initial node
        frontier = QueueFrontier()
        frontier.add(node)

        while True:
            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored)

            # Remove a node from the frontier
            node = frontier.remove()

            # Mark the node as explored
            explored[node.state] = True
            # Return if the node contains a goal state
            if node.state == grid.end:
                return Solution(node, explored)

            # Go right
            neighbours = grid.get_neighbours(node.state)
            for k,n in neighbours.items(): 
                if n not in explored:
                    new_node = Node("", n, node.cost + grid.get_cost(n))
                    new_node.parent = node
                    new_node.action = k
                    frontier.add(new_node)
                    explored[n] = True    
