record1 =['stdid' ,'stdname','standard','age','hindi','english','maths','science','computer','total']
record2=['std101','Ashish kumar','10th',15,67,89,87,89,90,422]
record3=['std102','Abhishek kunar','10th',14,85,45,48,90,45,313]
record4=['std103','Aman','10th',15,23,56,78,78,67,302]
record5=['std104','Rahul','10th',14,45,67,45,45,56,258]
record6=['std105','Ruby','10th',13,89,67,89,93,65,403]
record7=['std106','Suman','10th',13,90,46,67,67,67,337]
record8=['std107','Saurabh','10th',15,45,23,34,45,34,181]
record9=['std108','Sumit','10th',14,23,45,67,78,90,303]
record10=['std109','kamlesh','10th',15,45,56,78,99,67,345]
record11=['std110','Rohan','10th',15,34,12,24,45,56,171]


studentrecord=[record1,record2,record3,record4,record5,record6,record7,record8,record9,record10,record11]
print(studentrecord)

for row in studentrecord:
    print(row)

print("-------------------------------------------------")
print("name of students whose marks in english is greater than 50 : ")
for rowindex in range(1,len(studentrecord)):
    if (studentrecord[rowindex][5] > 50):
        print(studentrecord[rowindex][1])
        
print("---------------------------------------------------------------------")

# Extracting relevant data (student id, name, and maths score) from studentrecord
maths_scores = [(record[0], record[1], record[6]) for record in studentrecord[1:]]

# Sorting based on maths scores in descending order
maths_scores_sorted = sorted(maths_scores, key=lambda x: x[2], reverse=True)

# Getting the top 4 scorers
top_4_scorers = maths_scores_sorted[:4]

for student in top_4_scorers:
    print(f"Student ID: {student[0]}, Name: {student[1]}, Maths Score: {student[2]}")
    
print("---------------------------------------------------------------------")  
print("The student who are bottom three scorer in computer:")  
print("---------------------------------------------------------------------")

# Extract the records for sorting
student_records = [record2, record3, record4, record5, record6, record7, record8, record9, record10, record11]

# Sort the records based on the computer score (9th index)
sorted_records = sorted(student_records, key=lambda x: x[8])

# Get the bottom 3 scorers
bottom_3_computer_scorers = sorted_records[:3]

# Display the results
for record in bottom_3_computer_scorers:
    print(f"{record[1]} scored {record[8]} in computer.")

