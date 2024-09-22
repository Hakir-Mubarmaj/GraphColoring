import math

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

def main():
    # Example graph size for complexity analysis
    V = 5  # Number of vertices (nodes)
    E = 4  # Number of edges
    m = 3  # Number of available colors

    print("\n--- Complexity Calculations ---")
    
    # BFS and DFS Time Complexity
    bfs_dfs_complexity(V, E)

    # Graph Coloring with Backtracking Time Complexity
    graph_coloring_backtracking_complexity(V, m)

    # Graph Coloring with Forward Checking Time Complexity
    graph_coloring_forward_checking_complexity(V, m)

    # Arc Consistency Time Complexity
    arc_consistency_complexity(V, E)

if __name__ == "__main__":
    main()
