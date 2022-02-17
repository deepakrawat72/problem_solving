def product_of_items(nums, n):
    if n == 1:
        return 0

    product = 1
    zero_count = 0
    for i in range(n):
        if nums[i] == 0:
            zero_count += 1
        else:
            product *= nums[i]

    for i in range(n):
        if nums[i] == 0 and zero_count == 1:
            nums[i] = product
        elif zero_count >= 1:
            nums[i] = 0
        else:
            nums[i] = product // nums[i]

    return nums


if __name__ == '__main__':
    print(product_of_items([1, 0], 2))
    print(product_of_items([1, 2, 3, 4, 0], 5))
    print(product_of_items([0, 8, 6, 2, 4, 7, 9, 3, 9, 2, 8, 3, 0, 1, 7, 8, 9, 1, 5, 4, 9, 2, 5, 7, 4, 9, 9, 4], 28))
