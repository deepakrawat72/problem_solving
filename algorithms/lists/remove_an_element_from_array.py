# https://leetcode.com/problems/remove-element/
def remove(arr, item):
    i = 0
    h = len(arr) - 1
    while i < len(arr):
        if arr[i] == item:
            if arr[h] != item:
                arr[i] = arr[h]
                i += 1
            arr.pop(h)  # remove last element
            h -= 1
        else:
            i += 1


if __name__ == '__main__':
    arr = [0, 1, 2, 2, 3, 0, 4, 2]
    remove(arr, 2)
    print(arr)
