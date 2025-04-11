def count_words(book):
    split_book = book.split()
    return len(split_book)

def count_chars(book):
    lowered_book = book.lower()
    char_count = {}
    for letter in lowered_book:
        if letter in char_count:
            char_count[letter] +=1
        else:
            char_count[letter] = 1
    return char_count

def dict_sorter(char_dict):
    dict_list = []
    
    for key in char_dict:
        alpha_dict = {}
        for key in char_dict:
            if key.isalpha():
                alpha_dict[key] = char_dict[key]
        sorted_list = dict(sorted(alpha_dict.items(), key=lambda key_val: key_val[1], reverse=True))
    return sorted_list
    