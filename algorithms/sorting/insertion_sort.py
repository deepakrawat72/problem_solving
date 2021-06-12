def sort(arr):
    print("Unsorted array - " + str(arr))
    for i in range(1, len(arr)):
        current_item = arr[i]
        j = i
        print("Checking if " + str(current_item) + " is smaller than any element in left sorted array : "
              + str(arr[0:i]))

        while j > 0 and current_item < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = current_item

        print("After - " + str(i) + " iteration " + str(arr))


if __name__ == '__main__':
    arr = [5, 3, 2, 1, 4]
    sort(arr)
