import sys
from stats import count_words
from stats import count_chars


def sort_num(item):
    return item["num"]


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()

        print("============ BOOKBOT ============")
        print('Analyzing book found at books/frankenstein.txt')

        print('----------- Word Count ----------')
        print(f"{count_words(file_contents)} words found in the document")

        print('--------- Character Count -------')
        chars = count_chars(file_contents)
        chars.sort(reverse=True, key=sort_num)
        for char in chars:
            print(f"{char['char']}: {char['num']}")

        print("============= END ===============")


if __name__ == "__main__":
    main()
