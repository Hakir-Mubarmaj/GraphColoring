import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    priority_queue = [(heuristic(start), start)]  # (heuristic_cost, node)
    visited = set()
    came_from = {start: None}

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == goal:
            break

        for neighbor in graph.get_neighbors(current_node):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic(neighbor), neighbor))
                came_from[neighbor] = current_node

    return came_from
