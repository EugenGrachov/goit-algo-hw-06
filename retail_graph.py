import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Stores North
store_138 = "Vyzvolna St"
store_413 = "Chubarya St"
store_290 = "Bakaliivska St"
store_1303 = "Nikolskyi"
store_1356 = "Klochkovskyi"
store_967 = "Lyapunova St"
store_1255 = "Verbna St"
store_255 = "Studentska St"

north_stores = [
    store_138, store_413, store_290, store_1303,
    store_1356, store_967, store_1255, store_255
]
north_route_time_min = [5, 6, 7, 10, 8, 4, 13]

# Stores South
store_720 = "Cotovskyi Ln"
store_125 = "Beketova St"
store_551 = "Dobra St"
store_108 = "Vilna St"
store_126 = "Nebesna Ave"
store_122 = "Kanta Ave"
store_714 = "Klochkivska St"
store_738 = "Oleniv Ave"

south_stores = [
    store_720, store_125, store_551, store_108,
    store_126, store_122, store_714, store_738
]
south_route_time_min = [9, 5, 7, 8, 11, 4, 6]

# Stores East
store_784 = "Tankopiia"
store_410 = "Malysheva St"
store_393 = "Shekspira St"
store_902 = "Mariyanenka Ln"
store_157 = "Zolochivska St"
store_180 = "Privokzalna St"
store_251 = "Budivnykiv Ave"
store_1070 = "Ak. Pavlova Ave"

east_stores = [
    store_784, store_410, store_393, store_902,
    store_157, store_180, store_251, store_1070
]
east_route_time_min = [7, 5, 6, 4, 8, 3, 10]

# Stores West
store_1105 = "Hirshmana St"
store_1432 = "Sharykova St"
store_592 = "Rybalko St"
store_1255 = "Svobody Ln"
store_1256 = "Shevchenka St"

west_stores = [
    store_1105, store_1432, store_592,
    store_1255, store_1256
]
west_route_time_min = [5, 3, 7, 6]

# Integrated retail network (intersections of stores from different districts)
retail_hub_north_south = [store_138, store_551]
retail_hub_north_east = [store_138, store_393]
retail_hub_south_east = [store_551, store_393]
retail_hub_west_north = [store_1432, store_138]
retail_hub_west_south = [store_1432, store_551]


# Create the retail graph with all stores and their connections
def create_retail_graph():
    # Initialize the graph
    rtl_graph = nx.Graph()
    
    # Add nodes for each district
    rtl_graph.add_nodes_from(north_stores)
    rtl_graph.add_nodes_from(south_stores)
    rtl_graph.add_nodes_from(east_stores)
    rtl_graph.add_nodes_from(west_stores)

	# Add edges for each district with travel time as weight
    rtl_graph.add_weighted_edges_from(array_to_pairs(north_stores, weights=north_route_time_min))
    rtl_graph.add_weighted_edges_from(array_to_pairs(south_stores, weights=south_route_time_min))
    rtl_graph.add_weighted_edges_from(array_to_pairs(east_stores, weights=east_route_time_min))
    rtl_graph.add_weighted_edges_from(array_to_pairs(west_stores, weights=west_route_time_min))

    # Add edges for intersections of stores from different districts
    rtl_graph.add_weighted_edges_from(array_to_pairs(retail_hub_north_south, weights=[8]))
    rtl_graph.add_weighted_edges_from(array_to_pairs(retail_hub_north_east, weights=[5]))
    rtl_graph.add_weighted_edges_from(array_to_pairs(retail_hub_south_east, weights=[11]))
    rtl_graph.add_weighted_edges_from(array_to_pairs(retail_hub_west_north, weights=[9]))
    rtl_graph.add_weighted_edges_from(array_to_pairs(retail_hub_west_south, weights=[3]))

    return rtl_graph

def display_graph_info(rtl_graph: nx.Graph):
    print(f"Total number of stores: {rtl_graph.number_of_nodes()}")
    print(f"Total number of connections: {rtl_graph.number_of_edges()}")
    for store in rtl_graph.nodes:
        print(f"Store '{store}' has {len(rtl_graph[store])} connections")

def render_graph(rtl_graph):
    np.random.seed(43)

    node_colors = []
    for node in rtl_graph.nodes:
        if node in north_stores:
            node_colors.append("#491E06")  # North
        elif node in south_stores:
            node_colors.append("#1B2944")  # South
        elif node in east_stores:
            node_colors.append("#770371")  # East
        elif node in west_stores:
            node_colors.append("#284139")  # West

    plt.figure(3, figsize=(17, 13))
    pos = nx.spring_layout(rtl_graph, k=0.7)
    nx.draw(rtl_graph, pos, with_labels=True, node_size=2500, node_color=node_colors, font_size=8, width=2 )
    labels = nx.get_edge_attributes(rtl_graph, 'weight')
    nx.draw_networkx_labels(rtl_graph, pos, font_size=8, font_color="#97C3F1")
    nx.draw_networkx_edge_labels(rtl_graph, pos, edge_labels=labels, font_size=8)
    plt.title("Kharkiv Retail Network", fontsize=16)
    plt.show()

def array_to_pairs(array: list, weights=None) -> list:
    if len(array) <= 1:
        return []

    result = []
    num_edges = len(array) - 1

    # One fixed weight
    if isinstance(weights, (int, float)):
        for i in range(1, len(array)):
            result.append((array[i - 1], array[i], weights))
    # List of weights
    elif isinstance(weights, list):
        if len(weights) != num_edges:
            raise ValueError(f"Length of weights ({len(weights)}) must match number of edges ({num_edges})")
        for i in range(1, len(array)):
            result.append((array[i - 1], array[i], weights[i - 1]))
    # Without weights
    else:
        for i in range(1, len(array)):
            result.append((array[i - 1], array[i], 1))  # Standard weight 1

    return result

def main():
    rtl_graph = create_retail_graph()
    display_graph_info(rtl_graph)
    render_graph(rtl_graph)


if __name__ == '__main__':
    main()
