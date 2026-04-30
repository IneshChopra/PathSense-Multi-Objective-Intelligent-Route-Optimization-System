import heapq

def dijkstra(graph, start, end, weight):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph.nodes}
    previous = {node: None for node in graph.nodes}

    distances[start] = 0

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        for neighbor in graph.neighbors(current_node):
            edges = graph.get_edge_data(current_node, neighbor)

            min_weight = float('inf')
            for key in edges:
                edge_data = edges[key]
                w = edge_data.get(weight, 1)
                if w < min_weight:
                    min_weight = w

            distance = current_dist + min_weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous[node]

    path.reverse()
    return path