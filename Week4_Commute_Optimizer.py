"""
Matt Polanco
Class: CS 566
Date: 2/15/23
Assignment 4
A program that builds upon Dijkstra's algorithm to find
shortest path from a source to a destination that passes through a stop.
"""

#  Dijkstra’s algorithm taken from Professor Braude's dijksta.py under 'Live Classroom Slides and Materials'
#  My added code expands upon the algorithm for a specialized business case
import heapq

def commute_optimizer(a_graph, a_source, a_destination, a_stop, visited = False):
    """
    INTENT: Expand Dijkstra's algorithm to find shortest path from a_source to a_destination
            that passes through a_stop.
    EXAMPLE: see below

    PRECONDITION 1 (a_graph): A dictionary representing a non-negative weighted graph_1,
    key = vertex and value = dictionary of neighboring vertices and edge weights.

    PRECONDITION 2 (a_source): a_source is a key in a_graph

    RETURNS: a_total_cost
    POSTCONDITION: a_total_cost the minimum cost of passing through the necessary a_stop on the way to a_destination
    """
    # Call the algorithm again to find optimized path from a_stop to a_destination
    if not visited:
        stop_distances = commute_optimizer(a_graph, a_destination, a_stop, a_stop, visited = True)
        stop_cost = stop_distances[a_stop]
        
    # OUTCOME 1 = a (Partly known): for every n in return_tree, EITHER value of n = infinity
    # OR value of n is the cost of the cheapest path from a_source
    return_tree = {vertex: float('infinity') for vertex in a_graph}
    return_tree[a_source] = 0
    
    # OUTCOME 2 (candidate_nodes): ... is a heap of the nodes in return_tree ordered by value
    candidate_nodes = [(0, a_source)]
    
    # OUTCOME 3 = b (Complement): candidate_nodes is empty
    while candidate_nodes:
        # Extract the vertex with the minimum distance from the source vertex
        (current_distance, current_node) = heapq.heappop(candidate_nodes)
        # Update the return_tree of its neighbors and add them to candidate_nodes
        # (unnecessarily checks nodes in candidate_nodes)
        for neighbor_, weight_ in a_graph[current_node].items():
            distance_ = current_distance + weight_
            if distance_ < return_tree[neighbor_]:
                return_tree[neighbor_] = distance_
                heapq.heappush(candidate_nodes, (distance_, neighbor_))
    
    # Check if stop has been passed through yet                     
    if not visited:
        # This will be the final return output
        # cost of a_source->a_stop + cost of a_stop->a_destination = cost of a_source->a_stop->a_destination
        a_total_cost = return_tree[a_stop] + stop_cost, return_tree[a_destination]
        return a_total_cost
    else:
        return return_tree


if __name__ == '__main__':
    
    # TEST CASES
    '''
    A-1-B-2-F   H-3-I  # all node values are infinity to begin
    |  /|   |\  |\ /|
    4 2 5   2 4 1 5 3
    |/  |   |  \|/ \|
    C-1-D-3-E-6-G-2-J
    '''
    graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5, 'F': 2},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1, 'E': 3},
            'E': {'D': 3, 'F': 2, 'G': 6},
            'F': {'B': 2, 'E': 2, 'G': 4},
            'G': {'E': 6, 'F': 4, 'H': 1, 'I': 5, 'J': 2},
            'H': {'G': 1, 'I': 3, 'J': 5},
            'I': {'G': 5, 'H': 3, 'J': 3},
            'J': {'G': 2, 'H': 5, 'I': 3}
        }
    distances = commute_optimizer(graph, a_source = 'A', a_destination = 'J', a_stop = 'C')
    '''
    # This is the optimized graph using Dijkstra's Algorithm with source 'A' and destination 'J' for reference
    A0-1-B1-2-F3   H8-3-I11
    |   /|    |\   |\  /|
    4  2 5    2 4  1 5  3
    |/   |    |  \ |/  \|
    C3-1-D4-3-E5-6-G7-2-J9
    '''
    print("Starting from 'A', go to 'J' with a stop at 'C'.")
    print(distances[0], "minutes with a stop.", distances[1], "minutes without a stop.\n")
    
    
    distances2 = commute_optimizer(graph, a_source = 'B', a_destination = 'G', a_stop = 'H')
    print("Starting from 'B', go to 'G' with a stop at 'H'.")
    print(distances2[0], "minutes with a stop.", distances2[1], "minutes without a stop.\n")
    
    
    distances3 = commute_optimizer(graph, a_source = 'A', a_destination = 'C', a_stop = 'I')
    print("Starting from 'A', go to 'C' with a stop at 'I'.")
    print(distances3[0], "minutes with a stop.", distances3[1], "minutes without a stop.\n")

