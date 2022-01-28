def reverse(l, s_idx, e_idx):
    while s_idx < e_idx:
        l[s_idx], l[e_idx] = l[e_idx], l[s_idx]
        s_idx = s_idx + 1
        e_idx = e_idx - 1


def rotate_anti_clock_wise(list1, digits):
    n = len(list1)
    reverse(list1, 0, digits - 1)
    reverse(list1, digits, n - 1)
    reverse(list1, 0, n - 1)


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    digits = 3
    rotate_anti_clock_wise(list1, digits)
    print(list1)
