# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

def searchInsert(nums, target) -> int:
    l = 0
    h = len(nums) - 1

    while l <= h:

        mid = int((l + h) / 2)

        if nums[mid] == target:
            return mid

        elif target > nums[mid]:
            if mid == h:
                return mid + 1
            else:
                l = mid + 1
        else:
            if mid == l:
                return mid
            else:
                h = mid - 1


if __name__ == '__main__':
    nums = [1, 3, 5, 6]

    print(searchInsert(nums, 0))
