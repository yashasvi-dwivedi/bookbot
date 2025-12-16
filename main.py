import sys
from stats import count_words, count_characters , sort_char

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = count_characters(text)
    sorted_chars = sort_char(char_counts)

    for item in sorted_chars:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['num']}")
           
    print("============= END ===============")


main()


