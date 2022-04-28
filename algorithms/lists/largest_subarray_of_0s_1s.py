def max_length(arr):
    sum = 0
    max_size = -1
    for i in range(0, len(arr)):
        sum = -1 if arr[i] == 0 else 1

        for j in range(i + 1, len(arr)):
            sum += -1 if arr[j] == 0 else 1

            if sum == 0 and max_size < j - i + 1:
                max_size = j - i + 1
                start_index = i

    print("start_index = " + str(start_index) + " to end_index = " + str(start_index + max_size - 1))


if __name__ == '__main__':
    max_length([1, 0, 0, 1, 0, 1, 1])
