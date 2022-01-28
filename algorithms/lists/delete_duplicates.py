def delete_duplicates(arr):
    last_non_duplicate_idx = 0
    i = 1
    while i < len(arr):
        if arr[i] != arr[last_non_duplicate_idx]:
            arr[last_non_duplicate_idx + 1] = arr[i]
            last_non_duplicate_idx += 1

        i += 1

    for i in range(last_non_duplicate_idx + 1, len(arr)):
        arr.pop()

    return arr


if __name__ == '__main__':
    print(delete_duplicates([2]))
