def forward_checking(graph, colors, available_colors):
    for node in graph.get_nodes():
        for neighbor in graph.get_neighbors(node):
            if colors[neighbor] == colors[node]:
                return False
    return True

def graph_coloring_forward_checking(graph, colors, available_colors):
    if forward_checking(graph, colors, available_colors):
        return True
    return False
