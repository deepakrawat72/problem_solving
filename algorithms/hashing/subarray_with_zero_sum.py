def sub_array_with_zero_sum(list):
    for i in range(0, len(list)):
        start_idx = i
        s = 0

        if list[i] == 0:
            return True

        for j in range(start_idx, len(list)):
            s = s + list[j]

            if s == 0:
                return True

    return False


# In this approach we take the cumulative sum in a set and check if it contains the curr_sum, if yes then it has a
# sub_array with sum 0
# -3, 4, -3, -1, 1
# \_____-3____/
#     \___0___/

def sub_array_with_zero_sum_option_2(list):
    cumulative_sum = set()
    curr_sum = 0
    for i in range(0, len(list)):
        curr_sum = curr_sum + list[i]

        if curr_sum == 0 or cumulative_sum in cumulative_sum:
            return True

        cumulative_sum.add(curr_sum)

    return False


if __name__ == '__main__':
    print(sub_array_with_zero_sum([1, 4, 13, -3, -10, 5]))
    print(sub_array_with_zero_sum([-1, 4, -3, -3, 5, 1]))
    print(sub_array_with_zero_sum([3, 1, -2, 5, 6]))
    print(sub_array_with_zero_sum([5, 6, 0, 8]))
