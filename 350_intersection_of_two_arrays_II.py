class Solution:
    def interset(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.interset(nums2, nums1)

        """
        A common problem that you can face when working with Python dictionaries is to try to access or modify keys that don’t exist in the dictionary. This will raise a KeyError and break up your code execution. To handle these kinds of situations, the standard library provides the Python defaultdict type, a dictionary-like class that’s available for you in collections.

The Python defaultdict type behaves almost exactly like a regular Python dictionary, but if you try to access or modify a missing key, then defaultdict will automatically create the key and generate a default value for it. This makes defaultdict a valuable option for handling missing keys in dictionaries.
        """
        lookup = collections.defaultdict(int)
        for i in nums1:
            lookup[i] += 1

        result = list()
        for i in nums2:
            if lookup[i] > 0:
                result.append(i)
                lookup[i] -= 1

        return result
