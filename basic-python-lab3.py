print("------------------------Assignment 1 -------------------------------")

# 1. Declare a div() function with two parameters. Then call the function and pass two
# numbers and display their division.

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed."
a=10
b=2
result = div(10,2)
print("The division of ",a, "by" ,b, "is : " , result)

# 2. Declare a square() function with one parameter.Then call the function and pass
# one number and display the square of that number 

def square(number):
    return number * number
num = 5
result = square(num)
print("The square of ",num, "is : ",result )

# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers.


import random
random_numbers = [random.randint(1, 100) for _ in range(5)]
max_num = max(random_numbers)
min_num = min(random_numbers)
print("Random numbers: ",random_numbers)
print("The maximum number is ", max_num)
print("The minimum number is ", min_num)

# 4. Accept a name from the user and display that in lower case using lower() function

name = input("Enter your name: ")
lowercase_name = name.lower()
print("Your name in lower case is: " , lowercase_name)


print("------------------------ Assignment 2 -------------------------------")

# 1. Write a Python program to count the occurrences of each word in a given sentence

string ="To change the overall look of your document. To change the look available in the gallery"
words = string.lower().split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
for word, count in word_counts.items():
    print(f"'{word}': {count}")
    
    
# 2. Write a Python program to remove a newline in Python

string = "\nBest \nDeeptech \nPython \nTraining\n"
new_string = string.replace("\n", " ")
print(new_string.strip())

# 3. Write a Python program to reverse words in a string

string = "Deeptech Python Training"
words = string.split()
reversed_words = words[::-1]
reversed_string = ' '.join(reversed_words)
print(reversed_string)


# 4. Write a Python program to count and display the vowels of a given text


string = "Welcome to python Training"
vowels = "aeiou"
vowel_counts = {vowel: 0 for vowel in vowels}
for char in string.lower():
    if char in vowel_counts:
        vowel_counts[char] += 1
for vowel, count in vowel_counts.items():
    if count > 0:
        print(f"'{vowel}': {count}")

print("------------------------ Assignment 3 -------------------------------")

# 1. Write a Python program to Count all letters, digits, and special
# symbols from the given string

string = "P@#yn26at^&i5ve"
countalpha=0
countnum=0
count=0
for i in range(len(string)-1):
    if string[i].isalpha() == True:
        countalpha += 1
    elif string[i].isnumeric() ==  True:
        countnum += 1
    else:
        count += 1
print("Total Alphabets : " ,countalpha)   
print("Total Numeric values : ",countnum)
print("Total special character : ",count)


# 2. Write a Python program to remove duplicate characters of a given string.

input_string = "String and String Function"
words = input_string.split()
unique_words = []
seen_words = set()

for word in words:
    if word not in seen_words:
        unique_words.append(word)
        seen_words.add(word)
result_string = ' '.join(unique_words)

print(result_string)

# 3. Write a Python program to count Uppercase, Lowercase, special character and
# numeric values in a given string

input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

uppercase_count = 0
lowercase_count = 0
numeric_count = 0
special_count = 0

special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

for char in input_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        numeric_count += 1
    elif char in special_characters or not char.isalnum():
        special_count += 1
print("UpperCase : ",uppercase_count)
print("LowerCase : ",lowercase_count)
print("NumberCase : ",numeric_count)
print("SpecialCase : ",special_count)

# 4. Write a Python Count vowels in a string

input_string = "Welcome to Python Assignment"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in input_string:
    if char in vowels:
        vowel_count += 1
print("Total vowels are: ",vowel_count)
