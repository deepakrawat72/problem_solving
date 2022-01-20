def find_last_occurrence(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if item < arr[mid]:
            high = mid - 1
        elif item > arr[mid]:
            low = mid + 1
        else:
            if mid == high or arr[mid] != arr[mid + 1]:
                return mid
            else:
                low = mid + 1

    return -1


if __name__ == '__main__':
    print(find_last_occurrence([5, 10, 10, 10, 12, 15], 10))