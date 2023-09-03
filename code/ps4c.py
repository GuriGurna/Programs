'''Write a function, called postRetirement, which takes three arguments: an initial amount
of money in your retirement fund (savings), a list of annual growth percentages on
investments while you are retired (growthRates), and your annual expenses (expenses).
Assume that the increase in the investment account savings is calculated before
subtracting the annual expenditures (as shown in the above table). Your function should
return a list of fund sizes after each year of retirement, accounting for annual expenses
and the growth of the retirement fund. Like problem 2, the length of the growthRates
argument defines the number of years you plan to be retired.
Note that if the retirement fund balance becomes negative, expenditures should continue
to be subtracted, and the growth rate comes to represent the interest rate on the debt
(i.e. the formulas in the above table still apply).'''

def postRetirement(savings, growthRates, expenses):
    bank_balance = []
    
    for i in growthRates:
        bank_balance.append(savings * (1 + 0.01 * i) - expenses)

    return bank_balance

print(postRetirement(1000000 ,[5,6,7,4,5,7] ,100000))    