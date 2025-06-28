import retail_graph
import heapq


def main():
    # Use graph from first task
    rtl_graph = retail_graph.create_retail_graph()

    # Calculate path
    shortest_path = dijkstra_shortest_path(rtl_graph, retail_graph.vatb_store_138)

    # Display path
    print(f"Shortest delivery path for retail graph:\n{shortest_path}")


# Find shortest path to visit every node
def dijkstra_shortest_path(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0

    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths


if __name__ == '__main__':
    main()