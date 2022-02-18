def max_profit_in_stocks(arr, n):
    last_min_price = arr[0]
    last_max_profit = 0
    max_profit = 0

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            max_profit += last_max_profit
            last_max_profit = 0
            last_min_price = arr[i]
        else:
            curr_profit = arr[i] - last_min_price
            if curr_profit > last_max_profit:
                last_max_profit = curr_profit

    max_profit += last_max_profit

    return max_profit


def max_profit_valley_peak_approach(arr, n):
    max_profit = 0

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            max_profit += (arr[i] - arr[i - 1])

    return max_profit


if __name__ == '__main__':
    # print(max_profit_in_stocks([5, 2, 7, 3, 6, 1, 2, 4], 8))  # 11
    print(max_profit_in_stocks([10, 22, 5, 75, 87, 80], 6))  # 87
    print(max_profit_valley_peak_approach([10, 22, 5, 75, 87, 80], 6))  # 87
    # print(max_profit_in_stocks([2, 30, 15, 10, 8, 25, 80], 7))  # 100
    # print(max_profit_in_stocks([100, 30, 15, 10, 8, 25, 80], 7))  # 72
    # print(max_profit_in_stocks([90, 80, 70, 60, 50], 5))  # 0
