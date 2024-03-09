#######################
#
# Name: Chenrui Fan
# Matriculation Number: 23-125-818
#
# Name: Francesco Lam
# Matriculation Number: 23-109-317
#
#######################

import networkx as nx
import numpy as np
import csv

from utils import load_graph, load_all_graphs, draw_graph, draw_all_graphs

# You can potentially add more code here (constants, functions, ...)

def create_index_mapping(graph):
    """
    Create a mapping from node ID to a continuous index starting from 0.
    This is because some nodes are not from 0 but 97, etc.
    """
    return {node: idx for idx, node in enumerate(graph.nodes())}

def _ullman_recursive(F, g1, g2, mapping, depth, g1_index_mapping, g2_index_mapping) -> bool:
    """
    Recursive part of the Ullman's algorithm

    Returns:
        True if g1 is a subgraph of g2 and False otherwise
    """
    # Code here

    # print('----------------------------------------------------')
    # print('depth:', depth, 'len(g1.nodes()):', len(g1.nodes()))

    if depth == len(g1.nodes()):
        # means all nodes in g1 are mapped in g2
        return True

    for u in g1.nodes():
        # if u in g1 has not found v in g2 yet, let it be
        if mapping[u] is None:
            for v in g2.nodes():
                u_idx = g1_index_mapping[u]
                v_idx = g2_index_mapping[v]
                # for debug:
                # print('u:', u, ' v:', v)
                # print('u_idx:', u_idx, ' v_idx:', v_idx)
                if F[u_idx][v_idx]:
                    # all(null) = True
                    if all((g1.has_edge(u, u2) == g2.has_edge(v, mapping[u2])) for u2 in g1.nodes() if mapping[u2] is not None):
                        
                        # now assume I can map them together
                        mapping[u] = v
                        # print(f'u-v:{u}-{v}')

                        # change F table
                        F[u_idx] = [0] * len(g2)  # Mark this row as used
                        for row in F:
                            row[v_idx] = 0 # Do not allow other u node from g1 to find this v in g2, very important!
                        F[u_idx][v_idx] = 1
                        # print(F)

                        if _ullman_recursive(F, g1, g2, mapping, depth + 1, g1_index_mapping, g2_index_mapping):
                            # return true only when depth == len(g1.nodes()), all nodes in g1 are mapped in g2
                            return True
                        # if not true, means u and v can not be mapped
                        mapping[u] = None

                        # in this case, recover F table, very very very important!!!
                        F[u_idx] = [1] * len(g2)
                        for row in F:
                            row[v_idx] = 1
                        # print(F)
    
    # if all mapping[u] is not none, but not all nodes in g1 mapping g2, then it is false, return and try other nodes
    return False


def Ullman(g1: nx.Graph, g2: nx.Graph) -> bool:
    """
    Perform the subgraph isomorphism test between g1 and g2

    Args:
        g1: A networkx graph object
        g2: A networkx graph object

    Returns:
        True if g1 is a subgraph of g2 and False otherwise
    """
    # Code here

    g1_index_mapping = create_index_mapping(g1)
    g2_index_mapping = create_index_mapping(g2)
    # initial F with all 1
    F = [[1] * len(g2) for _ in range(len(g1))]
    mapping = {node: None for node in g1.nodes()}
    return _ullman_recursive(F, g1, g2, mapping, 0, g1_index_mapping, g2_index_mapping)


if __name__ == '__main__':
    # 1. Load the graphs in the './graphs' folder

    graphs = load_all_graphs('./graphs')

    # 1.5 (You can visualize the graphs using utils.draw_all_graphs())

    output_folder = './drawings'
    draw_all_graphs(graphs, output_folder)

    # 2. Perform the Ullman's subgraph isomorphic test between all pairs of graphs.

    # test if .has_edge() works for undirected graph:
    # g1 = graphs[0]
    # print(g1.has_edge(2, 1), g1.has_edge(3, 1), g1.has_edge(1, 2))

    num = len(graphs)
    subgraph_matrix = [[0] * num for _ in range(num)]

    for i, g1 in enumerate(graphs):
        for j, g2 in enumerate(graphs):
            if i != j:
                if Ullman(g1, g2):
                    print(f'Graph {i} is a subgraph of Graph {j}')
                    subgraph_matrix[i][j] = 1
                    subgraph_matrix[j][i] = 1
                # else:
                #     print(f'Graph {i} is not a subgraph of Graph {j}')

    # Write the matrix to a CSV file
    with open('./results/Ullman_subgraph_isomorphism_test.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in subgraph_matrix:
            writer.writerow(row)

    pass
