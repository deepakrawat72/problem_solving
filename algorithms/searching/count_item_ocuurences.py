from searching import find_first_occurence_of_item, find_last_occurrence_of_item


def find_no_of_occurrences(arr, item):
    first = find_first_occurence_of_item.find_first_occurrence(arr, item)

    if first == -1:
        return 0
    else:
        return find_last_occurrence_of_item.find_last_occurrence(arr, item) - first + 1


if __name__ == '__main__':
    print(find_no_of_occurrences([5, 10, 10, 10, 12, 15], 2))
