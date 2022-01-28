def find_leader_items_naive(arr):
    leaders = []
    for i in range(0, len(arr)):
        is_leader = True
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                is_leader = False
                break
        if is_leader:
            leaders.append(arr[i])

    return leaders


def find_leader_items_optimized(arr):
    curr_leader = arr[len(arr) - 1]
    leader_items = [curr_leader]
    i = len(arr) - 2

    while i >= 0:
        if curr_leader < arr[i]:
            curr_leader = arr[i]
            leader_items.append(curr_leader)

        i -= 1

    return sorted(leader_items, reverse=True)


if __name__ == '__main__':
    print(find_leader_items_naive([16, 17, 4, 3, 5, 2]))
    print(find_leader_items_optimized([16, 17, 4, 3, 5, 2]))
