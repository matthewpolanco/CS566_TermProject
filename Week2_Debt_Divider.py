"""
Matt Polanco
Class: CS 566
Date: 2/1/23
Assignment 2
A program that uses the divide & conquer algorithm to calculate debt repayment 
"""

def division(an_int1):  # enables divide-and-conquer
    # INTENT: split debt equally into smaller, more managable payments
    split = an_int1/2  # definition
    # PRECONDITION: an_int1 > 0
    # RETURNS an_int1 divided by 2
    return split


def debt_calculator(monthly_income, total_debt, month_counter = 1):
    '''
    INTENT: Find the number of months and monthly payment required to pay off a debt within budget contraints.
    EXAMPLE: debt_calculator(monthly_income = 5000, total_debt = 18000) = $562.50 for 32 months
    '''
    '''
    PRECONDITION 1 (Positive Num): monthly_income and total_debt are positive numbers greater than 0
    
    RETURNS monthly_payment, num_months
    POSTCONDITION 1 (Budget): monthly_payment is less than or equal to 20% of monthly_income
    POSTCONDITION 2 (Payment): DebtSplit: total_debt = monthly_payment 
                              i.e. eventually debt will be divided to a point where it becomes your monthly payment
    '''
    DTI = 0.20 # definition: debt-to-income ratio

    # OUTCOME 1 = a (Solvabale Immediately?): 
    # EITHER postcondition holds & this returned OR total_debt/monthly_income > 20%
    if total_debt/monthly_income <= DTI:
        # OUTCOME 3 = c1 (Postcondition)
        monthly_payment = total_debt
        num_months = month_counter
        return monthly_payment, num_months
    # OUTCOME 2 = b1 (Split): DebtSplit: division(total_debt) = monthly_payment
    else: 
        return debt_calculator(monthly_income, division(total_debt), month_counter*2) # O3 is achieved recursively

if __name__ == '__main__':
    # TEST CASES
    print('debt_calculator(5000, 18000) =', debt_calculator(5000, 18000)) # $562.50 for 32 months
    print('debt_calculator(5000, 18000) =', debt_calculator(1, 25000)) # worst case: debt_calc(1, n) where n is any large positive number
    print('debt_calculator(5000, 18000) =', debt_calculator(5, 1)) # best case: debt_calc(n, 1) where n is any large positive number
    
