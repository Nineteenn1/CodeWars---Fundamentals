"""
above can be simplified with ternary operator:

def odd_even(n):
    return "odd number" if n%2 else "even number"
def old_young(age):
    return "children" if age<16 else "young man" if age<50 else "old man"
Task:
Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accept 1 parameters:n, n is the number of customers to buy hotdogs, different numbers have different prices (refer to the following table), return a number that the customer need to pay how much money.

number	price (cents)
n < 5	100
n >= 5 and n < 10	95
n >= 10	90
You can use if..else or ternary operator to complete it.

When you have finished the work, click "Run Tests" to see if your code is working properly.

In the end, click "Submit" to submit your code pass this kata.
"""
def sale_hotdogs(n):
    if n == 0:
        return 0
    elif n < 5:
        return n * 100
    elif n >5 and n< 10 or n == 5:
        return n * 95
    else:
        return n * 90
