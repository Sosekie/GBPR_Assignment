#######################
#
# Name: Chenrui Fan
# Matriculation Number: 23-125-818
#
# Name: Francesco Lam
# Matriculation Number: 23-109-317
#
#######################

import os
import csv
from typing import List

import networkx as nx
import numpy as np

from utils import load_graph, draw_graph, COLOR_MAP, NODE_LABEL


#################
#    Part 1     #
#################

def part1() -> List[nx.Graph]:
    """
    1. Load all the graphs in './graphs'
    2. Plot and save the corresponding graph drawing in './drawings'
    3. Return the list of loaded graphs

    Returns:
        The list of loaded graphs
    """
    # Code here

    graph_files = os.listdir('./graphs')
    graphs = []

    for graph_file in graph_files:
        graph_path = os.path.join('./graphs', graph_file)
        print("graph: ", graph_path)
        graph = load_graph(graph_path)
        graphs.append(graph)

        drawing_filename = os.path.join('./drawings', f'{graph_file[:-8]}.png')

        draw_graph(graph, drawing_filename)

    return graphs


#################
#    Part 2     #
#################

def naive_graph_isomorphism(graph1: nx.Graph, graph2: nx.Graph) -> bool:
    """
    This function checks if two input graphs are isomorphic
    by comparing the number of nodes, number of edges and the labels of the nodes.

    Args:
        graph1: A networkx graph object
        graph2: A networkx graph object

    Returns:
        Returns True if the input graphs are isomorphic, else False.
    """
    # Code here

    if graph1.number_of_nodes() != graph2.number_of_nodes():
        return False
    if graph1.number_of_edges() != graph2.number_of_edges():
        return False
    
    labels1 = [graph1.nodes[node]['x'] for node in graph1.nodes()]
    labels2 = [graph2.nodes[node]['x'] for node in graph2.nodes()]
    
    if sorted(labels1) == sorted(labels2):
        return True
    return False


def part2(graphs: List[nx.Graph]) -> None:
    """
    1. Complete 'naive_graph_isomorphism(graph1, graph2)'
    2. Construct an NxN matrix in which each element represents
       the result of the isomorphic test between two graphs.
       The value at the intersection of row i and column j indicating
       whether the i-th and j-t graphs are isomorphic.
    3. Save the NxN matrix in './results/naive_isomorphic_test.csv'

    Args:
        graphs: A list of networkx graph objects

    """
    # Code here

    num = len(graphs)
    isomorphism_matrix = [[0] * num for _ in range(num)]

    for i in range(num):
        for j in range(num):
            if i < j:
                if naive_graph_isomorphism(graphs[i], graphs[j]):
                    isomorphism_matrix[i][j] = 1
                    isomorphism_matrix[j][i] = 1

    # Write the matrix to a CSV file
    with open('./results/naive_isomorphic_test.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in isomorphism_matrix:
            writer.writerow(row)

    pass


def main():
    # Run part 1
    graphs = part1()

    # Run part 2
    part2(graphs)


if __name__ == '__main__':
    main()
