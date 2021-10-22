class Solution:
    def containsDuplicate(self, nums):
        d_nums = set()
        for val in nums:
            if val in d_nums:
                return True
            d_nums.add(val)
        return False
