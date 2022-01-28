def max_sum_path(arr1, arr2, m, n):
    arr1_sum = 0
    arr2_sum = 0
    max_sum = 0
    curr_arr1, curr_arr2 = 0, 0

    while curr_arr1 < m and curr_arr2 < n:
        if arr1[curr_arr1] < arr2[curr_arr2]:
            arr1_sum += arr1[curr_arr1]
            curr_arr1 += 1
        elif arr1[curr_arr1] > arr2[curr_arr2]:
            arr2_sum += arr2[curr_arr2]
            curr_arr2 += 1
        else:
            arr1_sum += arr1[curr_arr1]
            arr2_sum += arr2[curr_arr2]
            curr_arr1 += 1
            curr_arr2 += 1

            if arr1_sum > arr2_sum:
                max_sum += arr1_sum
            else:
                max_sum += arr2_sum

            arr1_sum = 0
            arr2_sum = 0

    while curr_arr1 < m:
        arr1_sum += arr1[curr_arr1]
        curr_arr1 += 1

    while curr_arr2 < n:
        arr2_sum += arr2[curr_arr2]
        curr_arr2 += 1

    if arr1_sum > arr2_sum:
        max_sum += arr1_sum
    else:
        max_sum += arr2_sum

    return max_sum


if __name__ == '__main__':
    print(max_sum_path([2, 3, 7, 10, 12], [1, 5, 7, 8], 5, 4))
    print(max_sum_path([1, 2, 3], [3, 4, 5], 3, 3))
