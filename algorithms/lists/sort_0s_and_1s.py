def sort_0s_and_1s(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
        if arr[high] == 1:
            high -= 1

        if arr[low] == 0:
            low += 1

    return arr


if __name__ == '__main__':
    print(sort_0s_and_1s([1, 1, 0, 0, 0, 0, 0, 0, 0, 1]))
