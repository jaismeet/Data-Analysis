def count_uppercase_characters(file_path):
    
    with open(file_path, 'r') as file:
        uppercase_count = 0
        for line in file:
            for char in line:
                if char.isupper():
                    uppercase_count += 1
        print("Total number of uppercase characters in ",file_path , " : ", uppercase_count)
    
count_uppercase_characters('ABC.txt')
