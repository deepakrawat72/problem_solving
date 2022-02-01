# https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/
def find_minimum_item(arr):
    high = len(arr) - 1
    low = 0
    ans = -1

    if high == 0:  # list with 1 element
        return arr[0]

    if arr[low] <= arr[high]:  # if 1st element is smaller than last element in array then return first item
        return arr[low]

    while low < high:
        mid = (low + high) // 2

        if arr[mid] <= arr[high]:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
