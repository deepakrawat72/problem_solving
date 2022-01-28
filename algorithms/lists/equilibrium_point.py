# Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of
# elements after it.

# hint : Use prefix sum

def find_equilibrium_point(arr):
    prev_sum = 0
    total_sum = 0

    for element in arr:
        total_sum += element

    for i in range(0, len(arr)):
        if prev_sum == (total_sum - arr[i]):
            return i + 1
        prev_sum += arr[i]
        total_sum -= arr[i]


if __name__ == '__main__':
    print(find_equilibrium_point([1]))
