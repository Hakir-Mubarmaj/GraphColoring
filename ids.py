def dls(graph, start, goal, depth):
    if start == goal:
        return True
    if depth <= 0:
        return False
    for neighbor in graph.get_neighbors(start):
        if dls(graph, neighbor, goal, depth-1):
            return True
    return False

def ids(graph, start, goal, max_depth):
    for depth in range(max_depth):
        if dls(graph, start, goal, depth):
            print(f"Found goal with depth: {depth}")
            return True
    return False
