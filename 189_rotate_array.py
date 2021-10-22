# Solution 1: Time limit exceeds
def rotate_array(nums, k):
    while (i := 1) <= k:
        pop_num = nums.pop()
        nums.insert(0, pop_num)
        i += 1

# Solution 2: output is wrong
# but it workes on python console
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    pivot = len(nums) - k
    left_nums = nums[:pivot]
    right_nums = nums[pivot:]
    nums = right_nums + left_nums

# Solution 3: Swap position
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # k might be longer than the length of the list
    k = k % len(nums)

    nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]
