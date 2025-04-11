from stats import count_words, count_chars, dict_sorter
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    word_count = count_words(book)
    char_count = count_chars(book)
    sorted = dict_sorter(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for key in sorted:
        print(f"{key}: {sorted[key]}")
    print("============= END ===============")
if __name__ == "__main__":
    main()