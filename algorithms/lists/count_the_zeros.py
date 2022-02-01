# https://www.geeksforgeeks.org/find-number-zeroes/

def find_no_of_zeros(arr, n):
    low = 0
    high = n - 1

    if arr[0] == 0:
        return n

    if arr[high] == 1:
        return 0

    while low < high:
        mid = (low + high) // 2

        if arr[mid] == 1:
            if arr[mid + 1] == 0:
                return n - (mid + 1)
            else:
                low = mid + 1
        elif arr[mid] == 0:
            if arr[mid - 1] == 1:
                return n - mid
            else:
                high = mid - 1


if __name__ == '__main__':
    print(find_no_of_zeros([1, 1, 1, 1, 1, 0], 6))
    print(find_no_of_zeros([1, 0, 0, 0, 0], 5))
    print(find_no_of_zeros([0, 0, 0], 3))
    print(find_no_of_zeros([1, 1, 1, 1], 4))
