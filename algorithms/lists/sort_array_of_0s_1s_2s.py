def sort_array(arr):
    zero_count = 0
    one_count = 0
    two_count = 0

    for item in arr:
        if item == 0:
            zero_count += 1
        elif item == 1:
            one_count += 1
        else:
            two_count += 1

    i = 0

    while i < len(arr):
        if zero_count == 0:
            if one_count == 0:
                arr[i] = 2
                two_count -= 1
            else:
                arr[i] = 1
                one_count -= 1
        else:
            arr[i] = 0
            zero_count -= 1

        i += 1

    return arr


if __name__ == '__main__':
    print(sort_array([0, 2, 1, 2, 0]))
