def find_pairs_with_zero_sum(arr, sum_to_find):
    curr_sum = 0
    no_of_pairs = 0
    cum_sums = {}
    for index in range(0, len(arr)):
        curr_sum += arr[index]
        print(f'cumulative sum ({cum_sums})')
        if arr[index] == sum_to_find or curr_sum in cum_sums:
            print(f'sub-array found at ({cum_sums[curr_sum] + 1},{index})')
            no_of_pairs += 1
        cum_sums[curr_sum] = index

    print(f'No of pairs found : {no_of_pairs}')


def find_pairs_with_x_sum(arr, sum_to_find):
    curr_sum = 0
    no_of_pairs = 0
    cum_sums = {}
    for index in range(0, len(arr)):
        curr_sum += arr[index]
        print(f'cumulative sum ({cum_sums})')
        x = curr_sum - sum_to_find
        if arr[index] == sum_to_find or x in cum_sums:
            print(f'sub-array found at ({cum_sums[x] + 1},{index})')
            no_of_pairs += 1
        cum_sums[curr_sum] = index

    print(f'No of pairs found : {no_of_pairs}')


if __name__ == '__main__':
    arr = [1, 3, 4, -4, 6, -6]
    given_sum = 0
    find_pairs_with_zero_sum(arr, given_sum)

    arr = [1, 3, 4, -4, 6, -6]
    given_sum = 2
    find_pairs_with_x_sum(arr, given_sum)
