# https://leetcode.com/problems/search-insert-position/


def find_index(nums, target):
    l = 0
    r = len(nums) - 1

    if target < nums[l]:
        return 0
    if target > nums[r]:
        return r + 1

    while l <= r:
        if nums[l] == target or target < nums[l]:
            return l
        elif nums[r] == target:
            return r
        elif target > nums[r]:
            return r + 1

        l += 1
        r -= 1

    return l


if __name__ == '__main__':
    arr = [1, 3]
    print(find_index(arr, 2))
