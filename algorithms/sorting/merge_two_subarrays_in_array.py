def merge_sorted_arrays(arr, l, r, mid_idx):
    l_arr = arr[l: mid_idx + 1]
    r_arr = arr[mid_idx + 1: r]

    i = j = x = 0

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


if __name__ == '__main__':
    arr1 = [3, 5, 7, 1, 2, 13]
    merge_sorted_arrays(arr1, 0, 6, 2)
    print(arr1)
