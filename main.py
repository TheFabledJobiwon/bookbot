def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = char_counter(text)
    chars_list = convert_to_list(chars_dict)
    letters_list = (letters_only(chars_list))
    letters_list.sort(reverse=True, key=sort_on)
    report(letters_list, num_words, book_path)
    
def char_counter(words):
    lowered_words = words.lower()
    d=dict.fromkeys(lowered_words,0)
    for val in lowered_words:
        d[val] += 1
    return d

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def convert_to_list(dictionary):
    return [{"char": key, "num": value} for key, value in dictionary.items()]

def letters_only(characters):
    letters = []
    for character in characters:
        if character["char"].isalpha():
            letters.append(character)
    return letters

def report(letters_list, num_words, path):
    print(f"--- Begin report of {path}")
    print(f"{num_words} words found in the document")
    print()
    for letters in letters_list:
        print(f"The '{letters['char']}' character was found {letters['num']} times")

main()