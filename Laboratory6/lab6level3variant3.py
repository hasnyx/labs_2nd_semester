def find_unreachable_cities(cities, storages, active_pipelines):
    graph = {node: [] for node in (cities + storages)}
    for start, end in active_pipelines:
        if start in graph:
            graph[start].append(end)

    results = []

    for storage in storages:
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(storage)

        unreachable = [city for city in cities if city not in visited]

        if unreachable:
            results.append([storage, unreachable])

    return results