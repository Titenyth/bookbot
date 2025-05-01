from collections import Counter

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

file_contents = get_book_text("./books/frankenstein.txt")


def num_words(file):
    words = file.split()
    num_words = len(words)
    return num_words

num_words = num_words(file_contents)

def num_characters(file):
    lowercase = file.lower()
    char_count = Counter(lowercase)
    return char_count

num_chars = num_characters(file_contents)


def dict_to_sorted_list(dict):
    new_dict = []
    for char, count in dict.items():
        char_count_dict = {"char": char, "num": count}
        new_dict.append(char_count_dict)

    def sort_on(dict):
        return dict["num"]

    new_dict.sort(reverse=True, key=sort_on)

    return new_dict
