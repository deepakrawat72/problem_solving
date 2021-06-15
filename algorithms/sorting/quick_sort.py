def partition(arr, l, h):
    i = l
    j = h

    pivot = arr[l]

    while i < j:
        while arr[i] <= pivot and i < h:
            i += 1
        while arr[j] > pivot and j > 0:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[l] = arr[l], arr[j]

    return j


def quick_sort(arr, l, r):
    if l < r:
        print("Before sorting  = " + str(arr))
        pivot = partition(arr, l, r)
        print("pivot = " + str(pivot))
        quick_sort(arr, l, pivot - 1)
        print("after sorting  partition 0 = " + str(arr))
        quick_sort(arr, pivot + 1, r)
        print("after sorting  partition 1 = " + str(arr))


if __name__ == '__main__':
    arr = [2, 6, 9, 3, 1, 4, 7]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
