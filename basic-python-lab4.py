print("----------------------------------------- Assignment - List --------------------------------------")

# 1. Write a Python program to sum all the items in a list.

numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)
print("The sum of all items in the list is:", total_sum)

# 2. Write a Python program to get the largest and smallest number from a list without built in function.

numbers = [3, 5, 1, 9, 2, 8]
largest = numbers[0]
smallest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)

# 3. Write a Python program to find duplicate values from a list and display those.

numbers = [1, 2, 3, 4, 2, 5, 3, 6, 7, 8, 5]
seen = set()
duplicates = set()
for number in numbers:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)
duplicates_list = list(duplicates)
print("Duplicate values in the list are:", duplicates_list)

# 4. Write a Python program to split a given list into two parts where the length of the first
# part of the list is given.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list: 3
# Splitted the said list into two parts:
# ([1, 1, 2], [3, 4, 4, 5, 1])

original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3

first_part = original_list[:length_of_first_part]
second_part = original_list[length_of_first_part:]

print("Original list:")
print(original_list)
print("Length of the first part of the list: ",length_of_first_part)
print("Splitted the said list into two parts:")
print((first_part, second_part))

# 5. Write a Python program to traverse a given list in reverse order, and print the
# elements with the original index.

original_list = ['red', 'green', 'white', 'black']

for i in range(len(original_list) - 1, -1, -1):
    element = original_list[i]
    print(element)


print("----------------------------------------- Assignment - Dictionary --------------------------------------")

# 1. Write a Python program and calculate the mean of the below dictionary.
# test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
values = test_dict.values()
sum_values = sum(values)
num_values = len(values)
mean = sum_values / num_values
print("Mean:", mean)

# 2.Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = dic1.copy()
result.update(dic2)
result.update(dic3)
print("Concatenated dictionary using update():", result)


# 3.Write a Python program to get the key, value and item in a dictionary.
# input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Key","   ","Value")
for key, value in dict_num.items():
    print(key,"    ",value)


# 4.Write a Python program to get the key, value and item in a dictionary.
# Input: input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}

input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
filtered_dict = {key: value for key, value in input_dict.items() if value is not None}
print("dict with empty items Dropped :")
print(filtered_dict)

print("----------------------------------------- Assignment - Tuple --------------------------------------")

# 1. Write a Python program to find the number of times 4 appears in the tuple.
# Input: tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )

tuplex = (2, 4, 5, 6, 2, 3, 4, 4,7)
counts= tuplex.count(4)
print("The number of times 4 appears in the tuple:", counts)

# 2.Write a Python program to convert a list to a tuple.
# Input: listx = [5, 10, 7, 4, 15, 3]

listx = [5, 10, 7, 4, 15, 3]
tuplex = tuple(listx)
print("Converted tuple:", tuplex)

# 3. Write a Python program to calculate the sum of the numbers in a given tuple.
# Input: tuples_list = [(1, 2), (3, 4), (5, 6)]

tuples_list = [(1, 2), (3, 4), (5, 6)]
total_sum = 0
for tup in tuples_list:
    total_sum += sum(tup)
print("Sum of tuple is:", total_sum)

# 4.Write a python program and iterate the given tuples
# Input:
# employee1 = ("John Doe", 101, "Human Resources", 60000)
# employee2 = ("Alice Smith", 102, "Marketing", 55000)
# employee3 = ("Bob Johnson", 103, "Engineering", 75000)

employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

employees = [employee1, employee2, employee3]
print("Employee Records :")
for employee in employees:
    name, emp_id, department, salary = employee
    print("\nName : ", name)
    print("Employee ID : ", emp_id)
    print("Department : ", department)
    print("Salary : ", salary)
    

print("----------------------------------------- Assignment - Set--------------------------------------")

# 1. Write a Python program to Get Only unique items from two sets.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_items = set1.union(set2)
print("Unique items from both sets:", unique_items)

# 2. Write a Python program to Return a set of elements present in Set A or B, but
# not both.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
symmetric_diff = set1.symmetric_difference(set2)
print("Elements present in Set A or B, but not both:", symmetric_diff)

# 3. Write a Python program to Check if two sets have any elements in common. If
# yes, display the common elements.

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90,10}
common_elements = set1.intersection(set2)
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements.")

# 4. Write a Python program to Remove items from set1 that are not common to
# both set1 and set2.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1 &= set2
print("Updated set1 with common elements:", set1)

