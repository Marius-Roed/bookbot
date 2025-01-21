def count_chars(book):
    symbols = [",", ".", "'", '"', "#", "]", "[", "(", ")", "_", "/", "\n", "-", "=", "+", " ", "*",
               "?", "!", "@", "%", ":", ";", "$", "&", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    chars = {}
    for char in book:
        if char.lower() in symbols:
            pass
        elif char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1

    return chars


def count_words(sentence):
    countWords = 0
    words = sentence.split()

    for word in words:
        countWords += 1

    return countWords


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        print("--- Begin book report ---")
        print(count_words(file_contents))

        chars = count_chars(file_contents)
        for char in chars:
            print(f"The '{char}' was found {chars[char]} times")

        print("--- End book report ---")


if __name__ == "__main__":
    main()
