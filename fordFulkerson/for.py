from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)
        
    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        
    def bfs(self, source, sink, parent):
        # Marcar todos los vértices como no visitados
        visited = defaultdict(bool)
        
        # Crear una cola para BFS
        queue = []
        
        # Marcar el nodo fuente como visitado y encolarlo
        queue.append(source)
        visited[source] = True
        
        # BFS Loop
        while queue:
            u = queue.pop(0)
            
            # Revisar todos los vértices adyacentes
            for v in self.graph[u]:
                # Si no está visitado y tiene capacidad
                if not visited[v] and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
        
        # Retornar True si llegamos al sumidero
        return visited[sink]
    
    def ford_fulkerson(self, source, sink):
        # Diccionario para almacenar el padre de cada nodo
        parent = defaultdict(lambda: None)
        max_flow = 0
        
        # Mientras exista un camino aumentante
        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            
            # Encontrar el flujo mínimo a lo largo del camino
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
                
            # Añadir el flujo al flujo máximo
            max_flow += path_flow
            
            # Actualizar las capacidades residuales
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                # Añadir arista residual si no existe
                if v not in self.graph:
                    self.graph[v] = {}
                if u not in self.graph[v]:
                    self.graph[v][u] = 0
                self.graph[v][u] += path_flow
                v = parent[v]
        
        return max_flow, self.graph

# Crear el grafo del ejemplo
g = Graph()

# Añadir las aristas con sus capacidades
g.add_edge('S', '1', 9)
g.add_edge('S', '2', 3)
g.add_edge('1', '3', 5)
g.add_edge('1', '2', 4)
g.add_edge('2', '4', 5)
g.add_edge('3', 'T', 15)
g.add_edge('4', 'T', 15)
g.add_edge('4', '3', 10)

# Calcular el flujo máximo
max_flow, residual_graph = g.ford_fulkerson('S', 'T')

print(f"El flujo máximo es: {max_flow}")
print("\nCapacidades residuales:")
for u in residual_graph:
    for v in residual_graph[u]:
        print(f"{u} -> {v}: {residual_graph[u][v]}")