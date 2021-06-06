def sum_of_digits(number):
    if number < 10:
        return

    return sum_of_digits(number // 10) + number % 10


if __name__ == '__main__':
    result = sum_of_digits(12345)
    print(result)
