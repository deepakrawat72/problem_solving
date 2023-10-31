# Find the Kth pair in ordered list of all possible sorted pairs of the Array
# Input: arr[] = {2, 1}, K = 4
# Output: {2, 2}
# Explanation:
# The sorted sequence for the given array is {1, 1}, {1, 2}, {2, 1}, {2, 2}. So the 4th pair is {2, 2}.
# Input: arr[] = {3, 1, 5}, K = 2
# Output: {1, 3}

# Asked in PAYPAL interview

def merge_sorted_arrays(arr1, arr2):
    i = j = 0
    merged_arr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            merged_arr.append(arr1[i])
            merged_arr.append(arr2[j])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged_arr.append(arr1[i])

    while j < len(arr2):
        merged_arr.append(arr2[j])

    return merged_arr


def find_kth_pair(nums, k):
    nums.sort()
    map_items = {}
    sorted_pairs = []

    for i in nums:
        if i in map_items:
            merged_arr = merge_sorted_arrays(map_items.get(i), nums)
            map_items[i] = merged_arr
        else:
            map_items[i] = nums

    for i, second_items_list in map_items.items():
        for x in second_items_list:
            sorted_pairs.append((i, x))

    return sorted_pairs[k + 1]


if __name__ == '__main__':
    arr = [2, 1, 2]
    print(find_kth_pair(arr, 4))
