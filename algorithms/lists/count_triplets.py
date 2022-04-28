from collections import Counter


def count_triplets(arr):
    arr_len = len(arr)
    triplet_count = 0

    for i in range(0, arr_len):
        for j in range(i + 1, arr_len):
            for k in range(j + 1, arr_len):
                if arr[i] + arr[j] == arr[k] or arr[i] + arr[k] == arr[j] or arr[j] + arr[k] == arr[i]:
                    triplet_count += 1

    return triplet_count


def count_triplets_using_set(arr):
    arr_len = len(arr)
    triplet_count = 0

    item_counts = Counter(arr)

    for i in range(0, arr_len):
        for j in range(i + 1, arr_len):
            sum_of_nos = arr[i] + arr[j]
            if sum_of_nos in item_counts:
                triplet_count += item_counts[sum_of_nos]

    return triplet_count


def count_triplets_using_two_pointers(arr):
    arr_len = len(arr)
    triplet_count = 0

    arr.sort()

    for i in range(arr_len - 1, 1, -1):
        start = 0
        end = i - 1
        inner_count = 0

        while start < end:
            sum_of_nos = arr[start] + arr[end]
            if arr[i] == sum_of_nos:
                inner_count += 1
                start += 1
                end -= 1
            elif arr[i] > sum_of_nos:
                start += 1
            else:
                end -= 1

        triplet_count += inner_count

    return triplet_count


if __name__ == '__main__':
    print(count_triplets([1, 2, 3, 4, 5]))
    # print(count_triplets([1, 1, 1, 2, 2]))
    print(count_triplets_using_set([1, 2, 3, 4, 5]))
    # print(count_triplets_using_set([1, 1, 1, 2, 2]))
    print(count_triplets_using_two_pointers([1, 2, 3, 4, 5]))
    # print(count_triplets_using_two_pointers([1, 1, 1, 2, 2]))
