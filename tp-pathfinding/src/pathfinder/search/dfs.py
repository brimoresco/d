from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:

    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth-First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", state=grid.start, cost=0, parent=None, action=None)

        # Initialize the reached dictionary with the initial state
        reached = {}
        #reached[node.state] = True

        # Return if the node contains a goal state
        if node.state == grid.end:
            return Solution(node, reached)

        # Initialize the frontier with the initial node
        # In this example, the frontier is a stack
        frontier = StackFrontier()
        frontier.add(node)

        while True:
            # Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(reached)

            # Remove a node from the frontier (stack)
            node = frontier.remove()
            if node.state in reached: 
                continue
            # Explore vecinos in a depth-first manner
            reached[node.state] = True
            successors = grid.get_neighbours(node.state)
            for action, new_state in successors.items():
                if new_state not in reached:
                    # Initialize the child node
                    new_node = Node("", new_state,
                                    node.cost + grid.get_cost(new_state),
                                    parent=node, action=action)

                    # Mark the successor as reached
                    

                    # Return if the node contains a goal state
                    if new_state == grid.end:
                        return Solution(new_node, reached)

                    # Add the new node to the frontier (stack)
                    frontier.add(new_node)
