def remove_duplicates(arr):
    x = i = 0
    last_index = len(arr) - 1
    while i < len(arr):
        if arr[x] != arr[i]:
            x += 1
            arr[x] = arr[i]
        i += 1
    #x += 1
    print(x)
    while last_index > x :
        arr.pop(last_index)
        last_index -= 1


if __name__ == '__main__':
    arr = [0, 0, 0, 0, 3]
    remove_duplicates(arr)
    print(arr)
