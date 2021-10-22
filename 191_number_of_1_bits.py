# Solution 1
class Solution:
    def hammingWeight(self, n):
        """
        n     = 1011
        n - 1 = 1010
        n & (n - 1) = 1010
        """
        answer = 0
        while n:
            n = n & (n - 1)
            answer += 1
        return answer


# Solution 2
class Solution:
    def hammingWeight(self, n):
        """
        using n to & 1, only if n == 1, the result is 1, otherwise the result is 0
        >> is the bit right shift
        """
        nums_bits = 0
        while n:
            nums_bits += n & 1
            n >>= 1
        return nums_bits

