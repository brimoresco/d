from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node
from queue import PriorityQueue

class AStarSearch:

    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

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
        frontier.add(node, node.cost + heuristic(node.state, grid.end))

        while True:
            # Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(reached)

            # Remove a node from the frontier
            node = frontier.pop()

            # Check if the node contains a goal state
            if node.state == grid.end:
                return Solution(node, reached)

            # Explore neighbors
            successors = grid.get_neighbours(node.state)
            for action, new_state in successors.items():
                if new_state not in reached:
                    reached[new_state] = True
                    new_node = Node("", new_state, parent=node, action=action, cost=node.cost + 1)
                    frontier.add(new_node, new_node.cost + heuristic(new_state, grid.end))

def heuristic(state, goal):
    """A heuristic function for A* Search (Manhattan distance)"""
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])
