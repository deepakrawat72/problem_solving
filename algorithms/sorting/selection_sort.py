def sort(arr):
    for i in range(0, len(arr)):
        min_item_idx = i
        print("minimum_item to be looked in : " + str(arr[i+1:]))
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_item_idx]:
                min_item_idx = j

        arr[i], arr[min_item_idx] = arr[min_item_idx], arr[i]

        print("After - " + str(i) + " iteration " + str(arr))


if __name__ == '__main__':
    arr = [5, 3, 2, 1, 4]
    sort(arr)
