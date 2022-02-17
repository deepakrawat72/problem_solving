# O(n^2) -- space - O(1)
def find_max_profit_naive_solution(arr, n):
    max_profit = -1

    for i in range(0, n):
        for j in range(i + 1, n):
            diff = arr[j] - arr[i]

            if diff > max_profit:
                max_profit = diff

    return max_profit


# O(n) -- space O(n)
def find_max_profit_using_max_array_from_right(arr, n):
    max_profit = 0
    max_price_array = [-1] * n
    max_price_array[n - 1] = arr[n - 1]

    # store maximum stock price on right of each index
    for i in range(n - 2, -1, -1):
        if max_price_array[i + 1] > arr[i]:
            max_price_array[i] = max_price_array[i + 1]
        else:
            max_price_array[i] = arr[i]

    for i in range(0, n):
        curr_profit = max_price_array[i] - arr[i]
        if curr_profit > max_profit:
            max_profit = curr_profit

    return max_profit


# O(n) -- space O(1)
def find_max_profit_using_min_max(arr, n):
    max_profit = 0
    min_price_so_far = arr[0]

    for i in range(1, n):
        curr_profit = arr[i] - min_price_so_far
        if max_profit < curr_profit:
            max_profit = curr_profit

        if arr[i] < min_price_so_far:
            min_price_so_far = arr[i]

    return max_profit


if __name__ == '__main__':
    print(find_max_profit_naive_solution([100, 180, 260, 310, 40, 535, 695], 7))
    print(find_max_profit_using_min_max([100, 180, 260, 310, 40, 535, 695], 7))
    print(find_max_profit_using_max_array_from_right([100, 180, 260, 310, 40, 535, 695], 7))
