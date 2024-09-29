import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph
from bfs import bfs
from collections import deque
from dfs import dfs
from backtracking import graph_coloring_backtracking

def visualize_bfs(graph, start):
    G = nx.Graph()

    for node in graph.get_nodes():
        G.add_node(node)

    for node in graph.get_nodes():
        for neighbor in graph.get_neighbors(node):
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    
    # BFS Visualization
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        nx.draw(G, pos, with_labels=True, nodelist=visited, node_color='skyblue', node_size=2000, font_size=15)
        plt.title(f'BFS: Visiting node {node}')
        plt.pause(1)

        for neighbor in graph.get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    plt.show()
    
def visualize_dfs(graph, start, visited=None, pos=None, G=None):
    if visited is None:
        visited = set()
        G = nx.Graph()
        for node in graph.get_nodes():
            G.add_node(node)
        for node in graph.get_nodes():
            for neighbor in graph.get_neighbors(node):
                G.add_edge(node, neighbor)
        pos = nx.spring_layout(G)
    
    visited.add(start)
    nx.draw(G, pos, with_labels=True, nodelist=visited, node_color='skyblue', node_size=2000, font_size=15)
    plt.title(f'DFS: Visiting node {start}')
    plt.pause(1)

    for neighbor in graph.get_neighbors(start):
        if neighbor not in visited:
            visualize_dfs(graph, neighbor, visited, pos, G)
            
def visualize_coloring(graph, colors, available_colors):
    G = nx.Graph()

    for node in graph.get_nodes():
        G.add_node(node)

    for node in graph.get_nodes():
        for neighbor in graph.get_neighbors(node):
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    
    # Coloring visualization
    for node in graph.get_nodes():
        color_list = [colors[node] if colors[node] else 'white' for node in graph.get_nodes()]
        nx.draw(G, pos, with_labels=True, node_color=color_list, node_size=2000, font_size=15)
        plt.title(f'Graph Coloring: Node {node} assigned {colors[node]}')
        plt.pause(1)

    plt.show()

def visualize_graph():
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    
    # visualize_bfs(graph, 0)
    # visualize_dfs(graph, 0)

    available_colors = ['Red', 'Green', 'Blue']
    colors = {node: None for node in graph.get_nodes()}

    # Backtracking for coloring
    if graph_coloring_backtracking(graph, colors, 0, available_colors):
        visualize_coloring(graph, colors, available_colors)
    else:
        print("No solution found.")

if __name__ == "__main__":
    visualize_graph()
