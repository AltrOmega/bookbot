from typing import Dict, List

def get_book_text(filepath: str) -> str:
    try:
        with open(filepath, "r", encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file '{filepath}' was not found.")

    
def get_num_words(text: str) -> int:
    return len(text.split())

def get_char_count(text: str) -> Dict[str, int]:
    text = text.lower()
    count: Dict[str, int] = {}
    for char in text:
        key = count.get(char)
        if key is not None:
            count[char] += 1
            continue
        count[char] = 1
    return count

def dict_sort(dict_: Dict[str, int]) -> List[Dict[str, int]]:
    list_ = [{key: value} for key, value in dict_.items()]
    return sorted(list_, key=lambda d: list(d.values())[0])
        
    
    