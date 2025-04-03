from ..models.grid import Grid
from ..models.frontier import StackFrontier
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
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        frontier = PriorityQueueFrontier()
        frontier.add(node,node.cost)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = node.cost

        while True:
            if frontier.is_empty():
                return NoSolution(explored)
            # Remove a node from the frontier
            node = frontier.pop()
            if node.state == grid.end:
                return Solution(node, explored)
            successors = grid.get_neighbours(node.state)

            
            for action, result in successors.items():  # Suponiendo que successors es un diccionario
                new_state = result
                cost_new_state=node.cost+ grid.get_cost(new_state)
                
                if new_state not in explored or cost_new_state<explored[new_state]:
                     # Initialize the son node
                    new_node = Node("", new_state,
                                    cost_new_state,
                                    parent=node,action=action)
                    
                    explored[new_state] = cost_new_state

                    frontier.add(new_node,cost_new_state)


        
        
