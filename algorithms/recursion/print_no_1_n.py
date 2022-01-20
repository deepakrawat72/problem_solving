def print_1_to_n(n):
    if n <= 0:
        return

    print_1_to_n(n - 1)
    print(str(n), end=' ')


def count_digits(n):
    if n // 10 == 0:
        return 1

    return count_digits(n // 10) + 1


def sum_of_digits(n):
    if n // 10 == 0:
        return n

    return sum_of_digits(n // 10) + n % 10


if __name__ == '__main__':
    # print_1_to_n(10)
    #print(count_digits(234567893456))
    print(sum_of_digits(3459876))
