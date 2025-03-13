import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    previous_nodes = {}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > shortest_distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return shortest_distances, previous_nodes


def reconstruct_path(previous_nodes, start, end):
    """ Reconstruct the shortest path from start to end. """
    path = []
    current = end
    while current != start:
        path.append(current)
        current = previous_nodes.get(current)
        if current is None:  # If no path exists
            return None
    path.append(start)
    path.reverse()
    return path


def main():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 5, 'D': 10},
        'C': {'A': 2, 'B': 5, 'D': 3, 'E': 8},
        'D': {'B': 10, 'C': 3, 'E': 6, 'F': 7},
        'E': {'C': 8, 'D': 6, 'F': 4},
        'F': {'D': 7, 'E': 4}
    }

    start = 'A'
    end = 'F'
    
    shortest_distances, previous_nodes = dijkstra(graph, start)
    path = reconstruct_path(previous_nodes, start, end)
    
    print(f"Shortest distance from {start} to {end}: {shortest_distances[end]}")
    print(f"Path: {path}")


if __name__ == "__main__":
    main()
