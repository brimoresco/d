from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search (UCS)

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", state=grid.start, cost=0, parent=None, action=None)

        # Initialize the reached dictionary with the initial state
        reached = {}
        reached[node.state] = True

        # Return if the node contains a goal state
        if node.state == grid.end:
            return Solution(node, reached)

        # Initialize the frontier with the initial node
        # In this example, the frontier is a priority queue
        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost)

        while True:
            # Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(reached)

            # Remove a node from the frontier with the lowest cost
            node = frontier.pop()

            # Get neighbors
            successors = grid.get_neighbours(node.state)

            for action, new_state in successors.items():
                # Check if the successor is not reached
                if new_state not in reached:
                    # Initialize the son node with updated cost
                    new_node = Node("", new_state,
                                    node.cost + grid.get_cost(new_state),
                                    parent=node, action=action)

                    # Mark the successor as reached
                    reached[new_state] = True

                    # Return if the node contains a goal state
                    if new_state == grid.end:
                        return Solution(new_node, reached)

                    # Add the new node to the frontier with its cost
                    frontier.add(new_node, new_node.cost)
