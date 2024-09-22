def is_arc_consistent(graph, colors):
    for node in graph.get_nodes():
        for neighbor in graph.get_neighbors(node):
            if colors[node] == colors[neighbor]:
                return False
    return True
