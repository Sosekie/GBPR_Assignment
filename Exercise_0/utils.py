from typing import Callable, List

import networkx as nx
from matplotlib import pyplot as plt


###############
#  CONSTANTS  #
###############

COLOR_MAP = {
    1.: '#648FFF',
    2.: '#785EF0',
    3.: '#DC267F',
    4.: '#FE6100',
    5.: '#FFB000',
    6.: '#004D40',
    7.: '#420E00'
}

NODE_LABEL = 'x'


###############
#   UTILS     #
###############

def load_graph(filename: str) -> nx.Graph:
    """
    Load the **file.graphml** as a **nx.Graph**.

    Args:
        filename:

    Returns:
        The loaded NetworkX graph
    """
    # Code here

    graphs = nx.read_graphml(filename)

    return graphs


def draw_graph(graph: nx.Graph,
               filename: str,
               labels: dict = None,
               node_color: List[str] = None,
               layout: Callable[[nx.Graph], dict] = None) -> None:
    """
    This function draws a given networkx graph object, saves the drawing to a specified file 

    Args:
        graph: A networkx graph object.
        filename: A string representing the path and filename
                  where the graph will be saved as an image.
        labels: A dictionary that maps node indices to labels.
        node_color: A list of strings representing the color of each node in the graph.
        layout: A layout function that takes a graph as input and returns a dictionary of node positions
                If None, the **nx.kamada_kawai_layout** layout will be used.

    """
    # Code here

    # Reference: https://networkx.org/documentation/stable/tutorial.html

    if layout is None:
        layout = nx.kamada_kawai_layout
    positions = layout(graph)
    
    # node = [(node_id, {attribute_key: attribute_value, ...}), ...]
    # node[0] is the node identifier and node[1] is the dictionary of attributes.
    # both key is float so we use node's value to get color in COLOR_MAP
    node_colors = [COLOR_MAP[node[1]['x']] for node in graph.nodes(data=True)]
    # use node identifier and value to generate a new dictionary
    labels = {node[0]: str(node[1]['x']) for node in graph.nodes(data=True)}

    # Draw the nodes
    # Set opacity level to 0.8 like the demo
    nx.draw_networkx_nodes(graph, positions, node_color=node_colors, alpha=0.8)

    # Draw the edges
    nx.draw_networkx_edges(graph, positions, alpha=1)

    # Draw the labels with white font
    nx.draw_networkx_labels(graph, positions, labels=labels, font_color='white', font_size=8)

    plt.axis('off')
    plt.savefig(filename)
    plt.close()

    pass
