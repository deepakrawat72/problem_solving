def longest_subarray(arr, n):
    max_step = 0
    counter = 0
    for i in range(0, n - 1):
        if arr[i + 1] > arr[i]:
            counter += 1
        else:
            if counter > max_step:
                max_step = counter

            counter = 0

    return max_step


if __name__ == '__main__':
    print(longest_subarray([5, 6, 3, 5, 7, 8, 9, 1, 2], 9))
