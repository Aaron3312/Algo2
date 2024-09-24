def bellman_ford(graph, V, start):
    # Initialize distances and predecessors
    dist = [float('inf')] * V
    pred = [None] * V
    dist[start] = 0

    # Relax edges V-1 times
    for _ in range(V - 1):
        for u in range(V):
            for v in range(V):
                if graph[u][v] != 0:
                    if dist[u] + graph[u][v] < dist[v]:
                        dist[v] = dist[u] + graph[u][v]
                        pred[v] = u
                        

    return dist, pred

def print_solution(dist, pred, V, start):
    print("Vertex\tDistance\tPath")
    for i in range(V):
        if i != start:
            path = []
            curr = i
            while curr is not None:
                path.append(curr)
                curr = pred[curr]
            path = path[::-1]
            letter_path = ' -> '.join(chr(65+node) for node in path)
            print(f"{chr(65+i)}\t{dist[i]}\t\t{letter_path}")

# Define a dictionary to convert letters A-Z to numbers 0-25
letter_to_number = {chr(65+i): i for i in range(26)}

# Get matrix size from user
size = int(input("Enter the size of the adjacency matrix: "))

# Read adjacency matrix from file
matrix = []
with open("input.txt", "r") as f:
    for _ in range(size):
        row = list(map(int, f.readline().split()))
        matrix.append(row)

# Ask user for starting node in letter form
start_letter = input("Enter the starting node (A-Z): ").upper()
start = letter_to_number[start_letter]

# Run Bellman-Ford algorithm
distances, predecessors = bellman_ford(matrix, size, start)

if distances is not None:
    print_solution(distances, predecessors, size, start)