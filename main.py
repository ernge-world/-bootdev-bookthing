from stats import word_count
from stats import character_dict
from stats import sorting_hat
import sys

def main(book):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}")
        print("----------- Word Count ----------")
        num_words = word_count(book)
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        letter_count = character_dict(book)
        sorted = sorting_hat(letter_count)
        for entry in sorted:
            ch = entry["char"]
            cnt = entry["num"]
            print(f"{ch}: {cnt}")
        print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])