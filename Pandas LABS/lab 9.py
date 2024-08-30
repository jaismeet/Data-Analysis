import pandas as pd
df = pd.read_csv("salesdata.csv")

# Lab1: Write a Pandas program to create a Pivot table and find the total sale
# amount region wise, manager wise, sales man wise.
pivot1 = df.pivot_table(values='Sale Amount', index=['Region', 'Manager', 'Salesman'], aggfunc='sum')
print(pivot1)
print()


# Lab2: Write a Pandas program to create a Pivot table and find the item wise
# unit sold.
pivot2 = df.pivot_table(values='Units Sold', index='Item', aggfunc='sum')
print(pivot2)
print()


# Lab3: Write a Pandas program to create a Pivot table and find the region
# wise, item wise unit sold.
pivot3 = df.pivot_table(values='Units Sold', index=['Region', 'Item'], aggfunc='sum')
print(pivot3)
print()


# Lab4: Write a Pandas program to create a Pivot table and count the
# manager wise sale and mean value of sale amount.
pivot4 = df.pivot_table(values='Sale Amount', index='Manager', aggfunc=['count', 'mean'])
print(pivot4)
