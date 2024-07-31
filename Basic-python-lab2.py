# 1. Python program to check leap year

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


# 2. Python Program to Find the Largest Among Three Numbers


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("The largest number among the three is:", largest)

# 3. Python Program to Check if a Number is Positive, Negative or 0

number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
# 4. A toy vendor supplies three types of toys: Battery Based Toys, Key-based
# Toys, and Electrical Charging Based Toys. The vendor gives a discount of
# 10% on orders for battery-based toys if the order is for more than Rs. 1000.On 
# orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a 
# discount of 10% is given on orders for electrical charging based toys of value 
# more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery 
# based toys, key-based toys, and electrical charging based toys respectively. 
# Write a program that reads the product code and the order amount and prints 
# out the net amount that the customer is required to pay after the discount.

product_code = int(input("Enter the product code (1 for Battery-Based Toys, 2 for Key-Based Toys, 3 for Electrical Charging Based Toys): "))
order_amount = float(input("Enter the order amount: "))
discount_percentage = 0
if product_code == 1:  
    if order_amount > 1000:
        discount_percentage = 10
elif product_code == 2:  
    if order_amount > 100:
        discount_percentage = 5
elif product_code == 3:  
    if order_amount > 500:
        discount_percentage = 10
else:
    print("Invalid product code.")
discount_amount = (discount_percentage / 100) * order_amount
net_amount = order_amount - discount_amount
print(f"The net amount to be paid after discount is: Rs. {net_amount:.2f}")

# 5. A transport company charges the fare according to following table:

distance = float(input("Enter the distance traveled in kilometers: "))
fare = 0
if 1 <= distance <= 50:
    fare = distance * 8  
elif 51 <= distance <= 100:
    fare = distance * 10  
elif distance > 100:
    fare = distance * 12  
else:
    print("Distance must be at least 1 kilometer.")
if distance >= 1:
    print(f"The fare for {distance} kilometers is Rs. {fare}")


# 6. Write a python program to reverse a number using a while loop.

number = int(input("Enter an integer: "))
reversed_number = 0
original_number = number
while number > 0:
    last_digit = number % 10
    reversed_number = reversed_number * 10 + last_digit
    number = number // 10
print("The reversed number of ",original_number, " is" ,reversed_number)

# 7. Write a python program to check whether a number is palindrome or not?

number = int(input("Enter an integer: "))
number_str = str(number)
reversed_str = number_str[::-1]
if number_str == reversed_str:
    print("The number ",number , "is a palindrome.")
else:
    print("The number ",number, "is not a palindrome.")


# 8. Write a python program finding the factorial of a given number using a while loop.

num = int(input("enter the any number:"))
i=1
fact=1
while(i<=num):
    fact*=i
    i+=1
print("the factorial is:" ,fact)

# 9. Accept numbers using input() function until the user enters 0. If user
# input 0 then break the while loop and display the sum of all the numbers.

total_sum = 0
while True:
    number = int(input("Enter a number (0 to quit): "))
    if number == 0:
        break
    total_sum += number
print("The sum of all entered numbers is: " ,total_sum)

# 10. Print the first 10 natural numbers using for loop

for number in range(1, 11):
    print(number)
    
# 11. Python program to check if the given string is a palindrome

input_string = input("Enter a string: ")
cleaned_string = input_string.replace(" ", "").lower()
if cleaned_string == cleaned_string[::-1]:
    print("The string ",input_string, " is a palindrome.")
else:
    print("The string ",input_string," is not a palindrome.")

# 12. Python program to check if a given number is an Armstrong number

number = int(input("Enter an integer: "))
number_str = str(number)
num_digits = len(number_str)
sum_of_powers = 0
for digit in number_str:
    sum_of_powers += int(digit) ** num_digits
if sum_of_powers == number:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")


# 13. Python program to get the Fibonacci series between 0 to 50

a, b = 0, 1
fibonacci_series = []
while a <= 50:
    fibonacci_series.append(a)
    a, b = b, a + b  
print("Fibonacci series between 0 and 50:")
print(fibonacci_series)


# 14. Python program to check the validity of password input by users

def is_valid_password(password):
    min_length = 8
    max_length = 20
    if len(password) < min_length or len(password) > max_length:
        return False, "Password must be between 8 and 20 characters long."
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*(),.?\":{}|<>"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    if has_upper and has_lower and has_digit and has_special:
        return True, "Password is valid."
    else:
        return False, "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
password = input("Enter a password: ")
valid, message = is_valid_password(password)
print(message)
