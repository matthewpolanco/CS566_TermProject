"""
Matt Polanco
Class: CS 566
Date: 2/8/23
Assignment 3
A program that uses a specialized sorting algorithm to sort debt obligations 
"""

def interest_calculator(a_list):  # enables divide-and-conquer
    # INTENT: calculate total accrued amount (principal + interest) for each list element
    principal = a_list[0]
    interest = a_list[1] / 100 # e.g. 3.85% = 0.0385
    time = a_list[2] # time in years
    A = principal * (1+(interest*time))  # definition: total accrued amount: A = P(1 + rt)
    return A

def debt_sorter(a_list):
    '''
    INTENT: Sort the list of debt obligations in descending order of total accrued amount (principal plus interest)
    EXAMPLE: a_list = [[1000, 2, 10], [15000, 1, 30], [500, 3, 5]]
             debt_sorter(a_list) =  [575.0, 1200.0, 19500.0]
    '''
    '''
    PRECONDITION 1 (Non-Empty): a_list is a non-empty list of numbers
    
    RETURNS a_list sorted in descending order
    POSTCONDITION 1 (Multiset): a_list and old(a_list) are identical multisets
    POSTCONDITION 2 (Sorted): a_list is sorted
    '''
    listA = list(map(interest_calculator, a_list)) # calculate total accrued amount for each list element
    
    for i in range(len(listA)-2, -1, -1):
 
        key = listA[i]
 
        j = i+1
    
        # Move elements of listA[i-1..0], that are
        # less than key, to one position behind
        # of their current position
        while j <= len(listA)-1 and key < listA[j]:
                listA[j-1] = listA[j]
                j += 1
        listA[j-1] = key
    
    return listA

if __name__ == '__main__':

    l1 = [[1000, 2, 10], [15000, 1, 30], [500, 3, 5]]
    
    # TEST CASES
    # l1 = [[1000, 2, 10], [15000, 1, 30], [500, 3, 5]]
    print('debt_sorter(l1): ', l1, ' -> ', debt_sorter(l1))

