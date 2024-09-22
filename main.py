from graph import Graph
from bfs import bfs
from dfs import dfs
from backtracking import graph_coloring_backtracking
from arc_consistency import is_arc_consistent
from forward_checking import graph_coloring_forward_checking

def main():
    # Create a graph
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)

    print("BFS traversal:")
    bfs(graph, 0)
    print("\nDFS traversal:")
    dfs(graph, 0)

    # Coloring using backtracking
    available_colors = ['Red', 'Green', 'Blue']
    colors = {node: None for node in graph.get_nodes()}

    print("\nGraph Coloring using Backtracking:")
    if graph_coloring_backtracking(graph, colors, 0, available_colors):
        print(colors)
    else:
        print("No solution found.")

    # Check arc consistency
    print("\nArc Consistency Check:")
    if is_arc_consistent(graph, colors):
        print("The graph is arc consistent.")
    else:
        print("The graph is not arc consistent.")
    
    # Forward Checking
    print("\nGraph Coloring using Forward Checking:")
    if graph_coloring_forward_checking(graph, colors, available_colors):
        print(colors)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
