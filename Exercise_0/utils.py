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
    return None


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
    pass
