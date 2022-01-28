def create_wave_array(arr):
    for i in range(0, len(arr), 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


if __name__ == '__main__':
    print(create_wave_array([2, 4, 7, 8, 9, 10]))
