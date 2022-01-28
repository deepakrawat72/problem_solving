def sorted_subsequence(arr):
    sorted_count = 1
    last_sorted_item = arr[0]
    sorted_subseq = [last_sorted_item]

    for i in range(1, len(arr)):
        if last_sorted_item > arr[i]:
            sorted_subseq.pop()
            last_sorted_item = -1 if len(sorted_subseq) == 0 else sorted_subseq[len(sorted_subseq) - 1]
            sorted_count -= 1

        if last_sorted_item < arr[i]:
            sorted_count += 1
            last_sorted_item = arr[i]
            sorted_subseq.append(arr[i])

        if sorted_count == 3:
            return sorted_subseq

    return []


if __name__ == '__main__':
    print(sorted_subsequence([1, 2, 1, 1, 3]))
    # print(sorted_subsequence([58, 15, 67, 44, 54, 36, 33, 93, 7, 18, 69, 30, 39, 60, 51]))
