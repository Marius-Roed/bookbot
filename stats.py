def count_words(sentence):
    countWords = 0
    words = sentence.split()

    for word in words:
        countWords += 1

    return countWords


def count_chars(book):
    chars = []
    char_index = {}

    for char in book:
        char = char.lower()
        if char in char_index:
            chars[char_index[char]]["num"] += 1
        elif char.isalpha():
            chars.append({"char": char, "num": 1})
            char_index[char] = len(chars) - 1

    return chars
