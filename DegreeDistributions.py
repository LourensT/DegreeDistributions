import networkx as nx
from networkx.classes.function import degree

import numpy as np

def DegreeDistribution(G, tail=False):
    pmf = {}
    degrees = [G.degree(n) for n in G.nodes()]
    n = len(degrees)
    for v in degrees:
        if v in pmf:
            pmf[v] += 1/n
        else:
            pmf[v] = 1/n

    assert abs(sum(pmf.values()) - 1.) < 0.0001, f"pmf does not sum to one, but to {sum(pmf.values())}"
    
    if tail:
        return _tailDistribution(pmf)
    else:
        return pmf


def RandomFriendDegreeDistribution(G, tail=False):

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

    assert abs(sum(pmf.values()) - 1.) < 0.0001, "pmf does not sum to one"

    if tail:
        return _tailDistribution(pmf)
    else:
        return pmf


def SizeBiasedDegreeDistribution(G, tail=False):
    # get normal degree distribution
    pmf_normal = DegreeDistribution(G)

    # get expectation of normal distribution
    expectation = sum(p*k for (p,k) in pmf_normal.items())

    # apply size-biased definition (1.2.2)
    pmf = {}
    for k in pmf_normal:
        pmf[k] = (k/expectation) * pmf_normal[k]
    
    assert abs(sum(pmf.values()) - 1.) < 0.0001, "pmf does not sum to one"

    if tail:
        return _tailDistribution(pmf)
    else:
        return pmf


'''
tail 
'''
def _tailDistribution(pmf):
    keys = list(pmf.keys())
    keys.sort()

    tail = {}
    prev = 1
    for key in keys:
        tail[key] = prev - pmf[key]
        prev = tail[key]
    
    tail.pop(keys[-1])

    return tail