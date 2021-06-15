def remove_duplicates(arr):
    x = i = 0
    while i < len(arr):
        if arr[x] != arr[i]:
            x += 1
            arr[x] = arr[i]
        i += 1
    x += 1
    while x < len(arr):
        arr[x] = '_'
        x += 1


if __name__ == '__main__':
    arr = [1, 1, 1, 3, 3, 4, 5]
    remove_duplicates(arr)
    print(arr)
