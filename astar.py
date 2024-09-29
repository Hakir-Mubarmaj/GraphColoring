import heapq

def a_star(graph, start, goal, heuristic):
    priority_queue = [(0, start)]
    visited = set()
    came_from = {start: None}
    cost_so_far = {start: 0}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == goal:
            break

        for neighbor, edge_cost in graph.get_neighbors(current_node, with_cost=True):
            new_cost = current_cost + edge_cost
            if neighbor not in visited or new_cost < cost_so_far.get(neighbor, float('inf')):
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor)
                heapq.heappush(priority_queue, (priority, neighbor))
                came_from[neighbor] = current_node

    return came_from, cost_so_far
