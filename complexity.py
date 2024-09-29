import math
from graph1 import Graph

def bfs_dfs_complexity(V, E):
    """
    Time Complexity for BFS/DFS is O(V + E)
    """
    complexity = V + E
    print(f"BFS/DFS Time Complexity: O(V + E) = O({V} + {E}) = O({complexity})")
    return complexity

def graph_coloring_backtracking_complexity(V, m):
    """
    Time Complexity for Graph Coloring with Backtracking is O(m^V)
    """
    complexity = math.pow(m, V)
    print(f"Graph Coloring (Backtracking) Time Complexity: O(m^V) = O({m}^{V}) = O({int(complexity)})")
    return complexity

def graph_coloring_forward_checking_complexity(V, m):
    """
    Time Complexity for Graph Coloring with Forward Checking is close to O(m^V)
    """
    complexity = math.pow(m, V)
    print(f"Graph Coloring (Forward Checking) Time Complexity: O(m^V) = O({m}^{V}) = O({int(complexity)})")
    return complexity

def arc_consistency_complexity(V, E):
    """
    Time Complexity for Arc Consistency is O(V^2 * E) (in general case)
    """
    complexity = math.pow(V, 2) * E
    print(f"Arc Consistency Time Complexity: O(V^2 * E) = O({V}^2 * {E}) = O({int(complexity)})")
    return complexity

def ucs_complexity(V, E):
    complexity = (V + E) * math.log(V)
    print(f"UCS Time Complexity: O((V + E) log V) = O(({V} + {E}) log {V}) = O({int(complexity)})")
    return complexity

def ids_complexity(b, d):
    complexity = math.pow(b, d)
    print(f"IDS Time Complexity: O(b^d) = O({b}^{d}) = O({int(complexity)})")
    return complexity

def greedy_complexity(V, E):
    complexity = (V + E) * math.log(V)
    print(f"Greedy Time Complexity: O((V + E) log V) = O(({V} + {E}) log {V}) = O({int(complexity)})")
    return complexity

def a_star_complexity(V, E):
    complexity = (V + E) * math.log(V)
    print(f"A* Time Complexity: O((V + E) log V) = O(({V} + {E}) log {V}) = O({int(complexity)})")
    return complexity

def dijkstra_complexity(V, E):
    complexity = (V + E) * math.log(V)
    print(f"Dijkstra Time Complexity: O((V + E) log V) = O(({V} + {E}) log {V}) = O({int(complexity)})")
    return complexity

def calculate_branching_factor(graph):
    total_neighbors = 0
    total_nodes = len(graph.get_nodes())
    
    for node in graph.get_nodes():
        neighbors = graph.get_neighbors(node)  # This will return a list of neighbors
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
    # Example graph size for complexity analysis
    V = 5  # Number of vertices (nodes)
    E = 4  # Number of edges
    m = 3  # Number of available colors
    
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

    print("\n--- Complexity Calculations ---")
    
    # BFS and DFS Time Complexity
    bfs_dfs_complexity(V, E)

    # Graph Coloring with Backtracking Time Complexity
    graph_coloring_backtracking_complexity(V, m)

    # Graph Coloring with Forward Checking Time Complexity
    graph_coloring_forward_checking_complexity(V, m)

    # Arc Consistency Time Complexity
    arc_consistency_complexity(V, E)
    
    ucs_complexity(V, E)
    
    ids_complexity(b, d)
    
    greedy_complexity(V, E)
    
    a_star_complexity(V, E)
    
    dijkstra_complexity(V, E)
    
    

if __name__ == "__main__":
    main()
