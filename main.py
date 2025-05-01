import sys
from stats import num_words
from stats import num_characters
from stats import get_book_text
from stats import dict_to_sorted_list

book_path = []
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]


file_contents = get_book_text(book_path)
num_chars = num_characters(file_contents)
new_dict = dict_to_sorted_list(num_chars)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in new_dict:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()