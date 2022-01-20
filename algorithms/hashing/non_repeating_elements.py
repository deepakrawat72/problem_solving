from collections import Counter


def non_repeating_items(arr):
    frequency_counter = Counter(arr)
    non_repeating_items_arr = []

    for item in arr:
        if frequency_counter[item] == 1:
            non_repeating_items_arr.append(item)

    return non_repeating_items_arr


if __name__ == '__main__':
    print(non_repeating_items([1, 2, 3, 4, 5, 5, 1, 2, 7]))
