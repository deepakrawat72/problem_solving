def three_way_partitioned_arr(arr, n, a, b):
    start = 0
    end = n - 1

    i = 0
    while i <= end:
        if arr[i] < a:
            arr[i], arr[start] = arr[start], arr[i]

            start += 1
            i += 1
        elif arr[i] > b:
            arr[i], arr[end] = arr[end], arr[i]

            end -= 1
        else:
            i += 1


if __name__ == '__main__':
    arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
    n = len(arr)
    three_way_partitioned_arr(arr, n, 10, 20)

    print(arr)
