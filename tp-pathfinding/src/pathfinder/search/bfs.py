from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

from collections import deque

class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Encuentra un camino entre dos puntos en una cuadrícula utilizando Breadth-First Search (BFS)

        Args:
            grid (Grid): Cuadrícula de puntos

        Returns:
            Solution: Solución encontrada
        """
        # Inicializa un nodo con la posición inicial
        node = Node("", state=grid.start, cost=0, parent=None, action=None)

        # Inicializa el diccionario 'alcanzado' con el estado inicial
        reached = {}
        reached[node.state] = True

        # Devuelve la solución si el nodo contiene un estado objetivo
        if node.state == grid.end:
            return Solution(node, reached)

        # Inicializa la frontera con el nodo inicial utilizando una cola
        frontier = deque()
        frontier.append(node)

        while frontier:

            # Elimina un nodo de la frontera (FIFO)
            node = frontier.popleft()

            # Explora todas las acciones posibles (derecha, izquierda, arriba, abajo)
            successors = grid.get_neighbours(node.state)

            for action, new_state in successors.items():
                # Comprueba si el sucesor no ha sido alcanzado
                if new_state not in reached:

                    # Inicializa el nuevo nodo hijo
                    new_node = Node("", new_state,
                                    node.cost + grid.get_cost(new_state),
                                    parent=node, action=action)

                    # Marca el sucesor como alcanzado
                    reached[new_state] = True

                    # Devuelve la solución si el nodo contiene un estado objetivo
                    if new_state == grid.end:
                        return Solution(new_node, reached)

                    # Agrega el nuevo nodo a la frontera
                    frontier.append(new_node)

        # Si el ciclo termina y no se encuentra una solución, devuelve NoSolution
        return NoSolution(reached)
