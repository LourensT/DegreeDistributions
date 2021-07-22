import networkx as nx
from networkx.classes.function import degree

import numpy as np

def DegreeDistribution(G):
    pmf = {}
    degrees = list(G.degree((n for n in G.nodes())).values())
    n = len(degrees)
    for v in degrees:
        if v in pmf:
            pmf[v] += 1/n
        else:
            pmf[v] = 1/n
    
    return pmf


def RandomFriendDegreeDistribution(G):

    # size of network
    n = G.number_of_nodes()
    
    # setting the pmf
    pmf = {}
    for node in G.nodes():
        
        # calculate probability of selecting this node
        adjacent = G.adj[node]
        prob = (1 / n) * sum([1/G.degree(v) for v in adjacent]) # these probs for all nodes sum to 1

        # update the empirical pmf
        k = G.degree(node)
        if k in pmf:
            pmf[k] += prob
        else:
            pmf[k] = prob

    return pmf

def SizeBiasedDegreeDistribution(G):
    pass

