num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    # Convert inputs to float
    num1 = float(num1)
    num2 = float(num2)

    print("The sum of numbers are : ",num1+num2)

except ValueError:
    raise TypeError("Both inputs must be numerical values.")
