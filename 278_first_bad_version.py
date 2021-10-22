class Solution:
    def firstBadVersion(self, n):
        start, end = 1, n + 1

        while start < end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1

        if isBadVersion(start) == True:
            return start

        return -1
