class Solution:
    def maximumSubarray(self, nums):
        """
        Strategy: Remove negative prefix

        negative sum is useless to the solution
        """
        maxSub = nums[0]
        currentSum = 0

        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n
            maxSub = max(maxSub, currentSum)
        return maxSub
