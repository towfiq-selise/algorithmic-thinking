"""
Author: Towfiqul Islam
Algorithmic Thinking (Part 1)
Application 1: Analysis of Citation Graphs
"""

import alg_load_graph
import alg_dpa_trial
from degree_distribution_for_graphs import in_degree_distribution

CITATION_URL = "https://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"
citation_graph = alg_load_graph.load_graph(CITATION_URL)

cite_dist = in_degree_distribution(citation_graph)

"""
Question 3
"""
all_vertex = citation_graph.keys()
out_degree = 0
for dummy_vertex in citation_graph.keys():
    out_degree += len(citation_graph[dummy_vertex])

ave_out = out_degree/27770.0    
print(ave_out)


"""
Question 4
"""
m = 13
n = 27770

dpa_graph = make_complete_graph(m)
trial = alg_dpa_trial.DPATrial(m)

for index in range(m,n):
    nbd = trial.run_trial(m)
    dpa_graph[index] = nbd
    
dpa_dist = in_degree_distribution(dpa_graph)
