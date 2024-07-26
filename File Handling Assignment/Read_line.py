with open("ABC.txt",'w') as file:
    file.write("    hello world  ")

def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())
read_file_line_by_line('ABC.txt')
