class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, v, visited, rec_stack):
        visited.add(v)
        rec_stack.add(v)

        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                if self.dfs(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(v)
        return False

    def is_cyclic(self):
        visited = set()
        rec_stack = set()

        for vertex in self.graph:
            if vertex not in visited:
                if self.dfs(vertex, visited, rec_stack):
                    return True
        return False

if __name__ == "__main__":
    g = Graph()
    
    edges = int(input("Enter the number of edges: "))

    print("Enter the edges in the format 'u v':")
    for _ in range(edges):
        u, v = input().split()
        g.add_edge(u, v)

    has_cycle = g.is_cyclic()
    print(has_cycle)  # Prints True if there's a cycle, otherwise False
