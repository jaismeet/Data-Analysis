user_input=input("Please enter an integer : ")
try:
    value = int(user_input)
    print("you entered the integer : ",value)
except ValueError :
    raise ValueError("Invalid input : Please enter a valid integer.")  
