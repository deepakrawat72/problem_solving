def find_largest_sub_array_with_zero_sum(arr):
    curr_sum = 0
    cumulative_sum_dict = {}
    largest_sub_array_length = 0

    for i in range(0, len(arr)):
        curr_sum = curr_sum + arr[i]

        if curr_sum == 0 and (i + 1) > largest_sub_array_length:
            largest_sub_array_length = i + 1
            cumulative_sum_dict[curr_sum] = i

        if curr_sum in cumulative_sum_dict:
            sub_array_start_index = cumulative_sum_dict[curr_sum] + 1
            sub_array_end_index = i + 1
            length_of_sub_array = sub_array_end_index - sub_array_start_index
            if length_of_sub_array > largest_sub_array_length:
                largest_sub_array_length = length_of_sub_array
        else:
            cumulative_sum_dict[curr_sum] = i

    return largest_sub_array_length


if __name__ == '__main__':
    print(find_largest_sub_array_with_zero_sum([1, -1, 4, 5, 7, -2, 2, -1, 1, 5, 6, -8, -6]))
