class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def greedy_coloring(self):
        result = [-1] * self.V  
      
        result[0] = 0

        available = [False] * self.V

        for u in range(1, self.V):
            for v in self.graph[u]:
                if result[v] != -1:
                    available[result[v]] = True

            for color in range(self.V):
                if not available[color]:
                    break

            result[u] = color

            for v in self.graph[u]:
                if result[v] != -1:
                    available[result[v]] = False

        color_names = ["Red", "Blue", "Green"]  
        for u in range(self.V):
            print(f"Vertex {u} --> Color {color_names[result[u]]}")

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    
    graph = Graph(vertices)
    
    edges = int(input("Enter the number of edges: "))

    print("Enter the edges (format: u v):")
    for _ in range(edges):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    print("Coloring of vertices:")
    graph.greedy_coloring()
