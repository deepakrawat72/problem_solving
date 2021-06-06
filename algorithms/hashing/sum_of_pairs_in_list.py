def sum_exists(arr, N):
    s = set(arr)
    for i in range(0, N):
        diff = sum - arr[i]

        if diff in s and diff != arr[i]:
            return 1

    return 0


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    N = 5
    sum = 5

    print(sum_exists(arr, 5))