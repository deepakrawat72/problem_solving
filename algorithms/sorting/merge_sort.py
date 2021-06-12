def merge_sorted_arrays(arr, l, r, mid_idx):
    l_arr = arr[l: mid_idx + 1]
    r_arr = arr[mid_idx + 1: r + 1]

    i = j = 0
    x = l

    while i < len(l_arr) and j < len(r_arr):
        if l_arr[i] <= r_arr[j]:  # check if all arr2 elements are parsed or arr1[i] < arr2[j]
            arr[x] = l_arr[i]
            i += 1
        else:
            arr[x] = r_arr[j]
            j += 1
        x += 1

    while j < len(r_arr):
        arr[x] = r_arr[j]
        j += 1
        x += 1

    while i < len(l_arr):
        arr[x] = l_arr[i]
        i += 1
        x += 1

    print("After merging = " + str(arr))


def sort(arr, l, r):
    if l < r:
        mid_idx = (l + r) // 2
        sort(arr, l, mid_idx)
        sort(arr, mid_idx + 1, r)
        merge_sorted_arrays(arr, l, r, mid_idx)


if __name__ == '__main__':
    arr = [4, 3, 1, 2, 9, 8]
    sort(arr, 0, len(arr) - 1)
    print(arr)
