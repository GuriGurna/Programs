'''Write a function, called nestEggVariable, which takes three arguments: a salary
(salary), a percentage of your salary to save (save), and a list of annual growth
percentages on investments (growthRates). The length of the last argument defines the
number of years you plan to work; growthRates[0] is the growth rate of the first year,
growthRates[1] is the growth rate of the second year, etc. (Note that because the
retirement fund’s initial value is 0, growthRates[0] is, in fact, irrelevant.) This function
should return a list, whose values are the size of your retirement account at the end of
each year.
'''

def nestEggVariable(salary, save, growthRates):
    retirement_account = []
    
    for i in range(len(growthRates)):
       
        if i == 0:
            retirement_account.append(salary*save*0.01)
       
        else:
            last_year_amount = retirement_account[-1]
            retirement_account.append(last_year_amount* (1 + 0.01 * growthRates[i]) + salary * save * 0.01) 

    return retirement_account        

print(nestEggVariable(100000, 15, [5 ,4 , 5 , 5 ,6]))