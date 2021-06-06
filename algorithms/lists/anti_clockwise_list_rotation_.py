def reverse(l, s_idx, e_idx):
    while (s_idx < e_idx):
        l[s_idx], l[e_idx] = l[e_idx], l[s_idx]
        s_idx = s_idx + 1
        e_idx = e_idx - 1


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    n = len(list1)
    d = 3
    reverse(list1, 0, d - 1)
    reverse(list1, d, n - 1)
    reverse(list1, 0, n - 1)

    print(list1)

