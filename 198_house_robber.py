# Solution 1 (do not fully understand)
class Solution:
    def rob(self, nums):
        """
        [2, 7, 9, 3, 1]
        in house: 3 (amount of money: 9
        - current max amount of money: 11
        - last point max amount of money: 7
        in house 4 (amount of money: 3
        - last point in 7: 7 + current money in house 3 => 10
        Compare with the last point: 10 < 11
        Current max amount of money 11


        iteration 1: last == 0, now == 0 => now = 0, max(0 + 2, 0) => now = 2
        iteration 2: last == 2, now ==

        """
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last + num, now)
        return now


# Solution 2
class Solution:
    def rob(self, nums):
        if not nums:
            return 0

        result = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                result[0] = nums[0]
            elif i == 1:
                result[1] = max(nums[0], nums[1])
            else:
                result[i] = max(nums[i] + result[i-2], result[i-1])
        return result[-1]
