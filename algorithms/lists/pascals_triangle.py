# https://leetcode.com/problems/pascals-triangle/

#         [1]
#         [1, 1]
#         [1, 2, 1]
#         [1, 3, 3, 1]
#         [1, 4, 6, 4, 1]


def create_pascals_triangle(no_of_row):
    final_arr = [[1]]
    for i in range(2, no_of_row + 1):
        last_row = final_arr[i - 2]
        curr_row = []
        for j in range(0, i):
            if j == 0 or j == i-1:
                curr_row.append(1)
            else:
                curr_row.append(last_row[j - 1] + last_row[j])

        final_arr.append(curr_row)

    return final_arr


if __name__ == '__main__':
    rows = create_pascals_triangle(8)
    for row in rows:
        print(str(row) + "\n")
