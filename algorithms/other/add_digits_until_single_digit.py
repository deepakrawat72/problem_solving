def add_digits(num):
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9


if __name__ == '__main__':
    print(add_digits(38))
    print(add_digits(9))
    