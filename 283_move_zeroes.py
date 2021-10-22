# Input: [0, 1, 0, 3, 9, 16]
# Output:[1, 3, 9, 16, 0, 0]

# Solution 1:
def moveZeroes(self, nums):
        pivot = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                pivot += 1


# Solution 2:
def moveZeroes(self, nums):
        pivot = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pivot] = nums[i]
                pivot += 1

        for i in range(pivot, len(nums)):
            nums[i] = 0
