# 1. Using input() function take one number from the user and using ternary operators
# check whether the number is even or odd

num = int(input("Enter any number : "))
result = "Even" if num % 2 == 0 else "Odd"

print("The number ",num, "is : " ,result)

# 2. Using input function take two number and then swap the number

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
print("Before swapping : ")
print("The first number is : ",num1)
print("The second number is : ",num2)

num1 , num2 = num2 , num1 

print("After swapping : ")
print("The first number is : ",num1)
print("The second number is : ",num2)

# 3. Write a Program to Convert Kilometers to Miles

kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * 0.621371
print(kilometers ,"kilometers is equal to ",miles,"miles")

# 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year

p = 200
r = 5
t = 5
print("Principle amount is : " , p)
print("Rate interest per year is : " , r,"(% per year)")
print("Time in years : " , t)
simple_interest = (p*r*t)/100
print("Simple interest on Rs" ,p, "for" ,t,"years at ",r,"(% per year) is : " ,simple_interest)
