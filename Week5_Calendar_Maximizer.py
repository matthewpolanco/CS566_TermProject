"""
Matt Polanco
Class: CS 566
Date: 2/22/23
Assignment 5
A program that uses dynamic programming to optimize ones calendar.
"""

# Class to represent an Event such as an activity/meeting
class Event:
    def __init__(self, begin_time, end_time, value):
        self.begin_time  = begin_time
        self.end_time = end_time
        self.value = value
        
## BinarySearch algorithm taken from https://www.geeksforgeeks.org/python-program-for-binary-search ##
def binarySearch(Event, begin_time_index):
    # INTENT: find the latest event that doesn't conflict with the current event
    # RETURN: latest event or -1 if all events conflict with current event

    low = 0
    high = begin_time_index - 1
    mid = 0
 
    while low <= high:
        mid = (low + high) // 2
        if Event[mid].end_time <= Event[begin_time_index].begin_time:
            if Event[mid + 1].end_time <= Event[begin_time_index].begin_time:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1
 
## Inspired by the Weighted Job Scheduling Problem
## Work Cited: 
## https://www.educative.io/answers/what-is-weighted-job-scheduling-in-dynamic-programming
## https://iq.opengenus.org/weighted-job-scheduling/
def calendar(Events):
    '''
    INTENT: Finds the maximum value of a list of events consisting of beginTime, endTime, and the value of attending. 
            Goal is to maximize the number of activities that can be accomplished in a given time frame such as day.
    EXAMPLE: see next section
    '''
    '''
    PRECONDITION 1 (Time): times must be in military time 0000-2400
    PRECONDITION 2 (Event): list of Events must be inputted
    
    RETURNS optimal value of events
    POSTCONDITION 1 (Optimal): value return is the highest possible value without conflicting events
    '''
   
    # Events sorted by end_time
    Events = sorted(Events, key = lambda x: x.end_time)
 
    # Create list to store subproblem solutions
    n = len(Events)
    sub_solutions = [0 for i in range(n)]
    sub_solutions[0] = Events[0].value;
 
    # Gather subproblem solutions  
    for i in range(1, n):
 
        # Find value including the current Event
        add_value = Events[i].value
        latest_nonconflict_event = binarySearch(Events, i)
        # check if nonconflict event exists
        if (latest_nonconflict_event != -1):
            add_value += sub_solutions[latest_nonconflict_event];
            
        # add the highest value out of current and previous    
        if add_value > sub_solutions[i - 1]:
            sub_solutions[i] = add_value
        else:
            sub_solutions[i] = sub_solutions[i - 1]
 
    return sub_solutions[n-1]

if __name__ == '__main__':
    
    # TEST CASES
    Events = [Event(830, 900, 50), Event(845, 930, 80), Event(1100, 1200, 170), Event(1400, 1530, 200)]
    print("Optimal value of calendar: ", calendar(Events))

