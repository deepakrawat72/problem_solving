# Given two sorted arrays of distinct elements. There is only 1 difference between the arrays.
# First array has one element extra added in between. Find the index of the extra element.

# complexity : O(n)
def find_extra_item_option1(arr1, arr2):
    max_length = max(len(arr1), len(arr2))

    i = 0
    while i < max_length:
        if i == len(arr2) or arr1[i] != arr2[i]:
            return i

        i += 1

    return -1


# complexity : log n
def find_extra_item_option2(arr1, arr2):
    low = 0
    high = len(arr1)

    result = -1
    while low < high:
        mid = (low + high) // 2

        if low == len(arr2):
            return low

        if arr1[mid] == arr2[mid]:
            low = mid + 1
        else:
            result = mid
            high = mid - 1

    return result


if __name__ == '__main__':
    print(find_extra_item_option1([1, 2, 3, 4], [1, 2, 3]))
    print(find_extra_item_option2([1, 2, 3, 4], [1, 2, 3]))
    print(find_extra_item_option2([8, 1, 2, 3], [1, 2, 3]))
