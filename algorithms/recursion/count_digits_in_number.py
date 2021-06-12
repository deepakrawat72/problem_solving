def no_of_digits(number):
    if number < 10:
        return 1

    return no_of_digits(number // 10) + 1


if __name__ == '__main__':
    no = 12345
    result = no_of_digits(no)
    print(result)
    no = 99999786780
    result = no_of_digits(no)
    print(result)
