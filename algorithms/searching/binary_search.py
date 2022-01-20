def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if item == arr[mid]:
            return "Item found at position : " + mid
        elif item < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return "Item not found"


def binary_search_recursive(arr, item, low, high):

    if low > high:
        return "Item not found"

    mid = (high + low) // 2

    if arr[mid] == item:
        return "Item found at position : " + mid
    elif item < arr[mid]:
        return binary_search_recursive(arr, item, low, mid - 1)
    else:
        return binary_search_recursive(arr, item, mid + 1, high)


if __name__ == '__main__':
    #print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1))
    print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1, 0, 9))
