def palindrome_checker(string):
    characters_set = set()

    for c in string:
        if c in characters_set:
            characters_set.remove(c)
        else:
            characters_set.add(c)

    if len(characters_set) > 1:
        return 'Given string is not a palindrome'
    else:
        return 'Given string is a palindrome'


def palindrome_checker_recursive(str, low, high):
    if low > high:
        return True

    is_matched = str[low] == str[high]

    return is_matched and palindrome_checker_recursive(str, low + 1, high - 1)


if __name__ == '__main__':
    result = palindrome_checker('nitiotin')
    print(result)
    result = palindrome_checker('geeggg')
    print(result)
    result = palindrome_checker('abccbabb')
    print(result)
    result = palindrome_checker_recursive("abccccba", 0, 7)
    print(result)