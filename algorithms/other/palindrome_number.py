def palindrome_checker(num):
    if num <= 9:
        return True
    if num < 0:
        return False

    reversed_digit = 0

    while num > reversed_digit:
        reversed_digit = reversed_digit * 10 + num % 10
        num //= 10

    return num == reversed_digit or num == reversed_digit // 10


if __name__ == '__main__':
    print(palindrome_checker(121))
