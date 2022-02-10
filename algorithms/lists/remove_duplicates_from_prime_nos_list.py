# A prime no. can only be divisible by itself so if we keep taking the product at each item and
# check if the after dividing the remainder is zero, it means this divisor prime number is duplicate item.
def remove_duplicates(arr):
    product = 1
    de_dup_arr = []
    for i in range(0, len(arr)):
        if product % arr[i] != 0:
            de_dup_arr.append(arr[i])

        product *= arr[i]

    return de_dup_arr


def remove_duplicates_method_2(arr):
    unique_items = set()
    last_unique_item_index = -1
    for i in range(0, len(arr)):
        if arr[i] not in unique_items:
            arr[last_unique_item_index + 1] = arr[i]
            last_unique_item_index += 1

        unique_items.add(arr[i])

    return arr[0: last_unique_item_index + 1]


if __name__ == '__main__':
    print(remove_duplicates_method_2([2, 2, 2, 3, 3, 3, 5]))
