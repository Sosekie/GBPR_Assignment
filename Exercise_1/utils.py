import os
from glob import glob
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
    assert filename.split('.')[-1] == 'graphml', f'Filename not valid: {filename}'

    graph = nx.read_graphml(filename, node_type=int)

    return graph


def load_all_graphs(folder: str) -> List[nx.Graph]:
    """
    This function loads all the graphml graphs from the specified folder using the NetworkX library.

    Args:
        folder: The path of the folder where the graph files are stored.

    Returns:
        A list of NetworkX Graph objects.
    """
    graph_files = glob(os.path.join(folder, '*.graphml'))
    graphs = [load_graph(graph_file) for graph_file in graph_files]

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
    if not layout:
        layout = nx.kamada_kawai_layout

    drawing_options = {
        "edgecolors": "tab:gray",
        "node_size": 800,
        "alpha": 0.9,
        "font_color": "whitesmoke"
    }

    f = plt.figure()
    nx.draw(graph,
            labels=labels,
            node_color=node_color,
            pos=layout(graph),
            **drawing_options)
    f.savefig(filename)


def draw_all_graphs(graphs: List[nx.Graph],
                    folder: str,
                    use_node_lbl: bool = True) -> None:
    """

    Args:
        graphs:
        folder:
        use_node_lbl:

    Returns:

    """
    colors, labels = None, None
    for graph_idx, graph in enumerate(graphs):

        if use_node_lbl:
            # colors = [COLOR_MAP[node_lbl]
            #           for node_idx, node_lbl in graph.nodes(data=NODE_LABEL)]
            # labels = {node_idx: node_lbl
            #           for node_idx, node_lbl in graph.nodes(data=NODE_LABEL)}

            colors = [COLOR_MAP.get(node_lbl, '#999999')  # Use default color if node_lbl is None
                      for _, node_lbl in graph.nodes(data=NODE_LABEL)]
            labels = {node_idx: (node_lbl if node_lbl is not None else '')
                      for node_idx, node_lbl in graph.nodes(data=NODE_LABEL)}

        draw_graph(graph,
                   os.path.join(folder, f'graph_0{graph_idx}.png'),
                   labels=labels,
                   node_color=colors)
