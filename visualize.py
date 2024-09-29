import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def visualize_graph(graph, path=None):
    """
    Visualize the graph using matplotlib and networkx.
    Optionally, highlight the path if provided.
    """
    G = nx.Graph()

    # Add edges to the graph
    for node in graph.get_nodes():
        for neighbor, cost in graph.get_neighbors(node, with_cost=True):
            G.add_edge(node, neighbor, weight=cost)

    pos = nx.spring_layout(G)  # Position nodes using a spring layout

    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)

    # Highlight the path if provided
    if path:
        edges_in_path = [(path[i], path[i+1]) for i in range(len(path)-1)]
        
        # Filter only valid edges that exist in the graph
        valid_edges_in_path = [(u, v) for u, v in edges_in_path if u in pos and v in pos]

        # Highlight the valid edges
        if valid_edges_in_path:
            nx.draw_networkx_edges(G, pos, edgelist=valid_edges_in_path, edge_color='r', width=2)

    # Display edge weights (costs)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()
