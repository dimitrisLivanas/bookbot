def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    num_chars_list = convert_dict_to_list(num_chars)
    print_report(book_path, num_words, num_chars_list)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in chars_count:
                chars_count[char] += 1
            else:
                chars_count[char] = 1
    return chars_count

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def convert_dict_to_list(dict):
    list = [{'key': k, 'value': v} for k, v in dict.items()]
    def sort_on(item):
        return item['value']
    sorted_list = sorted(list, reverse=True, key=sort_on)
    return sorted_list

def print_report(path, words, list):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document\n")
    for entry in list:
        print(f"The '{entry['key']}' character was found {entry['value']} times")
    print("--- End report ---")


main()