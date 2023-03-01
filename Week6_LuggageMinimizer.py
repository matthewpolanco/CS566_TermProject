"""
Matt Polanco
Class: CS 566
Date: 3/1/23
Assignment 6
A program that uses greedy algorithm to minimize luggage for travel
"""

# Class to represent items to pack with respective weights and capacity of bag/luggage
class Luggage:
    def __init__(self, weights, capacity):
        self.weights  = weights
        self.capacity = capacity
        self.length = len(weights)
 
## Inspired by the Bin Packing Problem
## Work Cited: 
## https://iq.opengenus.org/bin-packing-problem/ 
def augment_greedily(weights, capacity, length):
    '''
    INTENT: Find the minimum number of bags/luggage needed to pack all items with respective weights without
            going over capacity. Algorithm starts by packing the largest weight first. If the subsequent weight
            does not fit, the next bag/luggage will be used.
    EXAMPLE: see next section
    '''
    '''
    PRECONDITION 1 (Sort): List of weights must be sorted in descending order
    PRECONDITION 2 (Positive): Weights is a non-null list of positive integers
    
    RETURNS a_part_solution = minimum number of bags/luggage needed to pack all items
    POSTCONDITION 1 (Minimal): a_part_solution is the minimum possible value without going over capacity
    '''
    # DEFINITION: a_part_solution = number of bags/luggage
    a_part_solution = 0
     
    # DEFINITION: a_space = List for maximum amount of bags/luggage
    a_space = [0 for item in range(length)]
     
    # Go throughs items to pack
    for item in range(length):
       
        # Look for first bag/luggage able to hold weight[item]
        current_luggage = 0
        while(current_luggage < a_part_solution):
            if (a_space[current_luggage] >= weights[item]):
                a_space[current_luggage] = a_space[current_luggage] - weights[item]
                break
            current_luggage+=1
             
        # If no bag/luggage can hold weight[item], increment number of bags/luggage
        if (current_luggage == a_part_solution):
            a_space[a_part_solution] = capacity - weights[item]
            a_part_solution = a_part_solution + 1
    return a_part_solution
     
def LuggageMinimizer(Luggage):
    # INTENT: Greedily minimze the number of bags/luggage needed to packs given items with respective weights
    # RETURN: minimum number of bags/luggage

    # Sort weights in descending order
    Luggage.weights.sort(reverse = True)
    
    # Build solution greedily
    complete_solution = augment_greedily(Luggage.weights, Luggage.capacity, Luggage.length)
    
    return complete_solution

if __name__ == '__main__':
    # TEST CASES
    weights = [15, 20, 1, 1, 4, 35, 17, 5, 8, 2, 20, 27]
    capacity = 50
    
    print("Minimum number of bags/luggage needed is", LuggageMinimizer(Luggage(weights, capacity)))

