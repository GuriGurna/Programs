'''.
Write a function, called nestEggFixed, which takes four arguments: a salary, a
percentage of your salary to save in an investment account, an annual growth percentage
for the investment account, and a number of years to work. This function should return a
list, whose values are the size of your retirement account at the end of each year, with
the most recent year’s value at the end of the list.
Complete the implementation of:
Write your code in the appropriate place in the template. To test your function,
run the test cases in the test function testNestEggFixed(). You should add additional
test cases to this function to further test your code.
This first model is pretty simple. Clearly, the market does not grow at a constant rate. So a
ps4.py
def nestEggFixed (salary, save, growthRate, years):'''


def nestEggFixed(salary, save, growthRate, years):
    retirement_savings =[]
    
    for i in range(years):
        if i==0:
            retirement_savings.append(salary*save*0.01)

        else:
            last_year_amount = retirement_savings[i-1]
            retirement_savings.append(last_year_amount* (1 + 0.01 * growthRate) + salary * save * 0.01)    
    
    return retirement_savings        

print(nestEggFixed(100000, 15, 7, 10))