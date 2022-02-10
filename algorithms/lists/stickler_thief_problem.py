# Stickler the thief wants to loot money from a society having n houses in a single line. He is a weird person and
# follows a certain rule when looting the houses. According to the rule, he will never loot two consecutive houses.
# At the same time, he wants to maximize the amount he loots. The thief knows which house has what amount of money
# but is unable to come up with an optimal looting strategy. He asks for your help to find the maximum money he can
# get if he strictly follows the rule. Each house has a[i]amount of money present in it.

# Input:
# n = 6
# a[] = {5,5,10,100,10,5}
# Output: 110
# Explanation: 5+100+5=110

def max_amount_robbed(arr, n):
    if n < 0:
        return 0
    if n == 0:
        return arr[0]

    pick = arr[n] + max_amount_robbed(arr, n - 2)
    not_pick = max_amount_robbed(arr, n - 1)

    return max(pick, not_pick)


# with_dp
def get_max_amount_robbed(arr, n):
    dp = [-1] * (n + 1)

    def max_amount_robbed(arr, n, dp):
        if n < 0:
            return 0
        if n == 0:
            return arr[0]

        if dp[n] != -1:
            return dp[n]

        pick = arr[n] + max_amount_robbed(arr, n - 2, dp)
        not_pick = max_amount_robbed(arr, n - 1, dp)

        dp[n] = max(pick, not_pick)
        return dp[n]

    max_amount_robbed(arr, n, dp)


if __name__ == '__main__':
    # print(max_amount_robbed([5, 5, 10, 100, 10, 5], 5))
    # print(max_amount_robbed([1, 2, 3], 2))
    print(get_max_amount_robbed([5, 5, 10, 100, 10, 5], 5))
