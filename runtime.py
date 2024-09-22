import time
from bfs import bfs
from dfs import dfs
from backtracking import graph_coloring_backtracking
from forward_checking import graph_coloring_forward_checking
from arc_consistency import is_arc_consistent
from graph import Graph

def measure_time_bfs(graph, start):
    start_time = time.time()
    bfs(graph, start)
    end_time = time.time()
    print(f"\nBFS Execution Time: {end_time - start_time:.6f} seconds")

def measure_time_dfs(graph, start):
    start_time = time.time()
    dfs(graph, start)
    end_time = time.time()
    print(f"\nDFS Execution Time: {end_time - start_time:.6f} seconds")

def measure_time_backtracking(graph, available_colors):
    colors = {node: None for node in graph.get_nodes()}
    start_time = time.time()
    result = graph_coloring_backtracking(graph, colors, 0, available_colors)
    end_time = time.time()
    if result:
        print(f"Graph Coloring (Backtracking) Execution Time: {end_time - start_time:.6f} seconds")
    else:
        print("No solution found.")

def measure_time_forward_checking(graph, available_colors):
    colors = {node: None for node in graph.get_nodes()}
    start_time = time.time()
    result = graph_coloring_forward_checking(graph, colors, available_colors)
    end_time = time.time()
    if result:
        print(f"Graph Coloring (Forward Checking) Execution Time: {end_time - start_time:.6f} seconds")
    else:
        print("No solution found.")

def measure_time_arc_consistency(graph, colors):
    start_time = time.time()
    result = is_arc_consistent(graph, colors)
    end_time = time.time()
    print(f"Arc Consistency Check Execution Time: {end_time - start_time:.6f} seconds")
    return result

def main():
    # Create a graph
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)

    print("Measuring BFS:")
    measure_time_bfs(graph, 0)

    print("\nMeasuring DFS:")
    measure_time_dfs(graph, 0)

    available_colors = ['Red', 'Green', 'Blue']
    
    print("\nMeasuring Graph Coloring (Backtracking):")
    measure_time_backtracking(graph, available_colors)

    print("\nMeasuring Graph Coloring (Forward Checking):")
    measure_time_forward_checking(graph, available_colors)

    colors = {node: 'Red' for node in graph.get_nodes()}  # Assign arbitrary colors to test arc consistency
    print("\nMeasuring Arc Consistency:")
    measure_time_arc_consistency(graph, colors)

if __name__ == "__main__":
    main()
