# A panagram contains all the letters of english alphabet at least once.
def is_panagram(s):
    if len(s) < 26:
        return False

    my_dict = {}

    for i in s.lower():
        my_dict[i] = my_dict.get(i, 0) + 1

    if len(my_dict) < 26:
        return False

    for k, v in my_dict.items():
        if v == 0:
            return False

    return True


def is_panagram2(s):
    if len(s) < 26:
        return False

    alphabets = "abcdefghijkmnlopqrstuvwxyz"

    for a in alphabets:
        count = 0
        for x in s:
            if a == x.lower():
                count += 1

        if count == 0:
            return False

    return True


def is_panagram3(s):
    if len(set(s.lower())) < 26:
        return False
    else:
        return True


if __name__ == '__main__':
    print(is_panagram("Thequickbrownfoxjumpsoverthelazydog"))
    print(is_panagram("AbcdefGhijkllmmnnooppqqrrssttuvwxy"))
    print(is_panagram2("Thequickbrownfoxjumpsoverthelazydog"))
    print(is_panagram2("AbcdefGhijkllmmnnooppqqrrssttuvwxy"))
    print(is_panagram3("Thequickbrownfoxjumpsoverthelazydog"))
    print(is_panagram3("AbcdefGhijkllmmnnooppqqrrssttuvwxy"))
