from collections import Counter


def find_duplicates_in_array(arr):
    counter = Counter(arr)
    de_dup_array = []

    found_duplicate = False
    for item in arr:
        if counter[item] > 1:
            de_dup_array.append(item)
            counter[item] = 0
            found_duplicate = True

    if found_duplicate:
        return sorted(de_dup_array)
    else:
        return [-1]


if __name__ == '__main__':
    print(find_duplicates_in_array([2, 3, 1, 2, 3]))
