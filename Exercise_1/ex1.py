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

from utils import load_graph, load_all_graphs, draw_graph, draw_all_graphs

# You can potentially add more code here (constants, functions, ...)


def _ullman_recursive(F, g1, g2, mapping) -> bool:
    """
    Recursive part of the Ullman's algorithm

    Returns:
        True if g1 is a subgraph of g2 and False otherwise
    """
    # Code here

    # 如果所有的 g1 节点都被映射，则返回 True
    if all(mapped for mapped in mapping):
        return True

    # 选择下一个未映射的 g1 节点
    u = next((node for node in g1.nodes if not mapping[node]), None)

    # 尝试将 g1 节点 u 映射到所有 g2 节点
    for v in g2.nodes:
        if F[u][v] and all((g1.has_edge(u, other_u) == g2.has_edge(v, other_v) for other_u, other_v in mapping.items() if other_v is not None)):
            mapping[u] = v
            if _ullman_recursive(F, g1, g2, mapping):
                return True
            mapping[u] = None

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

    F = [[1 for _ in range(len(g2))] for _ in range(len(g1))]  # 初始 F 全为 1
    mapping = {node: None for node in g1.nodes}  # 初始化映射字典
    return _ullman_recursive(F, g1, g2, mapping)

    return False


if __name__ == '__main__':
    # 1. Load the graphs in the './graphs' folder

    graphs = load_all_graphs('./graphs')

    # 1.5 (You can visualize the graphs using utils.draw_all_graphs())

    # output_folder = './results'
    # draw_all_graphs(graphs, output_folder)

    # 2. Perform the Ullman's subgraph isomorphic test between all pairs of graphs.

    for i, g1 in enumerate(graphs):
        for j, g2 in enumerate(graphs):
            if i != j:  # 不和自身比较
                if Ullman(g1, g2):
                    print(f'Graph {i} is a subgraph of Graph {j}')

    pass
