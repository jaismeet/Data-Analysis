filename = 'abc.txt'

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError :
    print("file does not exists.")
