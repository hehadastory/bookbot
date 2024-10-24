def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = count_letters(text)
    sorted_counts = sort_count(num_chars)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_counts:
        print(f"The '{item[0]}' character was found {item[1]} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = len(text.split())
    return words
    
def count_letters(text):
    letter_counts = {}

    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    
    return letter_counts

def sort_count(letter_counts):
    sorted_counts = list(letter_counts.items())
    sorted_counts.sort(key=lambda item: item[1], reverse=True)
    return sorted_counts

main()