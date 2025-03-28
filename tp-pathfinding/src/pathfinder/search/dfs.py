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
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        #Test-Objetivo
        if node.state == grid.end:
            return Solution(node, explored)
            
        frontier = StackFrontier()
        frontier.add(node)

        while True:

            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored)
            # Remove a node from the frontier
            node = frontier.remove()
            

            if node.state in explored:
                continue
            explored[node.state]=True
            successors = grid.get_neighbours(node.state)

            for action, result in successors.items():  
                new_state = result  # Obtener el nuevo estado


                # Check if the successor is not reached
                if new_state not in explored:

                        # Initialize the son node
                    new_node = Node("", new_state,
                                        node.cost + grid.get_cost(new_state),
                                        parent=node,action=action)
                        # Mark the successor as reached
                    #explored[new_state] = True

                    # Return if the node contains a goal state
                    if new_state == grid.end:
                        return Solution(new_node, explored)
                
                  
                    # Add the new node to the frontier
                    frontier.add(new_node)
