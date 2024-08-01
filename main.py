def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"{num_words} words found in the document")
    print(f"Here's how many times each character appears: {num_chars}")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    return chars_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()