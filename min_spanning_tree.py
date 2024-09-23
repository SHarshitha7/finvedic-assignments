import heapq
def prims(vertices, edges):
    graph = {i: [] for i in range(vertices)}
    for u, v, weight in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))

    mst = []
    total_cost = 0
    visited = set()
    min_heap = [(0, 0)]  
    edge_to = {0: None}  

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            total_cost += weight

            if edge_to[u] is not None:
                mst.append((edge_to[u], u, weight))
                
            for edge_weight, v in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (edge_weight, v))
                    edge_to[v] = u  

    return mst, total_cost

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    
    edges_count = int(input("Enter the number of edges: "))

    edges = []
    print("Enter the edges in the format (u v weight):")
    for _ in range(edges_count):
        u, v, weight = input().split()
        edges.append((ord(u) - ord('A'), ord(v) - ord('A'), int(weight)))

    mst_edges, total_cost = prims(vertices, edges)

    print("Minimum Spanning Tree edges and their weights:")
    for u, v, weight in mst_edges:
        print(f"{chr(u + ord('A'))}-{chr(v + ord('A'))}: {weight}")
    print("Total cost of MST:", total_cost)
