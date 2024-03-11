import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple

def create_graph(data: pd.DataFrame) -> nx.DiGraph:
    """
    Create a directed graph based on social network data.

    Parameters:
        data (pd.DataFrame): DataFrame containing social network data.

    Returns:
        nx.DiGraph: Directed graph representing the social network.
    """
    graph = nx.DiGraph()

    # Add nodes and edges to the graph
    for _, row in data.iterrows():
        graph.add_edge(
            row['source'],
            row['target'],
            relationship_type = row['relationship_type'],
            relationship_strength = row['relationship_strength']
        )

    return graph

def draw_graph(graph: nx.DiGraph, positions: Dict[str, Tuple[float, float]],
               edge_colors: Dict[str, str], edge_widths: List[float]) -> None:
    """
    Draw the social network graph with specified node positions, edge colors, and widths.

    Parameters:
        graph (nx.DiGraph): Directed graph representing the social network.
        positions (Dict[str, Tuple[float, float]]): Positions for the nodes.
        edge_colors (Dict[str, str]): Colors for edges based on relationship type.
        edge_widths (List[float]): Widths for edges based on relationship strength.
    """
    plt.figure(figsize = (12, 8))

    for rel_type, color in edge_colors.items():
        edges = [(source, target) for source, target, data in graph.edges(data = True)
                 if data['relationship_type']  =  =  rel_type]
        widths = [graph[source][target]['relationship_strength'] / 2 for source, target in edges]
        nx.draw_networkx_edges(graph, positions, edgelist = edges, edge_color = color, width = widths, edge_cmap = plt.cm.Blues)

    nx.draw_networkx_nodes(graph, positions, node_size = 5000, node_color = 'skyblue')
    nx.draw_networkx_labels(graph, positions)

    plt.title('Relationship Network')
    plt.show()

def analyse_graph(graph: nx.DiGraph) -> None:
    """
    Analyse the social network, including density, degree centrality, in-degree centrality, and betweenness centrality.

    Parameters:
        graph (nx.DiGraph): Directed graph representing the social network.
    """
    # Analyse the density of connections
    density = nx.density(graph)
    print(f"Network Density: {density}")

    # Analyse individuals with high centrality (degree centrality)
    degree_centrality = nx.degree_centrality(graph)
    sorted_degree_centrality = sorted(degree_centrality.items(), key = lambda x: x[1], reverse = True)
    print("\nTop 5 Nodes with Highest Degree Centrality:")
    for node, centrality in sorted_degree_centrality[:5]:
        print(f"{node}: {centrality}")

    # Analyse individuals with low centrality (in-degree centrality)
    in_degree_centrality = nx.in_degree_centrality(graph)
    sorted_in_degree_centrality = sorted(in_degree_centrality.items(), key = lambda x: x[1])
    print("\nTop 5 Nodes with Lowest In-Degree Centrality:")
    for node, centrality in sorted_in_degree_centrality[:5]:
        print(f"{node}: {centrality}")

    # Identify bridge nodes (nodes with high betweenness centrality)
    betweenness_centrality = nx.betweenness_centrality(graph)
    sorted_betweenness_centrality = sorted(betweenness_centrality.items(), key = lambda x: x[1], reverse = True)
    print("\nTop 5 Nodes with Highest Betweenness Centrality:")
    for node, centrality in sorted_betweenness_centrality[:5]:
        print(f"{node}: {centrality}")


# Read data from CSV
data_path = 'C:/Users/Oscar/Documents/Projects/social_network_analysis/social_circle2.csv'
social_network_data = pd.read_csv(data_path)

# Create a directed social network graph
social_graph = create_graph(social_network_data)

# Define positions for the nodes using a layout algorithm
node_positions = nx.spring_layout(social_graph)

# Define edge colors based on relationship type
relationship_colors = {
    'Family': 'blue',
    'Spouse': 'red',
    'In-law': 'green',
    'Acquaintance': 'orange',
    'Friend': 'purple',
    'Colleague': 'brown',
    'Stranger': 'gray'
}

# Define edge widths based on relationship strength
relationship_widths = [row['relationship_strength'] / 2 for _, row in social_network_data.iterrows()]

# Draw the social network graph
draw_graph(social_graph, node_positions, relationship_colors, relationship_widths)

# Analyse the social network
analyse_graph(social_graph)
