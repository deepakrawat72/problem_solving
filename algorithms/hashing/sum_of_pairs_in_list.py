def sum_exists(arr, N):
    s = set(arr)
    for i in range(0, N):
        diff = sum - arr[i]

        if diff in s and diff != arr[i]:
            return 1

    return 0


def sum_exists_2(arr, sum):
    s = set()

    for item in arr:
        diff = sum - item
        if item in s:
            return 1
        else:
            s.add(diff)

    return 0


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    N = 5
    sum = 5

    print(sum_exists(arr, 5))
    print(sum_exists_2([74, 65, 42, 12, 54, 69, 48, 45, 63, 58, 38, 60, 24, 30, 17], 14))
