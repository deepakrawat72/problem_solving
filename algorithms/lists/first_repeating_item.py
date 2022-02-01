from collections import Counter


def find_first_repeating_item(arr):
    item_occurences_freq = Counter(arr)
    for i in range(0, len(arr)):
        if item_occurences_freq[arr[i]] > 1:
            return i + 1

    return -1


if __name__ == '__main__':
    print(find_first_repeating_item([1, 2, 3, 4, 5]))
