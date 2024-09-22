def is_safe(graph, node, colors, color):
    for neighbor in graph.get_neighbors(node):
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring_backtracking(graph, colors, node_index, available_colors):
    nodes = graph.get_nodes()
    if node_index == len(nodes):
        return True

    node = nodes[node_index]
    for color in available_colors:
        if is_safe(graph, node, colors, color):
            colors[node] = color
            if graph_coloring_backtracking(graph, colors, node_index + 1, available_colors):
                return True
            colors[node] = None
    return False
