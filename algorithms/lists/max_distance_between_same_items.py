def max_distance_between_same_items(arr, n):
    items_max_position_dict = {}
    max_distance = 0

    for i in range(0, n):
        if arr[i] in items_max_position_dict:
            curr_item_distance = i - items_max_position_dict[arr[i]]
            if max_distance < curr_item_distance:
                max_distance = curr_item_distance
        else:
            items_max_position_dict[arr[i]] = i

    return max_distance

if __name__ == '__main__':
    print(max_distance_between_same_items([1, 1, 2, 2, 2, 1], 6))
