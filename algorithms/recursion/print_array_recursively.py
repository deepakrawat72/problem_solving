def print_array_recursively(arr, n):
    if n == 0:
        return

    print_array_recursively(arr, n - 1)
    print(arr[n-1], end=' ')


if __name__ == '__main__':
    print_array_recursively([10, 20, 30, 40, 1, 2, 3], 7)
