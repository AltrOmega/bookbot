from stats import get_book_text, get_num_words, get_char_count, dict_sort
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    try:
        path = sys.argv[1]
        text = get_book_text(path) 
    except Exception as e:
        print(e)
        sys.exit(1)


    count_gen = get_num_words(text)
    count_spec = dict_sort(get_char_count(text))
    count_spec.reverse()


    print(f'''============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {count_gen} total words
--------- Character Count -------''')
    for dict_ in count_spec:
        key, value = list(dict_.items())[0]
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")
    


if __name__ == "__main__":
    main()