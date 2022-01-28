# Given two unsorted arrays arr1[] and arr2[]. They may contain duplicates. For each element in arr1[] count elements
# less than or equal to it in array arr2[].

# Hint :
# 1 - Do a binary search on the second array and find the index of the largest element smaller than or equal to
# the element of the first array.
# 2 - Create an empty array of zeros with size = max(max(arr1), max(arr2)). Now fill this array with count of each
# unique element in arr2 as indexes such that count[i] = count[i-1] + count[i]

def count_occurrences_of_item(arr, n, item):
    h = n - 1
    l = 0
    while l <= h:
        mid = (l + h) // 2

        if item >= arr[mid]:
            l = mid + 1
        else:
            h = mid - 1

    return h


def count_elements_less_than_or_equal_approach_1(arr1, arr2, n1, n2):
    arr2.sort()
    for i in range(0, n1):
        item_count = count_occurrences_of_item(arr2, n2, arr1[i]) + 1
        arr1[i] = item_count


def count_elements_less_than_or_equal_approach_2(arr1, arr2, n1, n2):
    size = max(max(arr1), max(arr2)) + 1
    counter = [0] * size

    for i in range(0, n2):
        counter[arr2[i]] += 1

    for j in range(1, len(counter)):
        counter[j] += counter[j - 1]

    for k in range(0, n1):
        arr1[k] = counter[arr1[k]]


if __name__ == '__main__':
    arr1 = [4098, 7968, 4523, 277, 6956, 4560, 2062, 5705, 5743, 879, 5626, 9961, 491, 2995, 741, 4827, 5436]
    arr2 = [4098, 7968, 4523, 277, 6956, 4560, 2062, 5705, 5743, 879, 5626, 9961, 491, 2995, 741, 4827, 5436, 9989,
            3403, 3902, 153, 292, 1181, 6220, 7515, 8517, 8694, 5447, 10525, 3570, 337, 1869, 8711, 3265, 3897, 5834,
            9894, 6301, 1409, 8920, 7931, 6472, 4664, 3940, 7711, 5851, 6868, 3145, 5242, 10260, 10355]

    n1 = len(arr1)
    n2 = len(arr2)

    count_elements_less_than_or_equal_approach_1(arr1, arr2, n1, n2)
    print("item counts =" + str(arr1))
