def max_water_trapped(arr, n):
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = arr[0]
    right_max[n - 1] = arr[n - 1]

    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])

    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])

    water_trapped = 0

    for i in range(0, n):
        water_trapped += min(left_max[i], right_max[i]) - arr[i]

    return water_trapped


def max_water_trapped_with_space_optimization(arr, n):
    low = 0
    high = n - 1
    left_max = -1
    right_max = -1
    water_trapped = 0
    while low <= high:
        if arr[low] < arr[high]:
            if left_max > arr[low]:
                water_trapped += left_max - arr[low]
            else:
                left_max = arr[low]

            low += 1
        else:
            if right_max > arr[high]:
                water_trapped += right_max - arr[high]
            else:
                right_max = arr[high]
            high -= 1

    return water_trapped


if __name__ == '__main__':
    print(max_water_trapped([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 12))
    print(max_water_trapped_with_space_optimization([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 12))
