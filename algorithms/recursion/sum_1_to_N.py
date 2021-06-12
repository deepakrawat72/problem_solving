def sum_1_to_n(n):
    if n == 0:
        return 0

    return sum_1_to_n(n - 1) + n


if __name__ == '__main__':
    print(sum_1_to_n(5))
