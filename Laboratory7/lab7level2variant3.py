import csv
from collections import deque, defaultdict


class MaxFlowFinder:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = self.graph[u].get(v, 0) + capacity
        if v not in self.graph:
            self.graph[v] = {}
        if u not in self.graph[v]:
            self.graph[v][u] = 0

    def bfs(self, source, sink, parent):
        visited = {node: False for node in self.graph}
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()
            for v, capacity in self.graph[u].items():
                if not visited.get(v, False) and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def get_max_flow(self, source, sink):
        parent = {}
        max_f = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_f += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_f


def calculate_max_cars(file_path):
    finder = MaxFlowFinder()
    
    try:
        with open(file_path, mode="r", encoding="utf-8") as f:
            lines = list(csv.reader(f))
            if len(lines) < 3:
                return 0

            farms = [item.strip() for item in lines[0]]
            shops = [item.strip() for item in lines[1]]
            
            s_source = "SUPER_SOURCE"
            s_sink = "SUPER_SINK"

            for farm in farms:
                finder.add_edge(s_source, farm, float("inf"))
            
            for shop in shops:
                finder.add_edge(shop, s_sink, float("inf"))

            for row in lines[2:]:
                if len(row) >= 3:
                    u, v, cap = row[0].strip(), row[1].strip(), int(row[2].strip())
                    finder.add_edge(u, v, cap)

            return finder.get_max_flow(s_source, s_sink)
    except (FileNotFoundError, ValueError, IndexError):
        return 0


if __name__ == "__main__":
    result = calculate_max_cars("roads.csv")
    print(f"Maximum number of cars: {result}")
