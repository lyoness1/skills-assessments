"""Advanced skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    char_dict = {}

    for char in phrase:
        if char == " ":
            continue
        elif char not in char_dict:
            char_dict[char] = 1
        else: 
            char_dict[char] += 1

    placeholder = 0

    for key in char_dict:
        if char_dict[key] > placeholder:
            top_char = [key]
            placeholder = char_dict[key]
        elif char_dict[key] == placeholder:
            top_char.append(key)
        else: 
            continue

    return sorted(top_char)


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    # initializes an empty dictionary
    words_by_length = {}

    # loops through the words in the given list
    for word in words:
        # if the length of the word is not already a key, add the length and word to the dict
        if len(word) not in words_by_length:
            words_by_length[len(word)] = [word]
        # if the length is already in dict, append word to length key
        # sort the words in the value list alphabetically
        else: 
            words_by_length[len(word)].append(word)
            words_by_length[len(word)].sort()

    # returns a sorted list of the tuples of (keys, [values])
    return sorted(words_by_length.items())


#####################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
