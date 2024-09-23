class Edge:
    def __init__(self, u, v, weight):
        self.u = u  
        self.v = v  
        self.weight = weight

def bellman_ford(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0  

    for _ in range(len(graph) - 1):
        for u in graph:
            for edge in graph[u]:
                if distances[u] != float('inf') and distances[u] + edge.weight < distances[edge.v]:
                    distances[edge.v] = distances[u] + edge.weight

    for u in graph:
        for edge in graph[u]:
            if distances[u] != float('inf') and distances[u] + edge.weight < distances[edge.v]:
                print("Graph contains a negative weight cycle")
                return None

    return distances

def print_shortest_paths(distances, source):
    print(f"Shortest paths from {source}:")
    for vertex, distance in distances.items():
        print(f"{source} -> {vertex}: {distance}")

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))

    graph = {chr(65 + i): [] for i in range(vertices)}
    
    print("Enter the edges in the format 'u v weight' (enter 'done' to finish):")
    while True:
        edge_input = input()
        if edge_input.lower() == 'done':
            break
        u, v, weight = edge_input.split()
        weight = int(weight)
        graph[u].append(Edge(u, v, weight))
        graph[v].append(Edge(v, u, weight))  

    source = input("Enter the source vertex: ").strip()

    distances = bellman_ford(graph, source)
    if distances is not None:
        print_shortest_paths(distances, source)
