# 1. Suppose you have a dataset containing daily temperature readings for a city, and you
# want to identify days with extreme temperature conditions. Find days where the
# temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees
# Celsius (cold day).

import numpy as np

temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4.5, 3.4, 2.5])

hot_days = temperatures > 35
cold_days = temperatures < 5


hot_day_indices = np.where(hot_days)[0] + 1 
cold_day_indices = np.where(cold_days)[0] + 1  

hot_temperatures = temperatures[hot_days]
cold_temperatures = temperatures[cold_days]

print("Hot Days:")
print("Day       " , "Temperature (°C)")
for i in range(len(hot_day_indices)):
    print(hot_day_indices[i],"        ",hot_temperatures[i])

print("\nCold Days:")
print("Day       " , "Temperature (°C)")
for i in range(len(cold_day_indices)):
    print(cold_day_indices[i],"        ",cold_temperatures[i])
    
    
# 2. Suppose you have a dataset containing monthly sales data for a company, and you
# want to split this data into quarterly reports for analysis and reporting purposes.

import numpy as np

monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

quarterly_sales = monthly_sales.reshape(4, 3)

# print(quarterly_sales)
print("Ouarter 1 sales (in thousands of dollars ) : \n" , quarterly_sales[0])
print("Ouarter 2 sales (in thousands of dollars ) : \n" , quarterly_sales[1])
print("Ouarter 3 sales (in thousands of dollars ) : \n" , quarterly_sales[2])
print("Ouarter 4 sales (in thousands of dollars ) : \n" , quarterly_sales[3])


# 3. Suppose you have a dataset containing customer data, and you want to split this data
# into two groups: one group for customers who made a purchase in the last 30 days and
# another group for customers who haven't made a purchase in the last 30 days.

import numpy as np  

customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])

active_customer = last_purchase_days_ago[last_purchase_days_ago <= 30 ]
i = np.where(active_customer)[0]
customer_id = customer_ids[i]
print("Active Customer (Last Purchase < = 30 days ago) : \n" ,customer_id)

inactive_customer = np.where(last_purchase_days_ago > 30)[0]
customer_id = customer_ids[inactive_customer]
print("Inactive Customer (Last Purchase > 30 days ago) : \n" ,customer_id)


# 4.Suppose you have two sets of employee data—one containing information about
# full-time employees and another containing information about part-time employees. You
# want to combine this data to create a comprehensive employee dataset for HR analysis.

import numpy as np

# Employee data for full-time employees
full_time_employees = np.array([
    [101, 'John Doe','Full-Time', 55000],
    [102, 'Jane Smith','Full-Time', 60000],
    [103, 'Mike Johnson','Full-Time', 52000]
])

# Employee data for part-time employees
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])

combined_employee_data = np.vstack((full_time_employees, part_time_employees))
# print(combined_employee_data)

id = combined_employee_data[:, 0]
emp_name = combined_employee_data[:, 1]
emp_type = combined_employee_data[:, 2]
emp_salary = combined_employee_data[:, 3]

print("Combined Employee Data :")
for i in range(len(id)):
    print("Employee ID :", id[i], ", Name :", emp_name[i], ", Type :", emp_type[i], ", Salary :", emp_salary[i])
    
print("---------------------------------------- Assignment ------------------------------------------")

# 1.How to find the mean of every NumPy array in the given list?

import numpy as np

list = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
]
means = [np.mean(array) for array in list]
print(means) 


# 2.Compute the median of the flattened NumPy array

import numpy as np 

x_odd = np.array([1, 2, 3, 4, 5, 6, 7])
print("Printing the original array : \n",x_odd)
median = np.median(x_odd)
print("The median of the array is : \n",median)


# 3.Compute the standard deviation of the NumPy array

import numpy as np

list = [20, 2, 7, 1, 34]

arr = np.array(list)
print("arr : ", arr)
standard_deviation = np.std(arr)
print("std of arr : " , standard_deviation)

arr = np.array(list , dtype = np.float32)
standard_deviation = np.std(arr)
print("More precision with Float32 \nstd of arr : ",standard_deviation)

arr = np.array(list, dtype = np.float64)
standard_deviation = np.std(arr)
print("More accuracy with Float64 \nstd of arr : ",standard_deviation)


# 4.Suppose you have a CSV file named 'house_prices.csv' with price information, and
# you want to perform the following operations:
# ● 1.Read the data from the CSV file into a NumPy array.
# ● 2.Calculate the average of house prices.
# ● 3.Identify house price above the average.
# ● 4.Save the list of high prices to a new CSV file.

import numpy as np

house_prices = np.genfromtxt('house_prices.csv', delimiter=',', skip_header=1, usecols=0)

average_price = np.mean(house_prices)
print(f"Average House Price: {average_price}")

high_prices = house_prices[house_prices > average_price]
print(high_prices)
np.savetxt('high_house_prices.csv', high_prices, delimiter=',', header='price',fmt='%.2f')