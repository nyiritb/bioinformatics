def word_occurences(text):
    """Return a dictionary of word occurences in a text."""
    words = text.split()
    word_dict = {}
    for word in words:
        word_dict[word] = text.count(word)
    return word_dict

if __name__ == '__main__':
    sample_in = 'We tried list and we tried dicts also we tried Zen'
    sample_out = {
        'and': 1,
        'We': 1,
        'tried': 3,
        'dicts': 1,
        'list': 1,
        'we': 2,
        'also': 1,
        'Zen': 1
    }
    assert(word_occurences(sample_in) == sample_out)