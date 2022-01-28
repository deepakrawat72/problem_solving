# An element is called a peak element if its value is not smaller than the value
# of its adjacent elements(if they exists).
# Given an array arr[] of size N, find the index of any one of its peak elements.
def find_peak_element(arr, n):
    if n == 1:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1
    peak_element_index = -1
    for i in range(1, len(arr)):
        if i != n - 1:
            curr = arr[i]
            prev = arr[i - 1]
            next = arr[i + 1]

            if prev < curr < next:
                peak_element_index = i

        if i == n - 1 and arr[i - 1] < arr[i]:
            return i

    return peak_element_index


if __name__ == '__main__':
    print(find_peak_element([6, 1, 15, 19, 9, 13, 12, 6, 7, 2, 10, 4, 1, 14, 11, 14, 14, 13], 18))
