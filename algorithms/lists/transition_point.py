def find_transition_point(arr):
    low = 0
    high = len(arr) - 1

    if arr[low] == 0 and arr[high] == 0:
        return -1
    elif arr[low] == 1 and arr[high] == 1:
        return 0
    else:
        while low < high:
            if arr[low] == arr[low + 1]:
                low += 1
            else:
                return low + 1

            if arr[high] == arr[high - 1]:
                high -= 1
            else:
                return high


if __name__ == '__main__':
    print(find_transition_point([0, 0, 0, 0, 0]))
