class Solution:
    def sortedSquares(self, nums):
        """
        Givin an integer array nums sorted in ascending order, return an array of
        the square of eash number sorted in non-descending order
        [-4, -1, 0, 3, 10] after squaring
        [16, 1, 0, 9, 100]
        return [0, 1, 9, 16, 100]]
        """
        # Solution 1
        # Time complexity: O(nlogn)
        # Space complexity: O(n)
        result = list()

        for i in range(len(nums)):
            result.append(nums[i] * nums[i])

        result.sort()
        return result

    def sortedSquares_twoPointers(self, nums):
        """
        Solution 2 is to use 2 pointers to solve the problem
        [-4, -1, 0, 3, 10]
        left           right
        absolute_value[right] > absolute_value[left] => right^2 > left^2 => result.insert(0, 100) =>
        [100]
        right - 1
        absolute_value[right] < absolute_value[left] => right^2 < left^2 => result.insert(0, 16) =>
        [16, 100]
        left + 1
        abs() function to get the absolute value
        ... ...
        """
        result = list()
        left, right = 0, len(nums) - 1
        
        for i in range(len(nums)):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1

            result.insert(0, square * square)

        return result


