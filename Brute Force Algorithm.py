import time 
import networkx as nx
from itertools import permutations

def all_permutations(g):
    n = g.number_of_nodes()
    shortest_tour = None

    for tour in permutations(range(n)) :
      tour_len = 0
      valid = True

      # length of the tour 
      for i in range(len(tour)) :
      	if not g.has_edge(tour[i], tour[i-1]) :
      		valid = False
      		break
      	else :
      		tour_len += g[tour[i-1]][tour[i]]['weight']

      # may be a valid cycle with the shortest length
      if valid and (shortest_tour is None or tour_len < shortest_tour) :
        shortest_tour = tour_len

    return shortest_tour


