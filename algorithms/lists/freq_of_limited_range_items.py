def find_freq(arr, N, P):
    x = [0] * P

    for item in arr:
        x[item - 1] += 1

    for i in range(0, N):
        if i >= P:
            arr[i] = 0
        else:
            arr[i] = x[i]


if __name__ == '__main__':
    arr = [3, 2, 2, 2, 1]
    find_freq(arr, 5, 3)
    print(arr)
