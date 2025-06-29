import retail_graph
import networkx as nx


def dfs_path_search(graph, start, visited = None, path = None, parent = None):
    # Recursive call
    if visited is None:
        visited = set()
        path = []

    visited.add(start)
    if parent is not None:
        path.append((parent, start))
    for next in graph[start]:
        if next not in visited:
            dfs_path_search(graph, next, visited, path, start)

    return path

def bfs_path_search(graph, start):
    # Iterative call
    visited, queue = {start}, [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                path.append((vertex, neighbour))

    return path

def main():
    rtl_graph = retail_graph.create_retail_graph()

    # Traversal of the retail graph through the dfs and bfs algorithms
    departure_from = retail_graph.store_138
    dfs_path = dfs_path_search(rtl_graph, departure_from)
    bfs_path = bfs_path_search(rtl_graph, departure_from)

    print(f"DFS path is: {dfs_path}\n")
    print(f"BFS path is: {bfs_path}\n")

    # Ensure the correctness of implementations by using built-in functions of the same algorithms
    dfs_path_check = list(nx.dfs_edges(rtl_graph, source = departure_from))
    bfs_path_check = list(nx.bfs_edges(rtl_graph, source = departure_from))

    print(f"DFS path test, path is: {dfs_path_check}\n")
    print(f"BFS path test, path is: {bfs_path_check}\n")


if __name__ == '__main__':
    main() 
