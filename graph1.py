class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, cost):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, cost))
        self.adj_list[v].append((u, cost))

    def get_neighbors(self, node, with_cost=False):
        if with_cost:
            return self.adj_list.get(node, [])
        else:
            return [neighbor for neighbor, cost in self.adj_list.get(node, [])]

    def get_nodes(self):
        return list(self.adj_list.keys())
