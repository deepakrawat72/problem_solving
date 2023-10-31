def get_data(arr):
    peak = arr[0]
    index = 0
    output = []

    for x in range(1, len(arr)):
        if arr[x] * arr[x - 1] > 0:
            if peak < 0 and arr[x] < peak:
                peak = arr[x]
                index = x

            if peak >= 0 and arr[x] > peak:
                peak = arr[x]
                index = x
        else:
            output.append((index, peak))
            peak = arr[x]
            index = x

    output.append((index, peak))

    return output


if __name__ == '__main__':
    arr = [1, 4, 2, -2, -9, 10, 2, 12, 2, -4, -4, -4, -4, 2, 7, 6, -6, -2]
    x = get_data(arr)
    print(x)
