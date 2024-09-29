from graph1 import Graph
from bfs import bfs
from dfs import dfs
from ucs import ucs
from ids import ids
from greedy import greedy_best_first_search
from astar import a_star
from dijkstra import dijkstra
from visualize import visualize_graph

# A simple heuristic function for Greedy and A* (for demonstration purposes)
def heuristic(node):
    return node  # You can define a proper heuristic based on your graph

def main():
    # Create a graph
    graph = Graph()
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 3, 1)
    graph.add_edge(1, 4, 3)
    graph.add_edge(2, 4, 2)
    graph.add_edge(3, 4, 2)
    
    start_node = 0
    goal_node = 4

    print("Choose the algorithm to run:")
    print("1. BFS")
    print("2. DFS")
    print("3. UCS")
    print("4. IDS")
    print("5. Greedy Best-First Search")
    print("6. A*")
    print("7. Dijkstra's Algorithm")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        print("Running BFS...")
        path = bfs(graph, start_node)
        visualize_graph(graph, path)
    elif choice == 2:
        print("Running DFS...")
        path = dfs(graph, start_node)
        visualize_graph(graph, path)
    elif choice == 3:
        print("Running UCS...")
        path, cost = ucs(graph, start_node, goal_node)
        visualize_graph(graph, path)
    elif choice == 4:
        print("Running IDS...")
        path = ids(graph, start_node, goal_node, max_depth=10)
        visualize_graph(graph, path)
    elif choice == 5:
        print("Running Greedy Best-First Search...")
        path = greedy_best_first_search(graph, start_node, goal_node, heuristic)
        visualize_graph(graph, path)
    elif choice == 6:
        print("Running A*...")
        path, cost = a_star(graph, start_node, goal_node, heuristic)
        visualize_graph(graph, path)
    elif choice == 7:
        print("Running Dijkstra's Algorithm...")
        path, cost = dijkstra(graph, start_node)
        visualize_graph(graph, path)
    else:
        print("Invalid choice! Exiting...")

if __name__ == "__main__":
    main()
