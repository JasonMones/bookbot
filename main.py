from stats import *
import sys

def get_book_text(FILE_PATH):
    with open(FILE_PATH) as path:
        return path.read()
    
def print_char_count(char_count):
    for dict in char_count:
        print(f"{dict["character"]}: {dict["count"]}")
    
def get_book_path():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def main():
    path = get_book_path()
    text = get_book_text(path)
    word_count = word_count_f(text)
    char_count = char_count_f(text)
    sorted_char_count_v = sorted_char_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_char_count(sorted_char_count_v)
    print("============= END ===============")

main()