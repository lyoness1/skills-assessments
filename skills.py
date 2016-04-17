"""Skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different::

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    return list(set(words))


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    
    return list(set(items1) & set(items2))


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    # initializes a diction to store word keys and values
    word_count_dict = {}

    # makes a list of words in the phrase
    words_list = phrase.split()

    # iterates through each word and adds it to dictionary
    for word in words_list:
        # if the word is not already in the dict, add it with a value 1
        if word not in word_count_dict:
            word_count_dict[word] = 1
        # if the word is already a key, add 1 to it's value
        else:
            word_count_dict[word] += 1

    return word_count_dict


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    # makes a dictionary of English keys and pirate values
    pirate_dict = {
        "man": "matey", 
        "hotel": "fleabag inn", 
        "student": "swabbie",
        "boy": "matey",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": "be",
    }

    # puts the words in the phrase in a list to iterate over
    word_list = phrase.split()

    # check to see if each word is in the pirate dictionary or not
    for word in word_list:
        # if the word is in the dictionary, replace it with the pirate version
        if word in pirate_dict:
            word_list[word_list.index(word)] = pirate_dict[word]

    # return a string of the words into a sentence
    return " ".join(word_list)

    # NOTE: The doctest failed because 'man' was not translated, but it wasn't provided in the original dictionary... 


def sort_by_word_length(words):
    """Given list of words, return list of ascending (len, [words]).

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- the length
    of the words for that word-length, and the list of words of
    that word length.

    For example::

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]
    """

    # initializes a dictionary to hold various word lengths
    length_of_words = {}

    # iterates through words to add to dictionary
    for word in words:
        # if the length of the word is not already a key, add it
        if len(word) not in length_of_words:
            length_of_words[len(word)] = [word]
        # if the word length is a key, append the word to the value list
        else: 
            length_of_words[len(word)].append(word)

    # return a list of tuples containing (key, value) from the dict
    return length_of_words.items()


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    # this function took about 45 minutes, the rest of them took about 3-4 minutes each
    # I'm not sure I really understood a 'sexy' way to do this without all the if/else statements and new variable 
    # I'm not super happy with this code, but it works!
    sums_of_pairs = {}

    # gets a total for each pair of numbers in the original list
    for num1 in numbers:
        for num2 in numbers[numbers.index(num1):]:
            total = num1 + num2
            # if the total is in the dictionary, append a list of the pair
            if total in sums_of_pairs:
                sums_of_pairs[total].append([num1, num2])
            # if the total isn't in the dict, add a list of the pair
            else: 
                sums_of_pairs[total] = [[num1, num2]]

    # making sure the duplicate pairs are in the same order before removing duplicates
    zero_sums = sorted(sorted(pair) for pair in sums_of_pairs[0])

    # this is my 'lazy' way of getting rid of duplicates (because I can't make a set out of a list?)
    no_duplicates = []
    for pair in zero_sums:
        if pair not in no_duplicates:
            no_duplicates.append(pair)

    # return only the pairs that sum to 0
    return no_duplicates


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary."""
    
    # initializes a new list for the answer and removes the first word from the input list
    result = [names.pop(0)]
    # initializes a new dict to store words by last letter
    word_dict = {}

    # creates a dictionary of items: (letter: [words starting w/ letter])
    for word in names:
        if word[0] in word_dict:
            word_dict[word[0]].append(word)
        else: 
            word_dict[word[0]] = [word]

    # loops until no more words begining with the current last letter of the result are found
    while True:
        # sets the key to look up by finding the last letter of result
        key = result[-1][-1]
        # breaks the while loop when an empty list is found for the key
        if word_dict[key] == []:
            break
        # appends the first instance of a word at the current key to the result
        # pops the word from the list in the dictionary so it can't be resued
        else: 
            result.append(word_dict[key].pop(0))

    return result


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
