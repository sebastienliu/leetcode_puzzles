class Solution:
    def combine(self, n, k):
        """
        n = 4, k = 2
        Pick 2 numbers from [1, 2, 3, 4]
        [1, 2] [1, 3] [1, 4]
        [2, 3] [2, 4]
        [3, 4]
        From the starting point, only choose the greater numbers.
        """
        result = []

        def backtrack(start, combination):
            if len(combination) == k:
                result.append(combination.copy())
                return

            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1, combination)
                combination.pop()

        backtrack(1, [])
        return result
