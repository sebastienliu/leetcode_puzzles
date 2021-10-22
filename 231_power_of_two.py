# Solution 1
class Solution:
    def isPowerOfTwo(self, n):
        if n < 1:
            return False

        while n % 2 == 0:
            n /= 2
        return True if n == 1 else False


# Solution 2
class Solution:
    def isPowerOfTwo(self, n):
        """
        2: 0010
        4: 0100
        8: 1000
        """
        return n > 0 and (n & (n - 1)) == 0
