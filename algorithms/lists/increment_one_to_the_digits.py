def plus_one(nums):
    current_idx = 0
    last_carry_over = 1
    nums.reverse()
    while current_idx < len(nums) and last_carry_over == 1:
        plus_one_value = nums[current_idx] + last_carry_over
        if plus_one_value == 10:
            nums[current_idx] = 0
            last_carry_over = 1
        else:
            nums[current_idx] = plus_one_value
            last_carry_over = 0

        current_idx += 1

    if last_carry_over == 1:
        nums.append(1)

    nums.reverse()

    return nums


if __name__ == '__main__':
    arr = [9]
    print(plus_one(arr))
