from stats import get_book_text, get_num_words, get_char_count, dict_sort

FRANK = "books/frankenstein.txt"
TEXT = get_book_text(filepath=FRANK)

def main():
    count_gen = get_num_words(TEXT)
    count_spec = dict_sort(get_char_count(TEXT))
    count_spec.reverse()
    path = FRANK
    print(f'''============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {count_gen} total words
--------- Character Count -------''')
    for dict_ in count_spec:
        key, value = list(dict_.items())[0]
        print(f"{key}: {value}")

    print("============= END ===============")
    
if __name__ == "__main__":
    main()