def find_max(arr, n):
    max_length = -1

    for i in range(0, n):
        for j in range(i + 1, n):
            diff = j - i
            if arr[j] > arr[i] and diff > max_length:
                max_length = diff

    return max_length


def find_max_efficient(arr, n):
    max_length = -1

    for i in range(0, n):
        for j in range(i + 1, n):
            diff = j - i
            if arr[j] > arr[i] and diff > max_length:
                max_length = diff

    return max_length


if __name__ == '__main__':
    print(find_max([34, 8, 10, 3, 2, 80, 30, 33, 1], 9))
    print(find_max([9, 2, 3, 4, 5, 6, 7, 8, 18, 0], 10))
    print(find_max([1, 2, 3, 4, 5, 6], 6))
    print(find_max([6, 5, 4, 3, 2, 1], 6))
