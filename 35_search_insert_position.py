class Solution:
    def searchInsert(self, nums, target):
        """
        Given a sorted list of distinct integers and a target value, return index if the target is
        found. If not, return the index where it would be if it were inserted in order.
        """
        # If the target number is greater than any of the numbers in the list,
        # Then the target is inserted to the end of the list
        if target > nums[len(nums) - 1]:
            return len(nums)
        
        # If the target is found in the list, then return the index of the number,
        # otherwise if the number in the list is greater than the target, the position of the
        # number is to be occupied by the target, so return the index of the number.
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
