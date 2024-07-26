def count_words_in_file(file_path):
    
    with open(file_path, 'r') as file:
        total_words = 0
        for line in file:
            words = line.split()
            total_words += len(words)
        print("Total number of words in ",file_path," : " , total_words)
    

count_words_in_file('ABC.txt')
