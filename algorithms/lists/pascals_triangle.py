# https://leetcode.com/problems/pascals-triangle/

def create_pascals_triangle(no_of_row):
    final_list = []
    for index in no_of_row:
        [1]
        [1, 1]
        [1, 2, 1]
        [1, 3, 3, 1]
        [1, 4, 6, 4, 1]
        [1, 5, 10, 10, 5, 1]
        [1, 6, 15, 20, 15, 6, 1]
        [1, 7, 21, 35, 35, 21, 7, 1]

        i = 0
        j = no_of_row

        for i in range(1, no_of_row):
            
