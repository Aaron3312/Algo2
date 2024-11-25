from typing import Dict, List, Set, Tuple
import heapq

class Node:
    def __init__(self, name: str, h: int):
        self.name = name
        self.h = h
        self.neighbors: List[Tuple['Node', int]] = []  # Lista de (nodo, costo)
    
    def add_neighbor(self, node: 'Node', cost: int):
        self.neighbors.append((node, cost))

    def __lt__(self, other):
        # Necesario para heapq
        return self.name < other.name

class PathState:
    def __init__(self, node: Node, g: int, parent: 'PathState' = None):
        self.node = node
        self.g = g  # costo acumulado hasta este nodo
        self.f = g + node.h  # f = g + h
        self.parent = parent
    
    def __lt__(self, other):
        # Comparador para heapq, ordena por f
        return self.f < other.f

def reconstruct_path(state: PathState) -> List[str]:
    path = []
    current = state
    while current:
        path.append(current.node.name)
        current = current.parent
    return list(reversed(path))

def astar(start: Node, goal: Node, optimize: bool = False) -> Tuple[List[str], int]:
    """
    Implementa A* con opción de usar la optimización de no revisitar nodos.
    
    Args:
        start: Nodo inicial
        goal: Nodo objetivo
        optimize: Si True, usa la optimización de no revisitar nodos
    
    Returns:
        Tupla de (camino, costo total)
    """
    fringe = []  # priority queue
    visited = set() if optimize else set()  # Solo usada si optimize=True
    
    # Inicializar con el estado inicial
    initial_state = PathState(start, 0)
    heapq.heappush(fringe, initial_state)
    
    while fringe:
        current_state = heapq.heappop(fringe)
        current_node = current_state.node
        
        # Si encontramos el objetivo, reconstruimos el camino
        if current_node == goal:
            return reconstruct_path(current_state), current_state.g
        
        # Si usamos optimización y ya visitamos este nodo, lo saltamos
        if optimize and current_node.name in visited:
            continue
            
        if optimize:
            visited.add(current_node.name)
        
        # Explorar vecinos
        for neighbor, cost in current_node.neighbors:
            new_g = current_state.g + cost
            new_state = PathState(neighbor, new_g, current_state)
            heapq.heappush(fringe, new_state)
    
    return None, float('inf')  # No se encontró camino

def create_test_graph() -> Tuple[Node, Node]:
    """Crea el grafo del ejemplo y retorna (start, goal)"""
    # Crear nodos
    nodes = {
        'S': Node('S', 2),
        'A': Node('A', 4),
        'B': Node('B', 1),
        'C': Node('C', 1),
        'G': Node('G', 0)
    }
    
    # Agregar conexiones
    nodes['S'].add_neighbor(nodes['A'], 1)
    nodes['S'].add_neighbor(nodes['B'], 1)
    nodes['A'].add_neighbor(nodes['C'], 1)
    nodes['B'].add_neighbor(nodes['C'], 2)
    nodes['C'].add_neighbor(nodes['G'], 3)
    
    return nodes['S'], nodes['G']

def main():
    # Crear el grafo
    start, goal = create_test_graph()
    
    # Probar A* con optimización (subóptimo)
    print("\nA* CON optimización (no revisitar):")
    path, cost = astar(start, goal, optimize=True)
    print(f"Camino encontrado: {' -> '.join(path)}")
    print(f"Costo total: {cost}")
    
    # Probar A* sin optimización (óptimo)
    print("\nA* SIN optimización (permite revisitar):")
    path, cost = astar(start, goal, optimize=False)
    print(f"Camino encontrado: {' -> '.join(path)}")
    print(f"Costo total: {cost}")

if __name__ == "__main__":
    main()