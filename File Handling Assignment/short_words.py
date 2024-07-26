def display_words(file_path):
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for short_word in words:
                if len(short_word) < 4:
                    print(short_word)

display_words('ABC.txt')
