# find all items from a list which appears odd times and which occurs even time
def find_even_odd_appearing_items(list):
    odd_appearing_items = set()
    even_appearing_items = set()
    for item in list:
        if list.count(item) % 2 == 0:
            even_appearing_items.add(item)
        else:
            odd_appearing_items.add(item)

    return even_appearing_items, odd_appearing_items
