# Solution 1
class Solution(object):
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        lookup = Counter(s)

        for i,c in enumerate(s):
            if lookup[c] == 1:
                return i

        return -1

# Solution 2
class Solution(object):
    def firstUniqChar(self, s: str) -> int:
        lookup = dict()

        for char in s:
            if char in lookup:
                lookup[char] += 1
            else:
                lookup[char] = 1

        for i, char in enumerate(s):
            if lookup[char] == 1:
                return i

        return -1
