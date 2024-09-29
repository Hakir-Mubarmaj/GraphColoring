import math
from graph1 import Graph

def bfs_complexity(b, d):
    complexity = math.pow(b, d)
    print(f"BFS Time Complexity: O(b^d) = O({b}^{d}) = O({int(complexity)})")
    return complexity

def dfs_complexity(b, m):
    complexity = math.pow(b, m)
    print(f"DFS Time Complexity: O(b^m) = O({b}^{m}) = O({int(complexity)})")
    return complexity

def ucs_complexity(V, E):
    complexity = (V + E) * math.log(V)
    print(f"UCS Time Complexity: Number of nodes with g(n) <= C*")
    return complexity

def ids_complexity(b, d):
    complexity = math.pow(b, d)
    print(f"IDS Time Complexity: O(b^d) = O({b}^{d}) = O({int(complexity)})")
    return complexity

def greedy_complexity(b, d, m):
    worst_case = math.pow(b, m)
    best_case = math.pow(b, d)
    print(f"Greedy Time Complexity (Worst Case): O(b^m) = O({b}^{m}) = O({int(worst_case)})")
    print(f"Greedy Time Complexity (Best Case): O(b^d) = O({b}^{d}) = O({int(best_case)})")
    return worst_case, best_case

def a_star_complexity(V, E):
    print(f"A* Time Complexity: Number of nodes with g(n) + h(n) <= C*")
    return (V + E) * math.log(V)

def dijkstra_complexity(V, E):
    complexity = (V + E) * math.log(V)
    print(f"Dijkstra Time Complexity: O((V + E) log V) = O(({V} + {E}) log {V}) = O({int(complexity)})")
    return complexity

def calculate_branching_factor(graph):
    total_neighbors = 0
    total_nodes = len(graph.get_nodes())
    
    for node in graph.get_nodes():
        neighbors = graph.get_neighbors(node)
        total_neighbors += len(neighbors)
    
    if total_nodes == 0:
        return 0
    
    # Branching factor is the average number of neighbors per node
    return total_neighbors / total_nodes

def bfs_with_depth(graph, start, goal):
    visited = set()
    queue = [(start, 0)]  # Each item in the queue is a tuple (node, depth)
    
    while queue:
        node, depth = queue.pop(0)
        
        if node == goal:
            return depth
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get_neighbors(node):
                if neighbor not in visited:
                    queue.append((neighbor, depth + 1))
    
    return -1  # Return -1 if no path is found

def main():
    V = 5  # Number of vertices (nodes)
    E = 6  # Number of edges
    
    graph = Graph()
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 3, 1)
    graph.add_edge(1, 4, 3)
    graph.add_edge(2, 4, 2)
    graph.add_edge(3, 4, 2)
    
    start_node = 0
    goal_node = 4
    b = calculate_branching_factor(graph)
    d = bfs_with_depth(graph, start_node, goal_node)
    m = 5  # Maximum path length for DFS and Greedy Worst-case

    print("\n--- Complexity Calculations ---")
    
    # BFS Time Complexity
    bfs_complexity(b, d)

    # DFS Time Complexity
    dfs_complexity(b, m)

    # UCS Time Complexity
    ucs_complexity(V, E)
    
    # IDS Time Complexity
    ids_complexity(b, d)
    
    # Greedy Time Complexity
    greedy_complexity(b, d, m)
    
    # A* Time Complexity
    a_star_complexity(V, E)
    
    # Dijkstra Time Complexity
    dijkstra_complexity(V, E)

if __name__ == "__main__":
    main()
