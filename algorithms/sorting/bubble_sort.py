def sort(arr):
    for i in range(0, len(arr) - 1):
        is_swapped = False
        print("Pass - " + str(i + 1))
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swapped = True

        if not is_swapped:
            return

        print("Elements after - " + str(i + 1) + " pass : " + str(arr))


if __name__ == '__main__':
    arr = [5, 3, 2, 1, 4]
    sort(arr)
    # arr = [1, 2, 3, 4, 5]
    # sort(arr)
