def find_max_profit_naive_solution(arr, n):
    max_profit = -1

    for i in range(0, n):
        for j in range(i + 1, n):
            diff = arr[j] - arr[i]

            if diff > max_profit:
                max_profit = diff

        return max_profit


if __name__ == '__main__':
    print(find_max_profit_naive_solution([100, 180, 260, 310, 40, 535, 695], 7))
