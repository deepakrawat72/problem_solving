if __name__ == '__main__':
    arr1 = []

    consecutive_counts = 0
    max_counts = 0
    prev_number = -1
    for item in arr1:
        if item == prev_number:
            if consecutive_counts > max_counts:
                max_counts = consecutive_counts
        else:
            consecutive_counts = 1

        prev_number = item
        consecutive_counts += 1

    print(max_counts)