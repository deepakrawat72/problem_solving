def sort_by_abs_diff(arr, num):
    x = {}
    n = len(arr)

    for i in range(0, n):
        diff = abs(num - arr[i])
        x[arr[i]] = diff

    x = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

    i = 0
    for item in x.keys():
        arr[i] = item
        i += 1

    print(arr)


if __name__ == '__main__':
    sort_by_abs_diff([10, 5, 3, 9, 2], 7)
