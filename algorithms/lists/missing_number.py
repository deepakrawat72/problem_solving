def missing_number(arr, n):
    expected_sum = (n*(n+1))//2
    actual_sum = 0

    for i in range(0, len(arr)):
        actual_sum += arr[i]

    return expected_sum - actual_sum
if __name__ == '__main__':
    print(missing_number([1, 2, 3, 5, 6, 7], 7))
    #print(missing_number([1], 2))
