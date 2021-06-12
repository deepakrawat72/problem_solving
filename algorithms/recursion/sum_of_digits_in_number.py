def sum_of_digits(number):
    if number < 10:
        return number

    return sum_of_digits(number // 10) + number % 10


if __name__ == '__main__':
    no = 12345
    result = sum_of_digits(no)
    print(result)
    no = 99999
    result = sum_of_digits(no)
    print(result)