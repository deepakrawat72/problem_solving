def merge_sorted_arrays(arr1, arr2):
    arr3 = []
    m, n = len(arr1), len(arr2)

    i, j, x = 0, 0, 0

    while x < m + n:
        if j == n or arr1[i] < arr2[j]:  # check if all arr2 elements are parsed or arr1[i] < arr2[j]
            arr3.append(arr1[i])
            i, x = i + 1, x + 1
        elif i == m or arr1[i] > arr2[j]:  # check if all arr1 elements are parsed or arr1[i] > arr2[j]
            arr3.append(arr2[j])
            j, x = j + 1, x + 1
        else:
            arr3.append(arr1[i])
            arr3.append(arr2[j])
            i, j = i + 1, j + 1
            x += 2

    return arr3


if __name__ == '__main__':
    arr1 = [3, 5, 7, 9, 11]
    arr2 = [1, 5, 10]

    print(merge_sorted_arrays(arr1, arr2))
