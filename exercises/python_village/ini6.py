def word_occurences(text):
    """Return a dictionary of word occurences in a text."""
    words = text.split()
    word_dict = {}
    for word in words:
        word_dict[word] = words.count(word)
    return word_dict

if __name__ == '__main__':
    print(word_occurences('We tried list and we tried dicts also we tried Zen'))