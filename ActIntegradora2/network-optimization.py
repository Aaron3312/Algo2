import numpy as np
from typing import List, Tuple
from collections import defaultdict
import heapq

class NetworkOptimizer:
    def __init__(self, n: int, distances: List[List[int]], capacities: List[List[int]], centrals: List[Tuple[int, int]]):
        self.n = n  # número de colonias
        self.distances = np.array(distances)
        self.capacities = np.array(capacities)
        self.centrals = centrals

    def find_optimal_cabling(self) -> List[Tuple[str, str]]:
        """Implementación del algoritmo de Prim para encontrar el árbol de expansión mínima"""
        visited = [False] * self.n
        edges = []
        visited[0] = True
        mst_edges = []
        
        # Agregar todas las aristas del primer vértice
        for i in range(self.n):
            if i != 0 and self.distances[0][i] != 0:
                heapq.heappush(edges, (self.distances[0][i], 0, i))
        
        while edges:
            weight, u, v = heapq.heappop(edges)
            if visited[v]:
                continue
                
            visited[v] = True
            mst_edges.append((chr(65 + u), chr(65 + v)))
            
            for i in range(self.n):
                if not visited[i] and self.distances[v][i] != 0:
                    heapq.heappush(edges, (self.distances[v][i], v, i))
        
        return mst_edges

    def find_delivery_route(self) -> List[str]:
        """Implementación de una aproximación al TSP usando el algoritmo del vecino más cercano"""
        unvisited = set(range(1, self.n))
        route = [0]
        current = 0
        
        while unvisited:
            next_city = min(unvisited, key=lambda x: self.distances[current][x])
            route.append(next_city)
            unvisited.remove(next_city)
            current = next_city
            
        route.append(0)  # Regresar al inicio
        return [chr(65 + i) for i in route]

    def find_max_flow(self) -> int:
        """Implementación del algoritmo de Ford-Fulkerson"""
        def bfs(graph, source, sink, parent):
            visited = [False] * self.n
            queue = []
            queue.append(source)
            visited[source] = True
            
            while queue:
                u = queue.pop(0)
                for v in range(self.n):
                    if not visited[v] and graph[u][v] > 0:
                        queue.append(v)
                        visited[v] = True
                        parent[v] = u
            
            return visited[sink]

        residual_graph = self.capacities.copy()
        parent = [-1] * self.n
        max_flow = 0

        while bfs(residual_graph, 0, self.n-1, parent):
            path_flow = float("Inf")
            s = self.n-1
            while s != 0:
                path_flow = min(path_flow, residual_graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = self.n-1
            while v != 0:
                u = parent[v]
                residual_graph[u][v] -= path_flow
                residual_graph[v][u] += path_flow
                v = parent[v]

        return max_flow

    def find_voronoi_regions(self) -> List[List[float]]:
        """Implementación simplificada de regiones de Voronoi que retorna distancias"""
        # Inicializar lista de distancias para cada central
        distances_to_centrals = [[] for _ in range(len(self.centrals))]
        
        # Por simplicidad, creamos un grid de puntos y calculamos distancias a cada central
        for x in range(0, 1000, 50):  # Grid de 1000x1000
            for y in range(0, 1000, 50):
                min_dist = float('inf')
                closest_central = 0
                
                for i, (cx, cy) in enumerate(self.centrals):
                    dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
                    if dist < min_dist:
                        min_dist = dist
                        closest_central = i
                
                # Agregar la distancia a la lista de la central más cercana
                distances_to_centrals[closest_central].append(min_dist)
        
        return distances_to_centrals

def main():
    # Leer desde archivo en lugar de entrada estándar
    with open('network_input.txt', 'r') as file:
        # Lectura de entrada
        n = int(file.readline().strip())
        distances = []
        capacities = []
        
        # Leer matriz de distancias
        for _ in range(n):
            row = list(map(int, file.readline().strip().split()))
            distances.append(row)
        
        # Leer matriz de capacidades
        for _ in range(n):
            row = list(map(int, file.readline().strip().split()))
            capacities.append(row)
        
        # Leer ubicaciones de centrales
        centrals = []
        for _ in range(n):
            x, y = map(int, file.readline().strip().strip('()').split(','))
            centrals.append((x, y))
    
    # Crear instancia del optimizador
    optimizer = NetworkOptimizer(n, distances, capacities, centrals)
    
    # 1. Encontrar cableado óptimo
    optimal_cabling = optimizer.find_optimal_cabling()
    print("1. Cableado óptimo:")
    for edge in optimal_cabling:
        print(f"({edge[0]},{edge[1]})")
    
    # 2. Encontrar ruta de reparto
    delivery_route = optimizer.find_delivery_route()
    print("\n2. Ruta de reparto:")
    print(" -> ".join(delivery_route))
    
    # 3. Calcular flujo máximo
    max_flow = optimizer.find_max_flow()
    print(f"\n3. Flujo máximo: {max_flow}")
    
    # 4. Calcular regiones de Voronoi
    regions = optimizer.find_voronoi_regions()
    print("\n4. Regiones de Voronoi:")
    for i, region in enumerate(regions):
        print(f"Región {i+1}: {region}")

if __name__ == "__main__":
    main()
