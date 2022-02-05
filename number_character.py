def f(word, character):
    """Complete a function that returns the number of times a given
    character occurs in the given string"""
    count = 0
    for x in word:
        if x == character:
            count = count + 1
        else:
            pass

    print(count)
    return count


f("mississippi", "s")
