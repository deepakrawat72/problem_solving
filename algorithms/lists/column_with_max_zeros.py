def column_with_max_zeros(arr, N):
    # code here
    index_with_max_count = -1
    max_count = 0

    for i in range(0, N):
        col_count = 0
        for j in range(0, N):
            if arr[j][i] == 0:
                col_count += 1
        if col_count > max_count:
            max_count = col_count
            index_with_max_count = i

    return index_with_max_count


if __name__ == '__main__':
    print(column_with_max_zeros([[1, 0, 0],
                                 [1, 0, 1],
                                 [1, 0, 1]], 3))
