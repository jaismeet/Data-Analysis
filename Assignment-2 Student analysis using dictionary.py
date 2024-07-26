from tabulate import tabulate

data_dict = {
    "std101": {
        "stdname": "Ashish Kumar",
        "standard": "10th",
        "Age": 15,
        "Hindi": 67,
        "English": 89,
        "Maths": 87,
        "Science": 89,
        "Computer": 90,
        "Total": 422
    },
    "std102": {
        "stdname": "Abhishek Kumar",
        "standard": "10th",
        "Age": 14,
        "Hindi": 85,
        "English": 45,
        "Maths": 48,
        "Science": 90,
        "Computer": 45,
        "Total": 313
    },
    "std103": {
        "stdname": "Aman",
        "standard": "10th",
        "Age": 15,
        "Hindi": 23,
        "English": 56,
        "Maths": 78,
        "Science": 78,
        "Computer": 67,
        "Total": 302
    },
    "std104": {
        "stdname": "Rahul",
        "standard": "10th",
        "Age": 14,
        "Hindi": 45,
        "English": 67,
        "Maths": 45,
        "Science": 45,
        "Computer": 56,
        "Total": 258
    },
    "std105": {
        "stdname": "Ruby",
        "standard": "10th",
        "Age": 13,
        "Hindi": 89,
        "English": 67,
        "Maths": 89,
        "Science": 93,
        "Computer": 65,
        "Total": 403
    },
    "std106": {
        "stdname": "Suman",
        "standard": "10th",
        "Age": 13,
        "Hindi": 90,
        "English": 46,
        "Maths": 67,
        "Science": 67,
        "Computer": 67,
        "Total": 337
    },
    "std107": {
        "stdname": "Saurabh",
        "standard": "10th",
        "Age": 15,
        "Hindi": 45,
        "English": 23,
        "Maths": 34,
        "Science": 45,
        "Computer": 34,
        "Total": 181
    },
    "std108": {
        "stdname": "Sumit",
        "standard": "10th",
        "Age": 14,
        "Hindi": 23,
        "English": 45,
        "Maths": 67,
        "Science": 78,
        "Computer": 90,
        "Total": 303
    },
    "std109": {
        "stdname": "Kamlesh",
        "standard": "10th",
        "Age": 15,
        "Hindi": 45,
        "English": 56,
        "Maths": 78,
        "Science": 99,
        "Computer": 67,
        "Total": 345
    },
    "std110": {
        "stdname": "Rohan",
        "standard": "10th",
        "Age": 15,
        "Hindi": 34,
        "English": 12,
        "Maths": 24,
        "Science": 45,
        "Computer": 56,
        "Total": 171
    }
}

# Prepare the data for tabulat
table_data = []
for std_id, info in data_dict.items():
    row = [std_id] + list(info.values())
    table_data.append(row)
    
headers=["Student ID","Name","Standard","Age","Hindi","English","Maths","Science","Computer","Total"]

# Display the data in a table format
print(tabulate(table_data, headers=headers, tablefmt="pretty"))

# the students with English marks greater than 50
students = [info['stdname'] for info in data_dict.values() if info['English'] > 50]

print("\nStudents with English marks greater than 50:")
for student in students:
    print(student)
    
print("_--------------------------------------------------------------")

# Find the top 4 scorers in Maths
top_four_maths = sorted(data_dict.items(), key=lambda x: x[1]['Maths'], reverse=True)[:4]

# Extract the name and age of the top 4 scorers
top_four_maths_info = [(info['stdname'], info['Age']) for _, info in top_four_maths]

# Print the results
print("\nTop 4 scorers in Maths:")
for name, age in top_four_maths_info:
    print("Name is : ", name, " , Age is : ",age)
    
    
print("Bottom 3 scorer in computer: ")
    
    
# Sort the data based on the Computer score
sorted_data = sorted(data_dict.items(), key=lambda x: x[1]["Computer"])

# Extract the bottom three scorers in Computer
bottom_three = sorted_data[:3]

# Prepare the data for tabulate
bottom_three_data = []
for std_id, info in bottom_three:
    row = [std_id, info["stdname"], info["Age"]]
    bottom_three_data.append(row)
    
for i in bottom_three_data:
    print(*i)
