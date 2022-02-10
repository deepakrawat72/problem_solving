def get_pairs_count(arr, n, k):
    count_dict = {}
    no_of_pairs = 0

    for i in range(0, n):
        curr_item = arr[i]
        diff = k - curr_item
        if diff in count_dict:
            no_of_pairs += count_dict[diff]

        if curr_item in count_dict:
            count_dict[curr_item] += 1
        else:
            count_dict[curr_item] = 1

    return no_of_pairs


if __name__ == '__main__':
    print(get_pairs_count([1, 5, 7, 1], 4, 6))
    print(get_pairs_count([1, 1, 1, 1], 4, 2))
