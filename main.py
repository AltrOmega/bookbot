FRANK = "books/frankenstein.txt"

def get_book_text(filepath: str):
    with open(filepath, "r", encoding='utf-8') as f:
        return f.read()
    
def main():
    print(get_book_text(filepath=FRANK))
    
if __name__ == "__main__":
    main()