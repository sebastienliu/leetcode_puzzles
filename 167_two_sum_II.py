# [3, 4, 5, 6, 8, 9]
# target is 9
# return the index of 4 and 5, but not zero-based
# should return [2, 3]
def twoSums(numbers, target):
    left, right = 0, len(numbers) - 1
    sum = 0
    while left != right:
        sum = numbers[left] + numbers[right]
        if sum > target:
            right -= 1
        elif sum < target:
            left += 1
        else:
            return [left + 1, right + 1]
