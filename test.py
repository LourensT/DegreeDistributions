from DegreeDistributions import DegreeDistribution, SizeBiasedDegreeDistribution, RandomFriendDegreeDistribution

import networkx as nx

import matplotlib.pyplot as plt

def test_sums_to_one(pmf_dict, epsilon = 0.00001):
    probability_sum = sum(pmf_dict.values())
    if abs(probability_sum - 1) < epsilon:
        return True
    else:
        return False

score = 0
tests = 0

G = nx.erdos_renyi_graph(1000, 0.3)

u = DegreeDistribution(G)
if test_sums_to_one(u):
    print("1. test of DegreeDistribution(): PASSED")
    score += 1
    tests += 1
else:
    print("1. test of DegreeDistribution(): FAILED")
    tests += 1

v = RandomFriendDegreeDistribution(G)
if test_sums_to_one(v):
    print("1. test of RandomFriendDegreeDistribution: PASSED")
    score += 1
    tests += 1
else:
    print("1. test of RandomFriendDegreeDistribution: FAILED")
    tests += 1

w = SizeBiasedDegreeDistribution(G)
if test_sums_to_one(w):
    print("1. test of SizeBiasedDegreeDistribution: PASSED")
    score += 1
    tests += 1
else:
    print("1. test of SizeBiasedDegreeDistribution: FAILED")
    tests += 1

plt.scatter(x=u.keys(), y=u.values(), color='blue')
plt.scatter(x=v.keys(), y=v.values(), color='red')
plt.scatter(x=w.keys(), y=w.values(), color='green')
plt.show()

print('\n')
print("Test Results: {} out of {} tests passed.".format(score, tests))