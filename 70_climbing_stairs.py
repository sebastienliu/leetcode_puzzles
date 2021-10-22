class Solution:
    def climbStairs(self, n):
        """
        n = 1: output = 1
        n = 2: output = 2
        n = 3: output = 3
        n = 4: output = 5
        n = 5: output = 8
        ... (Fibonacci)
        """
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current
        return current

    # n = 1:  prev = 0, current = 1
    # n = 2:  prev = 1, current = 1 + 1 = 2
    # n = 3:  prev = 2, current = 1 + 2 = 3
