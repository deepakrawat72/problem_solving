# Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.
# Example 1:
# Input:
# N = 7, K = 4
# A[] = {1,2,1,3,4,2,3}
# Output: 3 4 4 3
# Explanation: Window 1 of size k = 4 is
# 1 2 1 3. Number of distinct elements in
# this window are 3.
# Window 2 of size k = 4 is 2 1 3 4. Number
# of distinct elements in this window are 4.
# Window 3 of size k = 4 is 1 3 4 2. Number
# of distinct elements in this window are 4.
# Window 4 of size k = 4 is 3 4 2 3. Number
# of distinct elements in this window are 3.

def count_distinct_by_window(arr, window_size):
    distinct_counts_by_window = []
    i = 0

    x = set()
    while (i + window_size) <= len(arr):
        for j in range(i, i + window_size):
            if arr[j] not in x:
                x.add(arr[j])

        distinct_counts_by_window.append(len(x))
        i += 1
    return distinct_counts_by_window


if __name__ == '__main__':
    print(count_distinct_by_window([1, 2, 1, 3, 4, 2, 3], 4))
